#!/usr/bin/env python3
"""Check the skill package and exercise the installer in a temporary home."""
import os
from pathlib import Path
import re
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'uiux'
ENTRY = SKILL / 'SKILL.md'


class PackageTests(unittest.TestCase):
    def test_only_one_manual_skill(self):
        self.assertEqual(list(ROOT.rglob('SKILL.md')), [ENTRY])
        header, body = ENTRY.read_text().split('\n---\n', 1)
        self.assertTrue(header.startswith('---\nname: uiux\n'))
        self.assertIn('\nmetadata:\n  opencode/autoinvoke: false', header)
        self.assertTrue(body.strip())

    def test_every_guide_is_routed(self):
        routes = set(re.findall(r'\]\((references/[\w-]+\.md)\)', ENTRY.read_text()))
        guides = {p.relative_to(SKILL).as_posix() for p in (SKILL / 'references').glob('*.md')}
        self.assertEqual(routes, guides)
        self.assertEqual(len(guides), 10)
        self.assertTrue(all((SKILL / name).read_text().strip() for name in routes))

    def test_readme_links(self):
        for link in re.findall(r'\]\(([^()]+)\)', (ROOT / 'README.md').read_text()):
            if '://' not in link:
                self.assertTrue((ROOT / link).is_file(), link)

    def test_link_lifecycle(self):
        with tempfile.TemporaryDirectory() as tmp:
            home = Path(tmp)
            config = home / 'with spaces'
            project = home / 'project sample'
            project.mkdir()
            env = dict(os.environ, HOME=tmp, XDG_CONFIG_HOME=str(config))

            def install(*args, success=True):
                proc = subprocess.run([ROOT / 'install.sh', *args], env=env,
                                      capture_output=True, text=True, check=False)
                self.assertEqual(proc.returncode == 0, success, proc.stdout + proc.stderr)

            for args, target in [(['--global'], config / 'opencode/skills/uiux'),
                                 (['--project', str(project)], project / '.opencode/skills/uiux')]:
                install(*args)
                self.assertTrue(target.is_symlink())
                self.assertEqual(target.resolve(), SKILL)
                install(*args)
                target.unlink()
                for kind in ('directory', 'file', 'other link', 'broken link'):
                    if kind == 'directory':
                        target.mkdir()
                    elif kind == 'file':
                        target.write_text('keep me')
                    else:
                        target.symlink_to(project if kind == 'other link' else home / 'absent')
                    install(*args, success=False)
                    if kind == 'directory':
                        self.assertEqual(list(target.iterdir()), [])
                        target.rmdir()
                    else:
                        if kind == 'file':
                            self.assertEqual(target.read_text(), 'keep me')
                        else:
                            self.assertEqual(target.readlink(), project if kind == 'other link' else home / 'absent')
                        target.unlink()
            install('--project', str(home / 'missing'), success=False)


if __name__ == '__main__':
    unittest.main(verbosity=2)
