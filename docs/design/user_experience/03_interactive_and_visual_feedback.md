# 03 - Interactive and Visual Feedback

A good UI must not be silent when users click or perform an action.

## 1. Interactive States

- **Hover:** change the surface slightly to show that it is interactive.
- **Active/pressed:** make the control feel pressed with a small scale or translation such as `scale-95`.
- **Focus:** keyboard `Tab` navigation must have a visible focus ring such as `ring-2 ring-primary`; never leave `outline: none` without an accessible replacement.
- **Disabled:** visibly communicate that the action is unavailable with reduced emphasis and a disabled cursor where appropriate.

## 2. Validation and Notifications

- **Success:** a short, non-blocking toast can confirm a completed action for roughly 3–5 seconds.
- **Form error:** show an inline error directly below the invalid field as soon as it is known.
- **System error:** use a toast or an in-context error for failures such as an unavailable database, with a recovery action.
- **Destructive actions:** confirm deletion in a dialog when it is not immediately reversible; explain the impact and offer undo when the product truly supports it.

## 3. Micro-interactions

Use short transitions such as `transition-all duration-200` for controls and links where they improve clarity. Hidden content should expand and collapse predictably rather than appearing with no context.
