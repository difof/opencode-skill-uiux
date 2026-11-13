# Standards and sources

These guides are a local synthesis. No upstream skill, code, dataset, or rules feed is installed or fetched when `@uiux` runs. The links below are for attribution and for checking exact wording, not instructions to load every source.

## Skill influences

| Source | What it contributes here |
| --- | --- |
| [Anthropic · frontend-design](https://github.com/anthropics/skills/tree/main/skills/frontend-design) | Visual direction, typography, and composition grounded in the product. |
| [Vercel · web-design-guidelines](https://github.com/vercel-labs/agent-skills) and [Web Interface Guidelines](https://vercel.com/design/guidelines) | Review interaction, layout, and feedback. No runtime download of upstream rules. |
| [Vercel · React best practices](https://github.com/vercel-labs/agent-skills) | React/Next.js network, render, and bundle performance. |
| [Vercel · composition patterns](https://github.com/vercel-labs/agent-skills) | Boundaries and maintainable component APIs, independent of performance. |
| ChatGPT Work · Sites (installed skill; provenance below) | The [Website design](website-design.md) guide adapts visitor-first narrative, concrete content/assets, bounded website implementation, and evidence-based delivery. |
| [NextLevelBuilder · UI UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | The [Design intelligence](design-intelligence.md) guide adds product/industry reasoning, separate style/motion/density choices, detected-stack and locale constraints, and preservation of an existing design system. No upstream search engine or catalogs are bundled. |
| [Emil Kowalski · design engineering](https://github.com/emilkowalski/skills) | Motion, feedback, and interruptible interactions. |
| [Impeccable](https://github.com/pbakaus/impeccable) | Evidence-led visual critique and refinement. |
| [shadcn/ui · shadcn](https://ui.shadcn.com/docs/skills) | Reuse and compose existing local components; only for projects already using shadcn/ui. |

## Integration provenance and boundaries

- **ChatGPT Sites:** inspected the Sites skill supplied in the ChatGPT session on **1405-08-22 (Asia/Tehran)**, specifically its `SKILL.md` Design section and relevant development/validation workflow, plus `references/design/presentation-led.md`. The website guide is an original portable adaptation of those installed resources, not a claim that they are a public OpenAI repository or that OpenCode has the Work runtime. Sites registration, credentials, hosting APIs/manifests, model selection, private deployment defaults, and framework-specific helpers are deliberately outside this skill. Project instructions and actual authorization govern implementation and publication.
- **UI UX Pro Max:** reviewed official source at [`6ae86f61f520d6ca229d2f40e070410638c908c5`](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/tree/6ae86f61f520d6ca229d2f40e070410638c908c5). Its published skill, shared skill template, reasoning/data structure, and detected-stack workflow informed the expanded guide; the source is MIT-licensed by Next Level Builder. The local guide is a synthesis, not the upstream CLI, BM25 search, design-system generator, full catalog, or premium product. Do not claim to have run those tools or retrieved catalog matches.
- **Integration policy:** load only this skill’s selected local guide. Preserve the existing stack, component library, canonical design documents, locale, and user’s scope. Upstream aesthetic defaults cannot override project evidence or accessibility criteria. No automatic upstream refresh, extra skill installation, or dependency on the separate Figcraft pack is introduced. Maintain these sources only when explicitly asked.

## Standards versus guidance

- **Conformance:** [WCAG 2.2](https://www.w3.org/TR/WCAG22/) defines testable accessibility criteria. At Level AA meet applicable A and AA criteria. [HTML](https://html.spec.whatwg.org/) and [WAI-ARIA](https://www.w3.org/TR/wai-aria-1.2/) specify native semantics and ARIA roles/states, respectively.
- **Implementation guidance:** [ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/) illustrates accessible widget behavior. Its examples are not independently binding WCAG criteria. Prefer native controls where possible.
- **Usability:** [Nielsen Norman Group’s ten heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/) are review lenses, not pass/fail criteria.
- **Design systems:** [Material Design](https://m3.material.io/), [IBM Carbon](https://carbondesignsystem.com/), [MUI](https://mui.com/material-ui/getting-started/), and [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/) are alternatives or stack-specific references, not simultaneous requirements.
- **Packaging:** [OpenCode 2 skills](https://opencode.ai/v2/docs/skills) documents explicit mentions, the model advertisement flag, and skill-relative paths. [Agent Skills specification](https://agentskills.io/specification) describes progressive disclosure.
