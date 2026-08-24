# 06. Custom AST Linter Rules & Static Guardrails (Tree Graphs & Static Analysis)

## 1. Overview & Problem Statement
Code conventions and architectural rules often decay over time without automated enforcement. Manual code reviews frequently miss unpaginated queries leading to Out-Of-Memory (OOM) failures or mutable dependency injections causing race conditions. This chapter formalizes static code analysis, Abstract Syntax Tree (AST) tree-traversal invariants, and automated rewrite rules.

## 2. DISMATH Theoretical Foundation
- **Tree Structures & Graph Theory (`08`):** Abstract Syntax Trees as rooted, directed acyclic trees $\mathcal{T} = \langle \mathcal{V}, \mathcal{E}, r \rangle$.
- **Quantified Tree Invariants (`03`):** Universal assertions over specific node subsets ($\forall v \in \mathcal{V}_{\text{class}}, P(v)$).
- **Confluent Tree Rewriting (`08`):** Finite-step monotonic AST code transformations (Auto-Fixers).

## 3. Formal Mathematical Specifications

### 3.1 Abstract Syntax Tree (AST) as a Directed Tree
An Abstract Syntax Tree is a directed acyclic tree $\mathcal{T} = \langle \mathcal{V}, \mathcal{E}, r \rangle$, where:
- $\mathcal{V}$ is the set of AST nodes (ClassDeclaration, MethodDefinition, ParameterProperty, etc.).
- $\mathcal{E} \subset \mathcal{V} \times \mathcal{V}$ is the set of parent-child syntax edges.
- $r \in \mathcal{V}$ is the root Program node.

### 3.2 Immutability Invariant Rule ($\text{Rule}_{\text{readonly}}$)
Let $\mathcal{V}_{\text{class}} \subset \mathcal{V}$ be class declaration nodes.
$$\forall v \in \mathcal{V}_{\text{class}}, \quad \text{HasDecorator}(v, \text{'Injectable'} \lor \text{'Controller'}) \implies \left( \forall p \in \text{Params}(\text{Ctor}(v)), \text{IsReadonly}(p) \right)$$

### 3.3 Memory Safety Query Invariant ($\text{Rule}_{\text{pagination}}$)
Let $\mathcal{V}_{\text{query}} \subset \mathcal{V}$ be TypeORM repository query call nodes.
$$\forall v \in \mathcal{V}_{\text{query}}, \quad \text{MethodName}(v) \in \{\text{'find'}, \text{'getMany'}\} \implies \text{HasOption}(v, \text{'take'} \lor \text{'limit'})$$

## 4. Invariants & Mathematical Proofs

### 4.1 Decidability and Finite Termination of AST Traversal
- **Theorem:** For any source file with $N$ AST nodes, the custom linter inspection terminates in $O(N)$ steps.
- **Proof:**
  1. The AST $\mathcal{T}$ is a finite tree with $|\mathcal{V}| = N < \infty$.
  2. The visitor pattern visits each node $v \in \mathcal{V}$ exactly once via depth-first search.
  3. Pattern matching and predicate evaluations at each node take $O(1)$ local operations.
  4. Therefore, total execution time is $O(N)$ and halting is guaranteed. $\blacksquare$

### 4.2 Confluence of Auto-Fix Rewriter
- **Theorem:** Applying the `readonly` auto-fixer transforms the AST to satisfy the Immutability Invariant monotonically without introducing syntax conflicts.
- **Proof:** The auto-fixer performs a deterministic string insertion (`' readonly'`) directly after the access modifier token (`'private'`), transforming $\text{IsReadonly}(p) = \text{False} \to \text{True}$ in a single pass. $\blacksquare$

## 5. Sanitized Generic Implementation

```javascript
import { AST_NODE_TYPES, ESLintUtils } from '@typescript-eslint/utils';

const createRule = ESLintUtils.RuleCreator((name) => `custom/${name}`);

/**
 * AST Rule: Enforces 'readonly' on injected constructor dependencies in NestJS classes
 */
export const nestjsReadonlyInjectablesRule = createRule({
  name: 'nestjs-readonly-injectables',
  meta: {
    type: 'suggestion',
    docs: {
      description: 'Enforce readonly modifier for injected dependencies in NestJS classes',
    },
    fixable: 'code',
    messages: {
      missingReadonly: 'Dependency injection "{{name}}" should be marked as readonly.',
    },
    schema: [],
  },
  defaultOptions: [],
  create(context) {
    return {
      ClassDeclaration(node) {
        const hasNestDecorator = node.decorators && node.decorators.some((d) => {
          if (d.expression.type === AST_NODE_TYPES.CallExpression) {
            const callee = d.expression.callee;
            return callee.type === AST_NODE_TYPES.Identifier &&
              (callee.name === 'Injectable' || callee.name === 'Controller');
          }
          return false;
        });

        if (!hasNestDecorator) return;

        const ctor = node.body.body.find(
          (el) => el.type === AST_NODE_TYPES.MethodDefinition && el.kind === 'constructor',
        );
        if (!ctor) return;

        for (const param of ctor.value.params) {
          if (param.type === AST_NODE_TYPES.TSParameterProperty && !param.readonly) {
            const paramName = param.parameter.type === AST_NODE_TYPES.Identifier ? param.parameter.name : 'unknown';

            context.report({
              node: param,
              messageId: 'missingReadonly',
              data: { name: paramName },
              fix(fixer) {
                const sourceCode = context.sourceCode;
                const tokens = sourceCode.getTokens(param);
                const modifierToken = tokens.find(
                  (t) => t.value === 'private' || t.value === 'protected' || t.value === 'public',
                );
                if (modifierToken) {
                  return fixer.insertTextAfter(modifierToken, ' readonly');
                }
                return null;
              },
            });
          }
        }
      },
    };
  },
});
```

## 6. Complexity & Algebraic Properties
- **Time Complexity:** $O(N)$ linear traversal across all $N$ AST syntax nodes.
- **Memory Complexity:** $O(D)$ where $D$ is the maximum AST nesting depth.
- **Formal Invariant Guarantee:** Compile-time AST linting prevents runtime immutability bugs.
