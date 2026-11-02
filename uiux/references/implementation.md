# Implement and refactor without changing the product contract

Inspect a neighboring component, its theme, its tests, and the installed framework version. Keep API contracts, server-side authorization, validation ownership, locale, and navigation intact. A disabled button is not authorization. Pick the smallest component boundary that owns the behavior.

## All web stacks

Use a link for navigation, a button for an action, and a form for submission. Persist filters, sort, and pagination in the URL when users need refresh, Back, or shareable views. Do not put sensitive form data there. Prefer intrinsic CSS layout and logical properties over measuring the DOM or hard-coding left/right. Test wrapping, long IDs, translated strings, and zoom. Reserve space for media and delayed content to prevent layout shift.

List only consequential states: loading vs refreshing; empty vs no matches; invalid vs permission denied; pending vs confirmed. Match feedback to the backend outcome. Preserve drafts across recoverable failures and do not change backend contracts as a side effect of UI work.

## React / Next.js only: pick the right Vercel lens

**Composition patterns** address painful APIs, not slow rendering. When several booleans create contradictory states, name the supported variants or compose existing primitives through children/slots. Keep a simple button simple. Lift state only to the closest owner that needs it; do not wrap the app in context for a local interaction.

**React best practices** address concrete costs. Trace the actual wait, payload, or render. Parallelize independent requests, not dependent or authorization-gated ones. Avoid deriving renderable data through mirrored state and effects. Use stable row keys. In Next.js, keep client boundaries near the interaction where supported by the installed router. Split expensive, rarely used UI only when it improves the initial path. For large tables, measure before adding memoization or virtualization; consider server pagination and filtering first.

Use project lint, typecheck, tests, and browser inspection already available. Evidence of a speedup is a comparable trace or measurement, not the presence of `useMemo`. Do not install another tool to satisfy this guide.
