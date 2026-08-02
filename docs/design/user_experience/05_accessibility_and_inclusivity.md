# 05 - Accessibility and Inclusivity

A professional application should work on mobile, with a keyboard, and with assistive technology.

## 1. Touch and Interaction Targets (Priority 2)

- On mobile, interactive elements should be around **44×44px** or larger, with at least **8px** spacing between adjacent targets.
- Do not make an important interaction hover-only; mobile users cannot hover. Provide an explicit control to open and close important menus.

## 2. Contrast and Readability (Priority 1)

- Meet WCAG AA expectations with a minimum contrast ratio of **4.5:1** for normal text.
- Do not place light gray text on a white background. Text on red or blue controls must remain clearly contrasting.

## 3. Screen Readers and Semantics

- Use semantic HTML such as `<nav>`, `<header>`, `<main>`, and `<button>` instead of generic `<div>` elements for everything.
- Meaningful images require `alt` text; decorative images use `alt=""`.
- Icon-only controls such as a close button need an accessible name such as `aria-label="Close"`.

## 4. Keyboard, Focus, and Landmarks

- Every action must be keyboard-operable. Focus must be visible and must not be hidden behind sticky elements or overlays.
- Use meaningful landmarks and a skip link when repeated navigation warrants it.
- A modal moves focus into the dialog, traps focus while open, has a close control, and restores focus to its trigger when closed.

## 5. Forms and Dynamic Status

- Associate labels, help text, and errors with the relevant control. Long forms may also need an error summary.
- Announce meaningful toast, loading, and validation changes through an appropriate status or live region without interrupting users unnecessarily.

## 6. WCAG 2.2 Interactions

- Provide a non-drag alternative for drag interactions and do not force a single input modality.
- Do not ask users to enter the same information unnecessarily and do not rely on inaccessible authentication puzzles.
- Respect `prefers-reduced-motion` and provide a way to stop motion that causes disruption.

References: [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/) and [W3C Dialog Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/).
