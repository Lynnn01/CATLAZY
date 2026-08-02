# 01 - Color System (Monochrome Minimal + Magic UI)

## 1. Monochrome First

- **Background and foreground:** use white, black, or dark neutrals as the structural foundation in every theme. Use semantic tokens such as `bg-background` and `text-foreground` to keep the system coherent.
- **Hierarchy:** keep the primary palette to one or two colors. For secondary elements, use opacity such as `text-foreground/70` or `bg-foreground/5` instead of introducing many unrelated gray values.

## 2. Accents for Purpose

Vibrant colors such as red, green, and blue communicate meaning; they are not decoration.

- 🟢 **Green (success/profit):** positive outcomes, gains, and successful completion.
- 🔴 **Red (danger/loss):** loss, destructive actions, and important warnings.
- 🔵 **Blue (brand/action):** a primary call to action or the place where the user should focus.

In dark mode, accents need sufficient luminance to separate from the background. A restrained glow may help, but it never replaces contrast.

## 3. High-Fidelity Details

- Avoid flat solid color across large surfaces when a more subtle surface treatment improves depth.
- **Gradients:** use soft gradients on cards or important buttons; the end of the gradient should blend into the surrounding theme.
- **Borders:** prefer translucent borders such as `border-foreground/10` over solid colors so light and dark themes remain consistent automatically.
