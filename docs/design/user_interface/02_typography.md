# 02 - Typography (Inter / Modern Sans-Serif)

## 1. Typeface Choice

- **Primary font:** choose a readable modern geometric sans-serif such as **Inter**, **Geist**, or **Roboto**.
- Do not combine too many typefaces. Normally use no more than two: one for headings and one for body text.

## 2. Type Hierarchy

- **Headings (H1, H2):** use larger size, bold or semibold weight, and tighter tracking such as `tracking-tight`.
- **Body text:** use regular weight and comfortable line length for long passages.
- **Labels and metadata:** use a smaller size (`text-sm` or `text-xs`), medium weight, and optional wider tracking. Uppercase labels may use `uppercase tracking-wider text-foreground/50` when that improves scanning.

## 3. Contrast by Weight and Opacity

Create hierarchy with weight and opacity before adding many font sizes or unrelated colors. For example, primary data can use `font-medium text-foreground`, while supporting data uses `text-sm text-foreground/60`.

## 4. Tabular Numerals

For data-heavy or financial applications such as portfolios and trading screens, enable tabular numerals (`tabular-nums`). Equal digit widths keep table columns aligned and prevent values from jumping when an animated number changes.
