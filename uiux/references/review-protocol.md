# Review the interface, not your own preferences

An audit is read-only unless fixes were requested. Identify the artifact (source, screenshot, or live route), target user, task, viewport, and available evidence. Start by trying the main action. A screenshot can demonstrate clipping, but cannot demonstrate broken keyboard handling or prove a particular accessible name.

## Review lenses

1. **Task:** can a user find the next action and know when it succeeds? Check loading, empty, denied, error, and retry behavior where relevant.
2. **Interaction:** check labels, control semantics, keyboard sequence, visible focus, overlays, hover-only actions, and validation. For a specific barrier use the accessibility guide. State an exact WCAG criterion only when applicable.
3. **Visual:** check hierarchy, typography, alignment, information density, responsive layout, and contrast. Explain the consequence: three equally strong actions hide the primary one; a dislike of rounded corners is not a defect.
4. **Implementation:** inspect a cascade, fetch waterfall, rerender, or shared component only when evidence implicates it. Avoid refactoring an unrelated subsystem in a design review.

## Report

Lead with task blockers or consequentially misleading results, then repeated friction, then optional polish. Mark findings **observed**, **needs verification**, or **preference**. For each: location → evidence → user impact → smallest fix → how to retest. Group repeated symptoms with the same cause. When no issue is established, say which path was checked rather than inventing one.

Example: “High · observed · Edit profile / dialog: after Escape, Tab starts at the page header instead of returning to Edit. Keyboard users must traverse the page again. Restore focus to the invoker; retest open → close → Tab.” End with material gaps, e.g. “Only desktop screenshots provided; keyboard and phone behavior not tested.”
