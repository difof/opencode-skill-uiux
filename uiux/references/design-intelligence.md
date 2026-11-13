# Product-led design intelligence

Use this guide when an open design choice needs a coherent product-level direction: layout pattern, visual character, palette, typography, density, or interaction treatment. For an existing component defect, start with the specific outcome instead of rethinking the whole system.

This is a local synthesis of UI UX Pro Max's decision process. Its searchable catalogs, Python tools, generated recommendations, and persistence commands are not bundled. Do not claim a database match or generated design-system result.

## Ground the choice

1. Identify the audience, primary task, content, usage frequency, platform, and consequence of an error. Name what the person must recognize or decide before choosing a style. An industry label is useful context, not evidence that every product in that industry should look alike.
2. Inspect the current repository's component library, theme, fonts, breakpoints, locale, and stack. Detect the actual framework from dependencies and existing usage; never silently assume React, Tailwind, shadcn, or a native platform. Preserve established choices unless the task includes changing them.
3. Choose one dominant question. For a new product direction, consider pattern, visual character, role colors, type, layout, and states together. For a focused problem, name the observable outcome first—such as readable badge text, an unobscured focus target, or a useful validation error—then consult implementation details for the detected stack.
4. Compare proposed choices with real or representative content and the nearest existing screen. Prefer one justified direction; offer alternatives only where the brief leaves a consequential decision open. A familiar pattern that supports the task is better than a fashionable style name.
5. State the smallest useful design contract: primary action and information order; shared components; semantic colors and type roles; spacing/density; responsive behavior; and consequential states. Keep assumptions visible. Reuse the project's existing design source when documentation is requested; do not automatically create a second master/override directory.

## Make the decisions together

| Decision | Evidence to use | What to preserve or avoid |
| --- | --- | --- |
| Page and interaction pattern | Visitor intent, task sequence, repeated actions, comparison needs, and content volume. | A presentation site needs a meaningful progression and next action; an operational interface needs scanning, state, and recovery. Do not apply a marketing layout to a work queue. |
| Visual character | Existing identity, subject, audience expectations, and the role of imagery or demonstrations. | Use a small coherent set of motifs. Do not combine unrelated styles, add decoration to imply functionality, or let a catalog label override the product. |
| Palette and themes | Real foreground/background combinations, semantic state roles, content emphasis, and supported themes. | Reuse tokens and measure actual combinations. Dark mode, trust-blue, health-green, and industry-associated palettes are choices, not requirements. A bright alert must still have text or another meaningful cue. |
| Typography | Reading versus scanning, script coverage, long labels, numeric comparison, and available licensed fonts. | Give headings, body, labels, metadata, and numbers deliberate roles. Verify actual font loading and fallback; a named pairing does not prove Arabic/Persian coverage or visual fidelity. |
| Density and layout | Task frequency, viewport, input method, content length, and comfortable action targets. | Adjust gaps, grouping, and disclosure before shrinking text or targets. Keep real layout constraints and intentional component exceptions; do not paste a spacing scale onto an established system. |
| Motion and feedback | What changed, whether an action was accepted, continuity between states, interruption, and user preferences. | Choose timing by the effect and context. Feedback must remain timely; reduced motion may switch directly to the final state. Do not add animation libraries or elaborate scrolling because an upstream preset exists. |
| Icons, imagery, and data | Meaning, consistent geometry, source credibility, comparison task, units, and the state being communicated. | Reuse an icon family, label controls, and distinguish decorative from meaningful assets. Pick chart forms from the data question; axes, units, accessible alternatives, and actual freshness matter more than visual novelty. |

## Tune independently

- **Visual variation:** choose restraint or a distinctive composition to suit the brief. More asymmetry is not inherently better; preserve familiar navigation and stable control positions where people work repeatedly.
- **Motion:** select the minimum movement that explains a transition or supplies useful feedback. Keep it interruptible and respect reduced motion. High visual variation does not imply high motion.
- **Density:** use whitespace for comprehension and compact grouping for repeated comparison. A dense dashboard still needs legible type, clear grouping, keyboard access, and adequate targets; a spacious page still needs substance.

Treat these as independent design decisions, not scores that prove quality or preset bundles to apply mechanically.

## Check context before applying a recommendation

- Prioritize blocked actions, accessibility, input reliability, recovery, and performance over ornamental polish. The task can change the order: data comprehension is central to a monitoring screen, even if a generic checklist ranks charts late.
- For RTL or mixed-direction content, use logical alignment and spacing where appropriate, then inspect actual text, truncation, navigation icons, carousels, charts, and motion paths. Do not mirror numbers, logos, media controls, or every icon indiscriminately.
- Apply platform-specific guidance only to that platform. CSS pixels, iOS points, and Android density-independent pixels are not interchangeable. Web accessibility criteria and their exceptions belong in the accessibility guide; native-app safe-area and gesture conventions are not a universal desktop-web checklist.
- Preserve global design decisions while allowing explicit page/state exceptions. Read the existing rule before replacing it; never force a regenerated palette or page override over deliberate project work.
- Treat upstream catalogs as inspiration and recommendations. Do not turn an industry profile into invented features, compulsory themes, business rules, compliance claims, or user research. If no project evidence supports a recommendation, label it as a proposal and explain its tradeoff.

Validate the chosen direction against a narrow viewport, realistic long content, an important non-happy state, and the real rendering when available. Open [Design system](design-system.md), [Accessibility](accessibility.md), [Enterprise data UI](enterprise-data-ui.md), or [Interaction and motion](interaction-motion.md) only for the specific unresolved question; do not load them all. See [Standards and sources](standards-and-sources.md) for provenance.
