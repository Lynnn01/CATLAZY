# 04 - Components and States

## 1. Interactive States

Anything the user can activate—buttons, links, and interactive cards—must provide state feedback:

- **Hover:** subtly lighten or darken the surface with a transition such as `transition-colors duration-200` and a token-based hover color.
- **Active/pressed:** make the control feel pressed using a small scale or a stronger surface, for example `active:scale-95`.
- **Disabled:** reduce emphasis (`opacity-50`), expose the unavailable state, and use `cursor-not-allowed` where appropriate.
- **Focus:** show a clear keyboard focus ring; never remove the outline without an equivalent accessible treatment.

## 2. Skeleton, Loading, and Empty States

- Never leave a user staring at a blank screen while data loads.
- **Loading:** use a skeleton whose shapes match the content being loaded, or a small spinner when the layout is already known.
- **Empty state:** explain the absence of data with a quiet icon or illustration and a call to action that helps the user create or discover the first item.
- **Error state:** explain the problem politely and provide a `Retry` action or another safe recovery path.

## 3. High-Fidelity UI Elements

Use premium details with restraint:

- **Subtle borders:** thin, low-opacity borders such as `border border-white/10`.
- **Glow effects:** a primary button may use a restrained glow to attract attention, but only when it does not reduce contrast.
- **Pills/badges:** compact `rounded-full` labels with a quiet background that distinguish status or category.
