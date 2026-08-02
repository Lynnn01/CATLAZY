# 00 - Design Tokens Contract

Design tokens are semantic names, not raw visual values in components. The implementation may use CSS custom properties, theme objects, or platform equivalents.

## Required token groups

| Group | Minimum semantic tokens |
|---|---|
| Color | `surface`, `surface-raised`, `text`, `text-muted`, `border`, `action`, `danger`, `success`, `focus` |
| Typography | `font-body`, `font-mono`, `text-body`, `text-small`, `text-heading`, `line-body` |
| Space | `space-1` through `space-8` on a 4px scale |
| Shape | `radius-control`, `radius-panel`, `border-width` |
| Elevation | `shadow-raised`, `shadow-overlay`, `z-dropdown`, `z-modal`, `z-toast` |
| State | `action-hover`, `action-active`, `action-disabled`, `field-error`, `field-success` |

## Implementation rules

- Define light, dark, and high-contrast values at the theme boundary; components consume semantic tokens only.
- A state must preserve readable text, visible focus, and non-color feedback.
- Use component-local values only when no semantic token describes the intent; promote repeated values to a token.

```css
:root {
  --color-surface: #ffffff;
  --color-text: #171717;
  --color-action: #1d4ed8;
  --space-1: 0.25rem;
  --radius-control: 0.5rem;
}
```
