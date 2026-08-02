# 07 - Component Architecture

## 1. Copy-and-Own Philosophy (Magic UI / shadcn)

A modern design system does not always need to be an installed NPM package. Copying a component into the project, for example `src/components/ui/`, gives the team direct ownership of its code.

**Benefits:** the project can customize the component completely, avoid waiting for a library release, and avoid hacks around code it does not own. Copying is appropriate only when the project can maintain the component and its accessibility contract.

## 2. Self-Contained and Modular

- Components such as `Card`, `Button`, and `Modal` should provide a complete, understandable behavior boundary.
- Minimize external dependencies when the platform or an existing utility already solves the problem.
- Keep closely related logic and styling together while extracting genuinely shared behavior rather than duplicating it.

## 3. Composition over Configuration

Avoid a component that accepts dozens of flags such as `<Table data={...} hideHeader={true} color="red" />`. Compose smaller parts instead:

```tsx
<Table>
  <TableHeader>
    <TableRow>
      <TableHead>Title</TableHead>
    </TableRow>
  </TableHeader>
  <TableBody>...</TableBody>
</Table>
```

Compound components remain flexible, readable, and easier to adapt to a different table shape.

## 4. Semantic and Accessible Components

- Start with native HTML controls before creating a custom widget.
- Every custom component needs an accessible name, semantic role, keyboard interaction, visible focus, and correct state attributes.
- Treat loading, empty, error, disabled, and responsive behavior as part of the component contract when the component can encounter them.
