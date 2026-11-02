# Accessibility: test the task, then cite the criterion

Use WCAG 2.2 Level AA (including applicable Level A criteria) as the web accessibility target. The ARIA Authoring Practices Guide (APG) describes interaction patterns; it is not a conformance standard. Start by reproducing the barrier on the affected route.

## Structure and semantics

- Use headings and landmarks that expose the page structure, native links for navigation, buttons for actions, persistent programmatic labels for inputs, and real tables for tabular data. Icon-only controls need an accessible name; decorative glyphs should not be announced twice.
- A role is not an interaction. Before adding ARIA, check whether a native element or existing accessible primitive implements the behavior. Match each custom widget’s role, state, keyboard interaction, and name.
- Announce relevant status changes without stealing focus or announcing every refresh. Associate validation text with the affected field and preserve typed values after failure.

## Keyboard, focus, and overlays

Walk the main task using Tab and Shift+Tab, and each control’s expected activation keys. The focus order should follow the task; a focus indicator must remain visible. At AA, author-created content must not **entirely** cover the focused component (2.4.11); check sticky headers and footers after scrolling.

For a modal, move focus inside on open. Tab should stay inside while modal, Escape should dismiss where appropriate, and focus should return to the trigger or a logical next control if the trigger vanished. Confirm the dialog name and that background content cannot be operated. Avoid custom select/date pickers unless the needed mouse, touch, and keyboard behavior is implemented.

## Perception and input

| Check | What to test |
| --- | --- |
| Contrast | Normal text: at least 4.5:1; qualifying large text: 3:1 (1.4.3, exceptions apply). Required non-text control/state indicators generally need 3:1 against adjacent colors (1.4.11). Measure actual composited colors. |
| Size and reflow | Test 200% text enlargement (1.4.4) and 320 CSS px width equivalent for horizontal writing (1.4.10). A genuinely two-dimensional data table may scroll; the surrounding page need not. |
| Target size | Check 24 × 24 CSS px or an applicable exception, including adequate spacing (2.5.8). A 44 px touch area is a useful larger target, not the AA minimum. |
| Alternate input | For drag operations, provide a single-pointer alternative unless an exception applies (2.5.7). Do not expose essential actions only on hover or signal status only by color. |
| Forms and authentication | Provide clear labels and actionable errors. Check repeated information in one process (3.3.7) and cognitive tests in authentication (3.3.8), including alternatives and exceptions. Support password managers and paste. |
| Motion | Respect reduced-motion settings and preserve the information conveyed. Check whether moving or auto-updating content requires pause, stop, or hide controls. |

Report observed failures, suspected defects, and untested behavior separately. Keyboard and screen-reader results are distinct. A source review, screenshot, or automated scan alone cannot establish full AA conformance.
