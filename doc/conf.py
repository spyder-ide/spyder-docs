# -*- coding: utf-8 -*-
#
# Spyder documentation build configuration file, created by
# sphinx-quickstart on Fri Jul 10 16:32:25 2009.
#
# This file is execfile()d with the current directory set to its parent dir.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/stable/config
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# Standard library imports
import os
import sys
import importlib

# Third party imports
from qtpy.QtCore import Qt, QCoreApplication
from qtpy.QtWidgets import QApplication
from qtpy import QtWebEngineWidgets

# Constants
HERE = os.path.abspath(os.path.dirname(__file__))
REPO = os.path.dirname(HERE)
SPYDER = os.path.join(REPO, "spyder-repo")
if not os.path.isdir(SPYDER):
    raise Exception(
        'To build docs you need to clone the Spyder repo inside "{}"'.format(SPYDER)
    )

sys.path.insert(0, SPYDER)
os.environ['RUNNING_SPHINX'] = 'true'

# Conf handling
with open("modules.rst", "r") as fh:
    lines = fh.read().split("\n")

if ":orphan:" not in lines[0]:
    lines.insert(0, ":orphan:")
    lines.insert(1, "")

    with open("modules.rst", "w") as fh:
        fh.write("\n".join(lines))


# PyQt handling
QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
app = QApplication([])

# Mocks and ignores
autodoc_mock_imports = [
    "PyQt5.QtWebEngineWidgets.QWebEnginePage",
    "PyQt5.QtWebEngineWidgets.QWebEngineView",
] 
nitpick_ignore = [
    ("py:class", "DirCreatedEvent"),
    ("py:class", "DirDeletedEvent"),
    ("py:class", "DirModifiedEvent"),
    ("py:class", "DirMovedEvent"),
    ("py:class", "FileCreatedEvent"),
    ("py:class", "FileDeletedEvent"),
    ("py:class", "FileModifiedEvent"),
    ("py:class", "FileMovedEvent"),
    ("py:class", "IPython.core.history.HistoryManager"),
    ("py:class", "PyQt5.QtCore.QAbstractItemModel"),
    ("py:class", "PyQt5.QtCore.QAbstractTableModel"),
    ("py:class", "PyQt5.QtCore.QObject"),
    ("py:class", "PyQt5.QtCore.QSortFilterProxyModel"),
    ("py:class", "PyQt5.QtCore.QThread"),
    ("py:class", "PyQt5.QtGui.QStandardItem"),
    ("py:class", "PyQt5.QtGui.QSyntaxHighlighter"),
    ("py:class", "PyQt5.QtGui.QTextBlockUserData"),
    ("py:class", "PyQt5.QtPrintSupport.QPrinter"),
    ("py:class", "PyQt5.QtWebEngineWidgets.QWebEnginePage"),
    ("py:class", "PyQt5.QtWebEngineWidgets.QWebEngineView"),
    ("py:class", "PyQt5.QtWidgets.ExtraSelection"),
    ("py:class", "PyQt5.QtWidgets.QAction"),
    ("py:class", "PyQt5.QtWidgets.QApplication"),
    ("py:class", "PyQt5.QtWidgets.QComboBox"),
    ("py:class", "PyQt5.QtWidgets.QDialog"),
    ("py:class", "PyQt5.QtWidgets.QDockWidget"),
    ("py:class", "PyQt5.QtWidgets.QFileIconProvider"),
    ("py:class", "PyQt5.QtWidgets.QFrame"),
    ("py:class", "PyQt5.QtWidgets.QHBoxLayout"),
    ("py:class", "PyQt5.QtWidgets.QHeaderView"),
    ("py:class", "PyQt5.QtWidgets.QItemDelegate"),
    ("py:class", "PyQt5.QtWidgets.QKeySequenceEdit"),
    ("py:class", "PyQt5.QtWidgets.QLabel"),
    ("py:class", "PyQt5.QtWidgets.QLineEdit"),
    ("py:class", "PyQt5.QtWidgets.QListWidget"),
    ("py:class", "PyQt5.QtWidgets.QMainWindow"),
    ("py:class", "PyQt5.QtWidgets.QMenu"),
    ("py:class", "PyQt5.QtWidgets.QMessageBox"),
    ("py:class", "PyQt5.QtWidgets.QPlainTextEdit"),
    ("py:class", "PyQt5.QtWidgets.QProxyStyle"),
    ("py:class", "PyQt5.QtWidgets.QPushButton"),
    ("py:class", "PyQt5.QtWidgets.QScrollArea"),
    ("py:class", "PyQt5.QtWidgets.QSplitter"),
    ("py:class", "PyQt5.QtWidgets.QStyledItemDelegate"),
    ("py:class", "PyQt5.QtWidgets.QTabBar"),
    ("py:class", "PyQt5.QtWidgets.QTabWidget"),
    ("py:class", "PyQt5.QtWidgets.QTableView"),
    ("py:class", "PyQt5.QtWidgets.QTableWidget"),
    ("py:class", "PyQt5.QtWidgets.QTextEdit"),
    ("py:class", "PyQt5.QtWidgets.QToolBar"),
    ("py:class", "PyQt5.QtWidgets.QToolButton"),
    ("py:class", "PyQt5.QtWidgets.QTreeView"),
    ("py:class", "PyQt5.QtWidgets.QTreeWidget"),
    ("py:class", "PyQt5.QtWidgets.QTreeWidgetItem"),
    ("py:class", "PyQt5.QtWidgets.QWidget"),
    ("py:class", "QAction"),
    ("py:class", "QColor"),
    ("py:class", "QFileInfo"),
    ("py:class", "QFont"),
    ("py:class", "QIcon"),
    ("py:class", "QIndex"),
    ("py:class", "QLayout"),
    ("py:class", "QMainWidget"),
    ("py:class", "QMenu"),
    ("py:class", "QModelIndex"),
    ("py:class", "QObject"),
    ("py:class", "QShortcut"),
    ("py:class", "QSize"),
    ("py:class", "QTextBlock"),
    ("py:class", "QTextCursor"),
    ("py:class", "QToolBar"),
    ("py:class", "QWebEngineView"),
    ("py:class", "QWidget"),
    ("py:class", "Qt.ItemFlags"),
    ("py:class", "QtGui.QBrush"),
    ("py:class", "QtGui.QColor"),
    ("py:class", "QtGui.QTextCursor"),
    ("py:class", "SRE_Pattern"),
    ("py:class", "callable"),
    ("py:class", "code.InteractiveConsole"),
    ("py:class", "collections.abc.MutableSequence"),
    ("py:class", "configparser.ConfigParser"),
    ("py:class", "iter"),
    ("py:class", "iterable"),
    ("py:class", "jupyter_client.kernelspec.KernelSpec"),
    ("py:class", "number"),
    ("py:class", "objbrowser.treeitem.TreeItem"),
    ("py:class", "object"),
    ("py:class", "optional"),
    ("py:class", "pydoc.Doc"),
    ("py:class", "pygments.lexer.RegexLexer"),
    ("py:class", "qtconsole.manager.QtKernelManager"),
    ("py:class", "qtconsole.rich_jupyter_widget.RichJupyterWidget"),
    ("py:class", "qtpy.QtWidgets.QComboBox"),
    ("py:class", "qtpy.QtCore.QUrl"),
    ("py:class", "sequence"),
    ("py:class", "spyder.plugins.completion.kite.KiteEndpoints"),
    ("py:class", "spyder_kernels.comms.commbase.CommBase"),
    ("py:class", "string"),
    ("py:class", "threading.Thread"),
    ("py:class", "watchdog.events.FileSystemEventHandler"),
    ("py:class", "watchdog.utils.BaseThread"),
]

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.githubpages",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# The encoding of source files.
source_encoding = "utf-8"

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "Spyder"
copyright = " 2018 Spyder Doc Contributors <a href='https://opensource.org/licenses/MIT' target='_blank'>MIT License</a>"
author = "The Spyder Doc Contributors"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = "3"
# The full version, including alpha/beta/rc tags.
release = "3"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of documents that shouldn't be included in the build.
# unused_docs = []

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "*tests*",
]

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = []

