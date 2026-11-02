# Design systems and tokens

Start in the repository, not with a new palette. Look at an adjacent screen, theme entry, CSS variables, token file, component imports, or `components.json`. Record what already owns type, spacing, surfaces, actions, focus, breakpoints, and density. Never introduce a second system to solve one screen.

## Choose the component path

| Existing system | Use | Avoid |
| --- | --- | --- |
| MUI | The installed theme, variants, slots, and accessible primitives. Check the installed version and existing wrappers. | Introducing shadcn/Tailwind to style a dialog or copying Material 3 specs over product conventions. |
| shadcn/ui | Read `components.json`, the actual local component source, semantic CSS tokens, and an existing usage. Compose the shipped primitives; preserve keyboard and focus behavior when changing triggers. | Assuming an alias, Radix vs Base UI backend, or an upstream demo matches this checkout. Do not run a generator over customized components. |
| Carbon / other design system | Use its existing component names, content rules, and densities. Extend an established variant before inventing one. | Mixing incompatible visual languages or importing a new system for inspiration. |
| No system yet | Define the smallest set needed for the requested flow. Reuse native controls where they suffice. | Choosing a new dependency, font service, or registry without a project reason. |

## A minimal design contract

Name colors by purpose (canvas, surface, text, border, action, focus, error, warning, success). Check the actual foreground/background pairs in each supported theme. Define type roles for body, headings, labels, and numeric data; use tabular numerals where comparisons matter. Pick a spacing scale and a small set of control sizes and radii. Define pressed, focused, busy, disabled, selected, and invalid states where they change the component. Check narrow widths, long text, and RTL when supported.

For example, a destructive button uses the existing danger token and focus ring. A failed save preserves the form and explains recovery; a red background alone does neither. Report which tokens or variants were reused and justify additions by a repeated need. UI UX Pro Max informs this decision process; no palette generator or search dataset is required.
