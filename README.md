# opencode-skill-uiux

One opt-in skill for designing, implementing, and reviewing web interfaces in **OpenCode 2**. Mention `@uiux` when you need it. It stays off the model’s advertised skill list otherwise. No MCP, extra agent, package install, or runtime fetch.

```text
@uiux Audit the checkout dialog for keyboard access. Report findings; don’t edit.
@uiux Build a compact incident table using our existing MUI theme. Keep filters on Back.
```

The [skill entry point](uiux/SKILL.md) picks one local guide by task: accessibility for a focus bug, product UX for a broken flow, visual direction for a new landing page, or implementation for a slow React component. More guides are read only when needed. Guidance from eight upstream skills is synthesized locally; their scripts and datasets are not bundled. [Standards and credits](uiux/references/standards-and-sources.md).

## Install

```sh
git clone https://github.com/difof/opencode-skill-uiux.git
cd opencode-skill-uiux
./install.sh --global                 # or: ./install.sh --project /path/to/app
```

The installer symlinks only `uiux/`. It is safe to rerun and refuses to replace another installation. Keep the clone in place; `git pull --ff-only` updates the linked files. To uninstall, remove only the `uiux` symlink from the global or project skills directory.

[OpenCode’s manual-invocation flag](https://opencode.ai/v2/docs/skills) hides this skill from normal discovery; it is not an access-control rule and does not hide separately installed upstream skills.
