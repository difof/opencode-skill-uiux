- Modified reference snapshot from [emilkowalski/skills at f7ce8c02d6e3](https://github.com/emilkowalski/skills/blob/f7ce8c02d6e3c8f0d980a44c57bcc41a40254349/performance-cheatsheet.md); source examples and structure preserved; see the [integration and license rules](catalog.md).
- Reference content is not another installed skill: upstream startup replies, tool permissions, helper commands, agent names, approval ceremonies, and artifact paths do not override the host UIUX skill or the user; no upstream runtime is installed by this pack.

# Performance Cheatsheet

| Problem                             | Solution                                                  |
| ----------------------------------- | --------------------------------------------------------- |
| Animation stutters                  | Animate `transform`/`opacity`, not `width`/`top`          |
| Long list scrolls slowly            | Virtualize — only render what's visible                   |
| Blur causes perf issues             | Keep animated `blur()` under 20px                         |
| Motion's `x`/`y` drops frames       | Upgrade to `motion` 14.2+, or use a `transform` string    |
| Random properties animate           | Don't do `transition: all`, list exact properties         |
| React re-renders every frame        | Write to `ref.current.style`, not state                   |
| Element shifts 1px as motion starts | `will-change: transform` (only once you see it)           |




