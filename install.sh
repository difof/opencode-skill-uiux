#!/bin/sh
# Link this checkout without overwriting another skill or editing OpenCode config.
set -eu
usage() { printf '%s\n' 'Usage: ./install.sh --global | --project DIR' >&2; exit 2; }
root=$(CDPATH= cd -P "$(dirname "$0")" && pwd -P)
src=$root/uiux
case ${1-} in
  --global) [ "$#" -eq 1 ] || usage; base=${XDG_CONFIG_HOME:-"$HOME/.config"}/opencode/skills ;;
  --project) [ "$#" -eq 2 ] || usage; project=$(CDPATH= cd -P "$2" && pwd -P) || exit 1; base=$project/.opencode/skills ;;
  *) usage ;;
esac
target=$base/uiux
[ -f "$src/SKILL.md" ] || { printf 'Missing skill: %s\n' "$src/SKILL.md" >&2; exit 1; }
if [ -L "$target" ] && [ -d "$target" ] && [ "$(CDPATH= cd -P "$target" && pwd -P)" = "$src" ]; then
  printf 'Already linked: %s\n' "$target"; exit 0
fi
if [ -L "$target" ] || [ -e "$target" ]; then
  printf 'Refusing to replace: %s\n' "$target" >&2; exit 1
fi
mkdir -p "$base"
ln -s "$src" "$base/"
printf 'Linked: %s -> %s\n' "$target" "$src"
