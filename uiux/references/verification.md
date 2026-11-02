# Verify with what the project already has

Start with one falsifiable check for the changed behavior. Use the project’s local browser, test harness, fixtures, or available manual route; do not install an MCP, browser framework, or external service. Use safe fixtures for destructive, financial, or permission-changing flows.

| Change | Exercise | Useful evidence |
| --- | --- | --- |
| Dialog | Open by keyboard, Tab/Shift+Tab, Escape, then Tab again. | Focused control before open, inside, and after close. |
| Layout | Narrow and wide viewports, intermediate width where layout breaks, long text and RTL when supported. | Same-state before/after screenshots with actual viewport and observed overflow. |
| Form | Empty, invalid, pending, failed, and successful submit; keyboard path. | Input survives failure; accessible error, recovery and actual result. |
| Results / grid | Sort, filter, no matches, many rows, stale response, select and return. | Actual visible scope, data, selection, and navigation behavior. |
| Motion / theme | Reduced motion, rapid interruptions, all supported themes. | Final state remains legible and operable without motion or color alone. |

For responsive work, roughly 375, 768, and 1440 px are useful starting points, not mandatory breakpoints. Probe just above and below the failure. For accessibility where applicable, test 200% enlargement and 320 CSS px reflow; a phone screenshot alone does not cover both. Check actual contrast pairs and accessible names. A keyboard test is not a substitute for a screen-reader test.

Run relevant existing lint, typecheck, tests, or build. Separate static evidence from rendered, keyboard, and assistive technology checks. Report the route/state, browser/viewport or command, and observed result. If only static checks were possible, mark visual behavior unverified and give the single most useful remaining manual check.
