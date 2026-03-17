import os
import subprocess
import yaml
from pathlib import Path
from shutil import rmtree, move
import re

# a single build step, which keeps conf.py and versions.yaml at the main branch
# in general we use environment variables to pass values to conf.py, see below
# and runs the build as we did locally
def build_doc(version, language, tag=None):
	os.environ["current_version"] = version
	os.environ["current_language"] = language
	subprocess.run("git reset --hard", shell=True)
	subprocess.run("git clean -fd", shell=True)
	subprocess.run("git fetch --all --tags", shell=True)
	if tag is None:
		# dev build: stay on main
		subprocess.run("git checkout main", shell=True)
	else:
		subprocess.run("git checkout " + tag, shell=True)
		for filename in ['conf.py', 'versions.yaml', '../.gitignore', 'build_docs.py']:
			subprocess.run(f"git checkout main -- {filename}", shell=True)
	external_link_file = Path("advanced_doc_link.rst")
	if external_link_file.exists() and language == 'en':
		with open(external_link_file, "r", encoding="utf-8") as f:
			content = f.read()
		new_content = re.sub(
			r'(<meta http-equiv="refresh" content="0; url=https://zukunfcs\.github\.io/fcs-doc-advanced/latest/)(jp)(/index\.html"\s*/?>)',
			r'\1en\3',
			content,
			flags=re.IGNORECASE
		)
		if content != new_content:
			with open(external_link_file, "w", encoding="utf-8") as f:
				f.write(new_content)
	os.environ['SPHINXOPTS'] = "-D language='{}'".format(language)
	subprocess.run("make html", shell=True)

	move('_build/html', f'pages/{version}/{language}')


def generate_root_index(latest_version, output_dir):
	"""Generate root index.html with browser language detection."""
	html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <noscript><meta http-equiv="refresh" content="0; url={latest_version}/en/index.html"></noscript>
    <title>Redirecting...</title>
    <script>
        var lang = (navigator.language || navigator.userLanguage || 'en').toLowerCase();
        if (lang.startsWith('ja')) {{
            window.location.replace('{latest_version}/jp/index.html');
        }} else {{
            window.location.replace('{latest_version}/en/index.html');
        }}
    </script>
</head>
<body>
    <p>If you are not redirected automatically, follow this <a href="{latest_version}/en/index.html">link</a>.</p>
</body>
</html>
'''
	Path(output_dir).mkdir(parents=True, exist_ok=True)
	with open(os.path.join(output_dir, 'index.html'), 'w') as f:
		f.write(html)


def generate_legacy_redirect(latest_version, language, output_dir):
	"""Generate legacy redirect from latest/{lang}/ to {latest_version}/{lang}/."""
	html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="refresh" content="0; url=../../{latest_version}/{language}/index.html">
    <title>Redirecting...</title>
</head>
<body>
    <p>If you are not redirected automatically, follow this <a href="../../{latest_version}/{language}/index.html">link</a>.</p>
</body>
</html>
'''
	path = Path(output_dir) / 'latest' / language
	path.mkdir(parents=True, exist_ok=True)
	with open(path / 'index.html', 'w') as f:
		f.write(html)


# to separate a single local build from all builds we have a flag, see conf.py
os.environ["build_all_docs"] = str(True)
os.environ["pages_root"] = "https://zukunfcs.github.io/fcs-doc"

if Path("./pages").exists():
    rmtree(Path("./pages"))
if Path("./_build").exists():
    rmtree(Path("./_build"))

# reading the yaml file
with open("versions.yaml", "r") as yaml_file:
	docs = yaml.safe_load(yaml_file)

# the first entry in versions.yaml is the latest version
latest_version = next(iter(docs))

# build all tagged versions
for version, details in docs.items():
	tag = details.get('tag', version)
	for language in details.get('languages', []):
		subprocess.run("rm -rf locale/en/LC_MESSAGES/*.mo", shell=True)
		subprocess.run("rm -rf locale/jp/LC_MESSAGES/*.mo", shell=True)
		build_doc(version, language, tag)

# build dev from main (no tag checkout)
os.environ["is_dev_build"] = "True"
for language in docs[latest_version].get('languages', []):
	subprocess.run("rm -rf locale/en/LC_MESSAGES/*.mo", shell=True)
	subprocess.run("rm -rf locale/jp/LC_MESSAGES/*.mo", shell=True)
	build_doc("dev", language, tag=None)
os.environ.pop("is_dev_build", None)

# assemble final output
build_dir = Path("./_build")
rmtree(build_dir, ignore_errors=True)
build_dir.mkdir(exist_ok=True, parents=True)
subprocess.run("mv ./pages _build/html", shell=True)
subprocess.run("git checkout main", shell=True)

# generate root index.html with language detection
generate_root_index(latest_version, '_build/html')

# generate legacy redirects for latest/jp/ and latest/en/
for language in docs[latest_version].get('languages', []):
	generate_legacy_redirect(latest_version, language, '_build/html')
