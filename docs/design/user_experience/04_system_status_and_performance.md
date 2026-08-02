# 04 - System Status and Performance

Users should never feel that the application has frozen or lost their action.

## 1. Visibility of System Status

- When saving, change the button to a progress state and disable it immediately to prevent double submission.
- During page load, use skeleton content shaped like the incoming data instead of an unexplained blank screen.

## 2. Perceived Performance

- A skeleton communicates that work has started and is usually more informative than a spinner left on screen indefinitely.
- **Optimistic UI:** for safe actions such as a like or comment, show the expected result immediately and send the request in the background. If it fails, explain the failure and roll back clearly.

## 3. Layout Stability

- Do not let late-loading images or text push buttons and content around. Reserve dimensions with width/height or `aspect-ratio`.
- Track Cumulative Layout Shift and set a realistic target appropriate to the product; do not use a cosmetic loading trick that hides instability.

## 4. Recovery and Performance Budgets

- Every recoverable failure tells users what happened, what remains safe, and whether they can retry, cancel, edit, or undo.
- Destructive confirmation explains consequences and includes undo when actually possible.
- Set budgets for critical loading and interaction paths; monitor Core Web Vitals, error rate, and failed requests.
