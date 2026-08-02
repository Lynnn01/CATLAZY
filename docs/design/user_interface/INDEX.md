# Unified Design Systems Index

This index is the single source of truth for the project’s UI rules and style guidance. It unifies the project’s Design Rules, Magic UI principles, and reusable design-system patterns.

## 📚 Design Guidelines

| File | Main coverage |
|---|---|
| [00_design_tokens.md](00_design_tokens.md) | Semantic tokens for themes, states, spacing, typography, and elevation |
| [01_color_system.md](01_color_system.md) | Monochrome-first color, semantic red/green accents, and subtle gradients |
| [02_typography.md](02_typography.md) | Inter, type hierarchy, weight/opacity contrast, and tabular numerals |
| [03_spacing_and_layout.md](03_spacing_and_layout.md) | 4px/8px grid, bento layouts, whitespace, and responsive grouping |
| [04_components_and_states.md](04_components_and_states.md) | Hover/active/focus states, skeletons, empty states, radii, and glow |
| [05_motion_and_animations.md](05_motion_and_animations.md) | Meaningful animation, staggered entries, micro-interactions, and reduced motion |
| [06_visual_depth_and_aesthetics.md](06_visual_depth_and_aesthetics.md) | Glassmorphism, soft shadows, glow, and visual restraint |
| [07_component_architecture.md](07_component_architecture.md) | Copy-and-own components, composition, and accessible boundaries |
| [08_design_philosophy.md](08_design_philosophy.md) | Anti-generic intent, professional flow, and data as the hero |

## 🚦 Critical Rules Checklist

Before pushing code or creating a new UI:

- [ ] Use **CSS variables and semantic tokens** instead of hard-coded colors such as `#ffffff`.
- [ ] Interactive controls include `transition-colors`, hover, pressed, disabled, and visible focus states as applicable.
- [ ] Important interactions work with keyboard, touch, and pointer; focus is visible and not covered.
- [ ] Motion respects `prefers-reduced-motion` and does not degrade performance.
- [ ] Data loading has a deliberate loading state (skeleton or spinner).
- [ ] Empty tables and lists have a useful empty state instead of a blank page.
- [ ] Financial values use tabular numerals where alignment matters.
- [ ] New shapes follow the project’s shared radius and token system.

## 🎯 UI/UX Priority Checklist

Before delivering UI, check these priorities in order:

| Priority | Category | Must have | Anti-pattern |
|---|---|---|---|
| **P1** | Accessibility | Contrast ≥ 4.5:1, alt text, accessible names | Removing focus rings because they “look bad” |
| **P2** | Touch and interaction | Targets around 44×44px, spacing ≥ 8px, loading feedback | Hover-only interactions that fail on mobile |
| **P3** | Performance | WebP/AVIF where useful, lazy loading, CLS < 0.1 | Layout thrashing and visible loading jumps |
| **P4** | Style tokens | CSS variables, semantic tokens, SVG icons | Raw hex in components or emoji used as icons |
| **P5** | Layout and responsive | Mobile-first breakpoints and no horizontal scroll | Fixed-pixel containers or disabling zoom |
| **P6** | Typography | Base font ≥ 16px and line-height ≥ 1.5 | Text below 12px or gray text on gray background |
| **P7** | Animation | Meaningful 150–300ms transitions and reduced-motion support | Decorative-only motion or no reduced-motion path |
