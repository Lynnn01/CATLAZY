# 07 - Quality Validation

Validate a critical flow before release with the smallest useful evidence.

## 1. Accessibility check

- Complete the flow by keyboard only, including opening and closing dialogs.
- Check focus order, visible/unobscured focus, labels, error messages, and status announcements.
- Test with a screen reader when introducing a custom widget, dialog, menu, live region, or complex form.

## 2. Usability check

- Give a representative user one task with a clear success condition.
- Record whether they complete it, where they hesitate, and whether recovery after an error is understandable.
- Fix the highest-impact failure before polishing visual details.

## 3. Product signals

- For a critical flow, choose one outcome metric (completion rate, error rate, or time to complete).
- Monitor performance and failures without collecting unnecessary personal data.
- Revisit the flow after meaningful changes, support complaints, or a metric regression.

## References

- [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/)
- [WAI-ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/)
