- Modified reference snapshot from [emilkowalski/skills at f7ce8c02d6e3](https://github.com/emilkowalski/skills/blob/f7ce8c02d6e3c8f0d980a44c57bcc41a40254349/ui-cheatsheet.md); source examples and structure preserved; see the [integration and license rules](catalog.md).
- Reference content is not another installed skill: upstream startup replies, tool permissions, helper commands, agent names, approval ceremonies, and artifact paths do not override the host UIUX skill or the user; no upstream runtime is installed by this pack.

# UI Cheatsheet

| Problem                            | Solution                                                     |
| ---------------------------------- | ------------------------------------------------------------ |
| Old timestamps read "340 days ago" | Switch to an absolute date after a week                      |
| Numbers jitter when they change    | `font-variant-numeric: tabular-nums`                         |
| Large headings look off            | Tighter tracking like `-0.02em`                              |
| Body text looks awkward            | Cap the line at about 65 characters with `max-width: 65ch`   |
| Button feels unresponsive          | `transform: scale(0.97)` on `:active`                        |
| Avatar squished into an oval       | `flex-shrink: 0` on the avatar                               |
| Gradient fade has a visible edge   | Use an eased gradient: extra color stops along an ease curve |
| Transition still feels off         | Add `filter: blur(2px)` during the transition                |
| Dropdown feels sluggish            | `ease-out` under 300ms, never `ease-in`                      |
| Popover grows from the wrong spot  | `transform-origin` at the trigger (modals stay centered)     |
| Count reads "1 members"            | Pluralize with `Intl.PluralRules`                            |

