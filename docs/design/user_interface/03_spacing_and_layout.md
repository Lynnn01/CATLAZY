# 03 - Spacing and Layout (Grid and Bento)

## 1. Grid-Based Spacing

- Base all padding, margin, and gap values on a 4px or 8px system. In Tailwind, use a consistent scale such as `1, 2, 4, 8, 16, 24`.
- Avoid arbitrary values such as 13px or 17px; a shared rhythm makes every screen feel intentional.
- **Maximum width:** prevent reading content from stretching across the full screen. Use a responsive constraint such as `max-w-7xl mx-auto` where appropriate.

## 2. Bento Grid Pattern

- A **bento box** arrangement can group cards of different sizes and work well with modern or glass-like surfaces.
- Each card needs a clear radius and consistent spacing such as `gap-4` or `gap-6`.
- Use the pattern when it clarifies relationships; do not force every page into a grid simply to make it look novel. Ensure cards reflow naturally on mobile.

## 3. Visual-Impact Layout

- **Hero section:** the top of a page should communicate its purpose clearly, use a strong heading, and provide a visible primary call to action when one exists.
- Preserve generous **negative space**. “Less is more”: do not fill every area with information.
- Keep related information together using the proximity principle, and use larger whitespace to separate unrelated groups.
