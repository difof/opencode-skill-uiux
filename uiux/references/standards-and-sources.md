# Standards and sources

These guides are a local synthesis. No upstream skill, code, dataset, or rules feed is installed or fetched when `@uiux` runs. The links below are for attribution and for checking exact wording, not instructions to load every source.

## Eight skill influences

| Source | What it contributes here |
| --- | --- |
| [Anthropic · frontend-design](https://github.com/anthropics/skills/tree/main/skills/frontend-design) | Visual direction, typography, and composition grounded in the product. |
| [Vercel · web-design-guidelines](https://github.com/vercel-labs/agent-skills) and [Web Interface Guidelines](https://vercel.com/design/guidelines) | Review interaction, layout, and feedback. No runtime download of upstream rules. |
| [Vercel · React best practices](https://github.com/vercel-labs/agent-skills) | React/Next.js network, render, and bundle performance. |
| [Vercel · composition patterns](https://github.com/vercel-labs/agent-skills) | Boundaries and maintainable component APIs, independent of performance. |
| [NextLevelBuilder · UI UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | Product-specific design-system decisions, without the upstream search scripts or catalogs. |
| [Emil Kowalski · design engineering](https://github.com/emilkowalski/skills) | Motion, feedback, and interruptible interactions. |
| [Impeccable](https://github.com/pbakaus/impeccable) | Evidence-led visual critique and refinement. |
| [shadcn/ui · shadcn](https://ui.shadcn.com/docs/skills) | Reuse and compose existing local components; only for projects already using shadcn/ui. |

## Standards versus guidance

- **Conformance:** [WCAG 2.2](https://www.w3.org/TR/WCAG22/) defines testable accessibility criteria. At Level AA meet applicable A and AA criteria. [HTML](https://html.spec.whatwg.org/) and [WAI-ARIA](https://www.w3.org/TR/wai-aria-1.2/) specify native semantics and ARIA roles/states, respectively.
- **Implementation guidance:** [ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/) illustrates accessible widget behavior. Its examples are not independently binding WCAG criteria. Prefer native controls where possible.
- **Usability:** [Nielsen Norman Group’s ten heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/) are review lenses, not pass/fail criteria.
- **Design systems:** [Material Design](https://m3.material.io/), [IBM Carbon](https://carbondesignsystem.com/), [MUI](https://mui.com/material-ui/getting-started/), and [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/) are alternatives or stack-specific references, not simultaneous requirements.
- **Packaging:** [OpenCode 2 skills](https://opencode.ai/v2/docs/skills) documents explicit mentions, the model advertisement flag, and skill-relative paths. [Agent Skills specification](https://agentskills.io/specification) describes progressive disclosure.
