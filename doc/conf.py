import os
import yaml
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'FCS Docs'
copyright = 'TOEI Zukun'
author = 'Zukun'


build_all_docs = os.environ.get("build_all_docs", False)
pages_root = os.environ.get("pages_root", "")
build_pdf = os.environ.get("build_pdf", )
suppress_warnings = ["myst.header"]

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser', 'sphinx_rtd_theme', 'sphinx_design', ]
if build_pdf:
    extensions.append('rst2pdf.pdfbuilder')
    extensions.append('sphinx.ext.autodoc')

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
current_language = os.environ.get("current_language", "jp")
current_version = os.environ.get("current_version", "latest")
version = current_version
release = current_version

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# -- Options for PDF output -------------------------------------------------
latex_engine = 'pdflatex'

latex_documents = [
  ('index', 'fcs_manual.tex', f'FCS Manaul {current_version}', 'TOEI Zukun', f'Manual {current_language}'),
]
# You can also customize LaTeX settings with 'latex_elements'
latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    'papersize': 'a4paper',

    # The font size ('10pt', '11pt' or '12pt').
    'pointsize': '12pt',

    # Additional stuff for the LaTeX preamble.
    'preamble': r'''
\usepackage{graphicx}
\usepackage{float}
\usepackage{sphinx}
\let\Oldincludegraphics\includegraphics
\renewcommand{\includegraphics}[2][]{\begin{figure}[H]\centering\Oldincludegraphics[width=\textwidth,keepaspectratio]{#2}\end{figure}}
\usepackage{luatexja-fontspec}
\setmainjfont{IPAexMincho}
''',    
    'inputenc': '',
    'utf8extra': '',
}

# -- sphinx-intl -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/advanced/intl.html
locale_dirs = ['locale/']
gettext_compact = False

# get the environment variable build_all_docs and pages_root
# if not there, we dont call this


if build_all_docs and build_all_docs == 'True':
    # we set the html_context wit current language and version 
    # and empty languages and versions for now
    html_context = {
        'current_language' : current_language,
        'languages' : [],
        'current_version' : current_version,
        'versions' : [],
    }

    with open("versions.yaml", "r") as yaml_file:
        docs = yaml.safe_load(yaml_file)

    for language in docs[current_version].get('languages', []):
        html_context['languages'].append([language, pages_root+'/'+current_version+'/'+language])        
    # html_context['versions'].append(['latest', pages_root + '/latest/en'])
    for _version, details in docs.items():
        html_context['versions'].append([_version, pages_root+'/'+_version+'/'+current_language])
        