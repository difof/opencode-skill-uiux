# Interaction feedback and motion

Start with the behavior, not an easing curve. What should the user understand: that an action registered, that content moved, that work is pending, or that it failed? If a state change communicates that clearly, it does not need animation.

## Choose feedback by outcome

| Event | Response |
| --- | --- |
| Immediate local action | Update the control or content directly. Avoid multiple success announcements for one action. |
| Slow save or async job | Show pending without promising success. Guard against accidental repeats; maintain a recovery path and expose the real result. |
| Failed request | Preserve input, scope, scroll, and selection where possible. Explain what failed and what to do next. |
| Reversible change | Offer Undo only where it genuinely restores state. Confirm irreversible actions in proportion to their impact. |

For movement, choose the shortest transition that explains the change and feels responsive in the product. Opening, closing, and quickly reopening a panel should work mid-animation. Respect `prefers-reduced-motion: reduce`; remove nonessential movement while preserving focus and final state. Avoid `transition: all`, layout thrashing, animated page-load cascades, and spinners on every click. Prefer transform/opacity where appropriate and let existing primitives own timing and focus.

Test rapid clicks, a second action before the first completes, touch without hover, keyboard activation, reduced motion, and a failed response. For overlays, verify focus on entry and return; a fade cannot fix broken focus. Impeccable-style polish often means removing duplicate feedback or noise rather than adding an effect.
