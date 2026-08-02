# 06 - Visual Depth and Aesthetics (Glassmorphism and Glow)

## 1. Glassmorphism and Translucency

Create depth with a restrained glass treatment when it communicates layering:

- Instead of an opaque modal or top navigation surface, use a translucent token-based surface such as `bg-background/80`.
- Pair it with `backdrop-blur-md` only when the resulting text and controls remain readable.
- The effect should make it obvious that a dialog or navigation layer floats above the content behind it.

## 2. Elevating with Shadows and Glows

- **Soft drop shadows:** avoid harsh black box shadows. Prefer broad, soft, low-opacity elevation such as `shadow-2xl` with `shadow-foreground/5`.
- **Glow effects:** dark themes may benefit from a subtle accent glow under an important card or button when a normal shadow would disappear.

## 3. Subtlety Is Key

Use shadows, blur, and glow sparingly. If every surface reflects light and blurs the background, the interface becomes noisy and competing elements lose hierarchy. Reserve the strongest treatments for primary buttons, important toasts, or focused pricing/action cards.

## 4. Patterns, Not Defaults

Glass, glow, gradients, and shadows are options, not mandatory decorations. Use them only when they separate layers or emphasize an action, and validate contrast, readability, and performance in every theme.