# The reST default role (used for this markup: `text`) to use for all docs.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "alabaster"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    "body_text_align": "left",
    "github_banner": False,
    "travis_button": False,
    "codecov_button": False,
    "extra_nav_links": {
        "Troubleshooting": (
            "https://github.com/spyder-ide/spyder/wiki/"
            + "Troubleshooting-Guide-and-FAQ"
        ),
        "Spyder Wiki": "https://github.com/spyder-ide/spyder/wiki",
    },
    "sidebar_collapse": True,
    "show_related": True,
    "page_width": "1000px",
    "sidebar_width": "250px",
    "fixed_sidebar": False,
    "gray_1": "#303030",
    "gray_2": "#EBEBEB",
    "gray_3": "#EE1C24",
    "font_family": "Raleway, 'Open Sans', Arial, sans-serif",
    "head_font_family": "Raleway, 'Open Sans', Arial, sans-serif",
    "font_size": "16px",
    "link": "#EE1C24",
    "link_hover": "#EE1C24",
}

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = 'spyder_bbg.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "_static/favicon.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
html_sidebars = {
    "**": [
        "about.html",
        "navigation.html",
        #'relations.html',
        "searchbox.html",
        "donate.html",
    ]
}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_use_modindex = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = ''


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "Spyderdoc"


# -- Options for LaTeX output ------------------------------------------------

# The paper size ('letter' or 'a4').
# latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
# latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    ("index", "Spyder.tex", "Spyder Documentation", author, "manual"),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# Additional stuff for the LaTeX preamble.
# latex_preamble = ''

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_use_modindex = True


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "Spyder",
        "Spyder Documentation",
        author,
        "Spyder",
        "The Scientific Python Development Environment.",
        "Miscellaneous",
    ),
]

# If true, show URL addresses after external links.
# man_show_urls = False


# -- Extension configuration -------------------------------------------------

# Napoleon settings
napoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
