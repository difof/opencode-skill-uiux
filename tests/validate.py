#!/usr/bin/env python3
"""Check the skill package and exercise the installer in a temporary home."""
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
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
        self.assertTrue(all((SKILL / name).read_text().strip() for name in routes))

    def test_readme_links(self):
        for link in re.findall(r'\]\(([^()]+)\)', (ROOT / 'README.md').read_text()):
            if '://' not in link:
                self.assertTrue((ROOT / link).is_file(), link)


    def test_policy_format_and_local_links(self):
        policies = [ROOT / 'README.md', ROOT / 'AGENTS.md', ENTRY,
                    *(SKILL / 'references').glob('*.md')]
        for path in policies:
            text = path.read_text()
            body = text.split('\n---\n', 1)[1] if path == ENTRY else text
            for number, line in enumerate(body.splitlines(), 1):
                if line.strip():
                    self.assertTrue(line.startswith('- '), f'{path.name}:{number}')
            for link in re.findall(r'\]\(([^()]+)\)', text):
                if '://' in link or link.startswith(('#', 'mailto:')):
                    continue
                target = link.split('#', 1)[0]
                if target:
                    self.assertTrue((path.parent / target).exists(),
                                    f'{path.name}: {link}')

    def test_pinned_source_integrity_and_scope(self):
        manifest = json.loads((SKILL / 'upstream/sources.json').read_text())
        self.assertEqual(manifest['schema_version'], 1)
        ids = [source['id'] for source in manifest['sources']]
        self.assertEqual(len(ids), len(set(ids)))
        registered = {}
        for source in manifest['sources']:
            if source['kind'] != 'licensed-upstream-snapshot':
                self.assertTrue((ROOT / source['coverage_file']).is_file())
                self.assertTrue((ROOT / source['guide']).is_file())
                continue
            self.assertRegex(source['revision'], r'^[0-9a-f]{40}$')
            self.assertTrue(source['repository'].startswith('https://github.com/'))
            self.assertTrue(source['license'])
            source_paths = [record['source_path'] for record in source['files']]
            self.assertEqual(len(source_paths), len(set(source_paths)))
            scoped = source['scope_inventory']
            scope_paths = [record['source_path'] for record in scoped]
            self.assertEqual(len(scope_paths), len(set(scope_paths)))
            included = {record['source_path'] for record in scoped
                        if record['status'] == 'included'}
            self.assertEqual(set(source_paths), included, source['id'])
            for record in scoped:
                self.assertIn(record['status'], ('included', 'excluded'))
                if record['status'] == 'excluded':
                    self.assertTrue(record.get('reason'), record['source_path'])
            for record in source['files']:
                self.assertRegex(record['source_sha256'], r'^[0-9a-f]{64}$')
                if record['source_sha256'] != record['sha256']:
                    self.assertTrue(record['transformations'], record['path'])
                self.assertNotIn(record['path'], registered)
                registered[record['path']] = record['sha256']
        for record in [*manifest['supplemental_attributions'],
                       *manifest['supporting_files']]:
            self.assertNotIn(record['path'], registered)
            registered[record['path']] = record['sha256']
        for name, expected in registered.items():
            path = ROOT / name
            self.assertTrue(path.resolve().is_relative_to(ROOT.resolve()), name)
            self.assertTrue(path.is_file(), name)
            self.assertRegex(expected, r'^[0-9a-f]{64}$')
            self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(),
                             expected, name)
        actual = {path.relative_to(ROOT).as_posix()
                  for path in (SKILL / 'upstream').rglob('*')
                  if path.is_file() and path.name != 'sources.json'}
        self.assertEqual(actual, set(registered))
        self.assertEqual(set(manifest['active_guides']),
                         {path.relative_to(ROOT).as_posix()
                          for path in (SKILL / 'references').glob('*.md')})
        self.assertFalse(list((SKILL / 'upstream').rglob('AGENTS.md')))
        self.assertFalse(list(SKILL.rglob('__pycache__')))
        self.assertFalse(list(SKILL.rglob('*.pyc')))

    def test_wcag_criterion_coverage(self):
        index = json.loads((SKILL / 'upstream/w3c/criteria-index.json').read_text())
        expected = {row['id'] for row in index['criteria']}
        self.assertEqual(index['count'], 55)
        self.assertEqual(len(index['criteria']), 55)
        self.assertEqual(len(expected), 55)
        self.assertNotIn('4.1.1', expected)
        self.assertIn('4.1.2', expected)
        self.assertTrue(all(row['level'] in ('A', 'AA') for row in index['criteria']))
        guide = (SKILL / 'references/accessibility-criteria.md').read_text()
        actual = re.findall(r'^- \*\*(\d+\.\d+\.\d+) \((?:A|AA)\)\*\*', guide, re.M)
        self.assertEqual(len(actual), len(expected))
        self.assertEqual(set(actual), expected)
        for row in index['criteria']:
            self.assertIn(index['source'] + '#' + row['slug'], guide)

    def test_offline_catalog_queries_are_read_only(self):
        def tree():
            return {path.relative_to(SKILL).as_posix():
                    hashlib.sha256(path.read_bytes()).hexdigest()
                    for path in SKILL.rglob('*') if path.is_file()}

        before = tree()
        search = SKILL / 'upstream/pro-max/scripts/search.py'
        with tempfile.TemporaryDirectory() as tmp:
            env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
            def query(*args):
                result = subprocess.run([sys.executable, '-B', str(search), *args],
                                        cwd=tmp, env=env, capture_output=True,
                                        text=True, timeout=30, check=False)
                self.assertEqual(result.returncode, 0, result.stderr)
                return json.loads(result.stdout)
            result = query('keyboard focus modal', '--domain', 'ux', '--json')
            self.assertEqual(result['domain'], 'ux')
            self.assertGreater(result['count'], 0)
            self.assertTrue(result['results'])
            result = query('internal analytics dashboard', '--design-system',
                           '--json', '--variance', '8', '--motion', '2',
                           '--density', '8')
            self.assertIsNone(result['persistence'])
            proposal = result['design_system']
            self.assertTrue(proposal['style'])
            self.assertTrue(proposal['colors'])
            self.assertEqual(proposal['dials']['density'], 8)
            self.assertEqual(list(Path(tmp).iterdir()), [])
        self.assertEqual(before, tree(), 'Catalog query mutated the installed skill')

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
