# 05 - Motion and Animations

## 1. Purposeful Animation

Every animation needs a reason; it must guide attention, explain a state change, preserve context, or make an interaction feel direct.

- A newly created item may slide in to show where it went.
- A removed item may collapse and fade so the user understands what changed.
- Avoid excessive bouncing. Prefer an ease-out rhythm—quick at the start and slower at the end—to suggest natural movement.

## 2. Staggered Entries

When rendering a small list or set of cards, a stagger can reveal items progressively instead of making every element appear at once. A short interval such as 0.05 seconds with slide-up and fade-in can improve perceived performance because the interface starts responding as soon as the first item is available.

Do not stagger long lists or delay content that should be immediately usable.

## 3. Micro-interactions

- When profit/loss values update, a restrained counter transition can make the change readable instead of flashing a new number.
- Opening and closing a modal can use a small scale-in transition so the layer relationship is clear.
- Libraries such as Framer Motion can coordinate these transitions in React, but use an existing project capability before adding a dependency.

## 4. Reduced Motion and Performance

- Respect `prefers-reduced-motion`: reduce or disable nonessential movement and never rely on animation alone to communicate meaning.
- Use stagger only when it guides attention and the item count is small enough; never make a long list feel slower.
- Prefer animating `opacity` and `transform` before properties that trigger layout work.
