# 02 - Information Architecture and Navigation

A good system prevents users from getting lost and does not dump every detail on them at once.

## 1. Progressive Disclosure

- Do not put everything on one page. Put advanced settings and deep detail behind tabs, accordions, or a clear “Show more” control.
- At each step, show the information needed for the current decision and keep secondary complexity available on demand.

## 2. Clear Navigation

- **You are here:** the current destination must be obvious. Highlight the active navigation item differently from inactive items.
- **Breadcrumbs:** when the hierarchy is deeper than two levels, provide breadcrumbs such as Home > Settings > Account so users can understand their location and go back easily.

## 3. Empty States

When a list is empty or a search returns no results, never show an unexplained white screen:

- **Visual:** use a quiet, meaningful icon or illustration.
- **Explanation:** state briefly why the area is empty, such as “There are no documents in this folder yet.”
- **Call to action:** offer the best first action, such as `+ Create a new document`.

## 4. Search and Filters

- Large collections need fast search, normally with debounce and clear empty/error feedback.
- Filters should be easy to find, expose active criteria, and update results immediately when that is safe and understandable.
