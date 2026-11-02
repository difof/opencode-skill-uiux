# Product UX, navigation, and recovery

Write the journey as **actor → entry → decision → action → confirmation → return**. For each transition, ask what the person knows, what they can undo, and what happens when the operation fails. Focus on the requested path, not every possible persona.

Use real product language: “Save address” says more than “Submit.” Keep labels visible; a placeholder becomes invisible precisely when input needs checking. Explain constraints near the relevant field, associate errors with inputs, and move focus to a helpful error summary or field after a failed submission. Never discard valid input because one field failed.

Use Nielsen’s heuristics to diagnose specific friction:

- **Status and recovery:** distinguish not started, in progress, confirmed, and failed. After a timeout, do not imply no change occurred if the outcome is unknown. A retry can be unsafe for a consequential action.
- **Control and error prevention:** offer Back, Cancel, or Undo where their results are clear. Before irreversible actions show the object, scope, and consequence. Do not interrupt routine reversible actions with confirmations.
- **Recognition and consistency:** put the relevant identifier and selection beside the decision. Preserve filters when returning to results. Reuse the same verb for the same action; do not require remembering an internal ID.
- **Efficiency and comprehension:** keep the frequent path short, group related controls, expose advanced options after essentials, and provide contextual help without hiding required information in tooltips.

Walk the happy path, an invalid submission, a slow or rejected request, and a return visit. Add long content, narrow widths, permissions, or RTL for products that support them. Planning deliverable: show decisions, states, recovery, and unknown business rules. Implementation deliverable: make the path work; do not invent backend capabilities to close a design gap.
