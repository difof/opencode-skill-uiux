# opencode-skill-uiux

One opt-in skill for designing, implementing, and reviewing web interfaces in **OpenCode 2**. Mention `@uiux` when you need it. It stays off the model’s advertised skill list otherwise. No MCP, extra agent, package install, or runtime fetch.

```text
@uiux Audit the checkout dialog for keyboard access. Report findings; don’t edit.
@uiux Build a compact incident table using our existing MUI theme. Keep filters on Back.
```

The [skill entry point](uiux/SKILL.md) selects one local guide for the task and reads more only for a concrete unanswered question. Accessibility fixes, product flows, dense data screens, implementation, visual review, and motion retain their focused guides. [Standards and credits](uiux/references/standards-and-sources.md).

- [Website design](uiux/references/website-design.md) adapts ChatGPT Work’s Sites design guidance: complete visitor journeys, purposeful sections, concrete imagery/examples, grounded copy, working interactions, and proportionate delivery checks. It uses the project’s tools and stack; it does not install ChatGPT hosting or model capabilities.
- [Design intelligence](uiux/references/design-intelligence.md) expands UI UX Pro Max into a product-specific decision workflow for patterns, styles, palettes, typography, density, motion, locale, and stack constraints. It preserves established systems and treats catalog preferences as hypotheses, not requirements.

These are local syntheses inside one skill. Upstream installers, search engines, scripts, and datasets are not bundled or fetched during use. The Figcraft pack remains independent: `@uiux` does not load its skill or execute its commands.

## Install

```sh
git clone https://github.com/difof/opencode-skill-uiux.git
cd opencode-skill-uiux
./install.sh --global                 # or: ./install.sh --project /path/to/app
```

The installer symlinks only `uiux/`. It is safe to rerun and refuses to replace another installation. Keep the clone in place; `git pull --ff-only` updates the linked files. To uninstall, remove only the `uiux` symlink from the global or project skills directory.

[OpenCode’s manual-invocation flag](https://opencode.ai/v2/docs/skills) hides this skill from normal discovery; it is not an access-control rule and does not hide separately installed upstream skills.
