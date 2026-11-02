---
name: uiux
description: Opt-in web interface design, implementation, critique, and accessibility review.
metadata:
  opencode/autoinvoke: false
---

# UI/UX

Work on the user’s named screen, component, or journey. An audit is read-only unless the user asks for fixes. A design brief calls for a design, not scaffolding. A UI bug calls for the smallest useful fix, not a redesign. Do not carry this workflow into an unrelated follow-up.

## Choose one starting point

Identify the user’s goal, the affected route, and the existing component system from the nearest relevant code, theme, or screenshots. **Pick the most specific row below. Read its local guide first.** All paths resolve from the directory containing this file, not the app’s working directory. The source names identify approaches already summarized here, not additional skills to invoke.

| What the user needs | First guide | How to use it |
| --- | --- | --- |
| Fix keyboard access, focus, labels, contrast, reflow, or audit against WCAG | [Accessibility](references/accessibility.md) | Test the user’s actual action; use WCAG for criteria and APG for widget behavior. A dialog focus bug starts here, not in motion. |
| Audit a screen, critique a screenshot, or explain why the UI is hard to use | [Review](references/review-protocol.md) | Vercel web-design-guidelines for observable defects; Impeccable for hierarchy and polish. Separate evidence from taste. |
| Design a dashboard, table, monitoring view, or admin console | [Enterprise data UI](references/enterprise-data-ui.md) | Start with the operator’s decision; choose columns, units, states, and drill-down before decoration. |
| Design a new screen, landing page, or visual identity | [Visual direction](references/visual-direction.md) | Anthropic frontend-design for hierarchy, type, and composition. Reuse existing brand decisions unless redesign is the assignment. |
| Improve onboarding, forms, navigation, labels, or recovery | [Product UX](references/product-ux.md) | Walk one person from entry to success, then through a failure. Use Nielsen’s heuristics to identify the friction. |
| Define tokens, variants, theming, or choose an existing primitive | [Design system](references/design-system.md) | UI UX Pro Max for system decisions; shadcn guidance **only** for an existing shadcn setup. In MUI, extend the existing MUI theme/components. |
| Implement a specified UI, simplify a component API, or fix slow rendering | [Implementation](references/implementation.md) | Vercel composition patterns for component APIs; Vercel React best practices for measured React/Next.js bottlenecks. In other stacks use only the framework-neutral guidance. |
| Polish transitions, feedback, or interrupted interactions | [Interaction and motion](references/interaction-motion.md) | Emil Kowalski for timing and interruption; Impeccable for removing visual noise. Keep reduced-motion behavior intact. |
| Reproduce a regression or verify a completed change | [Verification](references/verification.md) | Exercise the real route and state with available tools. Record what passed and what was not tested. |

**Context budget:** Start with one guide. Open a second only for a concrete unanswered question, e.g. table design → accessibility for a custom grid, or visual design → tokens for a new palette. For a multi-stage request, finish the current stage before opening the next guide. Do not read the whole directory, install upstream skills, or fetch remote rules. [Standards and sources](references/standards-and-sources.md) is for provenance or a specific criterion, not a startup checklist.

## Make and verify the decision

Stay within the requested scope. Functional correctness and accessibility come before aesthetics; existing product patterns come before vendor preferences. Prefer native controls. Preserve the existing locale, direction, tokens, and component library. Never invent permissions, success states, or business rules to make a mockup look finished.

- **Design:** Show the primary task, information order, responsive behavior, and consequential states. For a small fix, skip the design brief.
- **Build or fix:** Implement the smallest complete path, including the failure or recovery state relevant to it. Test the changed behavior, not just compilation.
- **Review:** Lead with the highest-impact finding. Give a route, file/line, or screenshot location; user impact; a fix; and a check. No edits on an audit-only request.
- **Finish:** Distinguish what you observed from what you inferred. No browser means no claim of visual verification. A clean automated scan is not WCAG conformance.
