# Spyder Documentation Style Guide

This style guide is intended as a comprehensive reference on a wide variety of topics that may be pertinent to specific situations encountered when writing the docs.
A more digestible summary of the most important points for doc authors to actively keep in mind is included in the [Contributing Guide](https://github.com/spyder-ide/spyder-docs/blob/master/CONTRIBUTING.md).
Readers should be familiar with the basics of reST syntax, as covered in a resource like the [Sphinx reStructuredText Primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html).


<!-- markdownlint-disable -->
<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [General](#general)
- [Structure](#structure)
- [Technical](#technical)
- [reST Style Elements](#rest-style-elements)
- [Images/Figures](#imagesfigures)
- [Writing (All Languages)](#writing-all-languages)
- [Writing (English)](#writing-english)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->
<!-- markdownlint-restore -->


## General

Must (not), should (not), recommended, suggested, may, and can generally follow IETF conventions, with some additional differentiation:

* **Must** (not) clauses are hard requirements that must always be observed
* **Should** (not) clauses can only be disregarded in a particular instance with strong justification, or if it is demonstratively highly impractical to follow for a specific case
* (Not) **Recommended** and **Preferred** clauses should be followed where practicable; a brief rationale should be provided for not doing so
* **Suggested** clauses indicate a convention, approach or guideline that may be helpful to follow, but has no binding effect or justification requirements
* **May** or **Can** clauses designate explicitly permitted guidelines, actions or conventions, often for clarity, that are allowed but have no weight of preference on them (and may even be gently discouraged with a suggested or preferred alternative)


## Structure

* In general, follow the [OpenStack Heading Guidelines](https://docs.openstack.org/doc-contrib-guide/writing-style/general-writing-guidelines.html) with regard to sections and headings; in particular, section and subsection titles delineating overall categories of tasks/topics and be in gerund (i.e. with "ing", e.g. "Editing code", "Debugging files"), while those concerning a concept or reference topic should be a noun (e.g. "General considerations", "Requirements") and lowest level topic/task titles should generally be in imperative ("Create a code cell", "Get help", etc) where reasonable
* Headings will appear in the sidebar, so use as few words as practicable
* Heading case: Page titles (L1 headings) should use Title Case, all others should use Sentence case
* One L1 Heading, used for page titles: Use ``######`` with overline; on first line of file; keep to a few words
* L2 Headings for section heads: Use ========= with overline; 3 blank lines before them
* L3 headings for subheads: Use ~~~~~~; 2 blank lines
* L4 Headings for sub-subheads if truly necessary: Use ---------; 1 blank line; keep to a minimum (consider a flatter structure or breaking into multiple files)
* Related panes at the bottom: L2 heading; bullets; try for 2-4 links if included
* All files with ``Related panes`` should contain at least one L2 section; if only one, can be entitled Overview
* Typically, for files with multiple sections or longer than one page, a summary section of a few lines length is helpful before the first section, summarizing the functionality discussed in the section and its purpose
* Name of component/topic should be in first sentence, Title Case, bold on first use


## Technical

* Markdown, Github-flavored (``.md``) for any non-documentation rendered text files in the root of the repo, e.g. ``README``, ``CONTRIBUTING``, etc.
* reStructuredText, (reST, ``.rst``) for documentation format, i.e. any user-visible files in the ``/doc`` directory
* Where not otherwise contradicted by this guide or specific individual requirements, a subset of Markdown corresponding to that cross-compatible with reST should be preferred where possible; e.g. ``*italic*`` vs. ``_italic_``, ``*`` for bulleted lists, double backtick for inline code vs. single, etc.
* Documentation should build with no warnings with ``Sphinx`` in nitpicky mode
* Lower case filenames, rst extension, hyphens as space deliminators, short but descriptive
* End files with a newline (blank line)
* 1 blank line after all headings and before and after paragraphs, directives and ``|``s
* Use Line Feed (LF, ``\n``) as the End of Line character on all platforms
* Use UTF-8 for all files (with no BOM, as dictated by the UTF-8 standard); do not use Windows Notepad as this adds a BOM and can otherwise corrupt files easily
* Use standard UTF-8 characters instead of escape sequences for non-ASCII values (e.g. em dash, en dash, etc)
* Suggested to avoid non-ASCII characters where minimal downside/need exists, or an existing proper name or other identifier uses them
* Spaces, no tabs for indentation (or otherwise)
* Natural indents (3 spaces) for directives, 4 spaces for further indents beyond that in code
* No hard wrap, put each sentence on its own line, and try to keep them under 180 characters
* Wrap code blocks at a width of 70 characters from the page margin for readability.
* Place section links above the section with one blank line between them and the section, and two blank lines between sections (as appropriate for that section level) between the link and the preceding text.
* Always use single backticks around link titles
* Eliminate any trailing whitespace before committing
* Try to keep individual files to under around ~500 lines; split into separate topics beyond that



## reST Style Elements

* Filenames/paths: Use :file: and ``/`` for delimiters e.g. :file:`path/to/test.py`. Example filenames should be all lowercase with no spaces or special characters unless called for by the application; real filenames should follow their actual case. Use {descriptive-name} for placeholders.
* Keyboard Shortcuts: Use :kbd: to format, Ctrl/Alt/Shift as abbreviations (instead of Command/Option), ``-`` with no spaces to separate, and title case (including capital letters for letter keys; always include Shift explicitly if needed) e.g. :kbd:`Ctrl-Alt-Shift-P`. Use the key name or symbol as printed on a standard keyboard. For any configurable shortcut, you should include "by default" to indicate this, and must include at least one other means the command can be accessed if available (e.g. via a menu or toolbar), which should be done for all shortcuts and should include all means of executing the command, if multiple others exist.
* GUI elements (names of things in the UI): Use ``:guilabel:`` , e.g. ``:guilabel:`Name` ``; make sure to use the exact name and capitalization as printed in the UI, except for the proper names of Spyder panes (i.e. those listed in the ``View > Panes`` menu), which should always be written in Title Case ("Variable Explorer", "Code Analysis", "IPython Console", etc. as they are proper names). Also, for consistency and clarity, they should be referred to as panes, rather than modules, plugins, panels, etc.
* Menu items and preference panes: Use :menuselection: to format and ``-->`` to separate, e.g. `` :menuselection:`Project --> New Project` ``. Make sure to use the exact name and capitalization of each level element
* Short commands/lines of code (under 20-30 characters), use `` , e.g. ``code``
* For any code longer than one line, ~20-30 characters, or that is otherwise important to emphasize rather than just mention, use ``code-block::`` tags, closed with ``end``, and specify the programming language (bash for command line, python for python, ini for configuration files, etc.). PEP 8 should be followed for Python code, with all "recommended"/"preferred"/"suggested" guidelines being treated as *should* i.e. only broken with appropriate justification in a situation requiring them; similarly, PEP 257 for docstrings where needed. Additionally, all code must be valid and idiomatic Python 3 unless specifically meant to illustrate a distinction with Python 2, and code should for the time being fall under the common subset supported by Spyder's supported platforms (currently, Python 3.6-3.8). Wrap code blocks at a width of 70 characters from the page margin for readability.
* Internal links to sections should never rely on implicit references, since they may change with section titles or other re-organization. Instead, always use explicit references above the target with one blank line between; keep ref names short, use ``-`` to replace spaces, use unique and distinctive names and append ``-ref`` to the end of the name for clarity.
* All external links should be inline (not bare) unless specifically needed to illustrate some property of the link itself, should be HTTPS if available, and should, generally, be written as a reference with `` `Test Link Name`_`` and then included in full after the end of the paragraph in which it appears, e.g. `` .._Test Link Name: https://www.example.com/ `` . A block of links should be separated from paragraphs above and below by one blank line, with no blank lines between links. Make sure to check your links, as the build will automatically check for broken ones. Strip anything unnecessary (parameters, referrers, etc) off the end. As the base docs are in US English, any links should be to the English, desktop version of the site.
* Use enumerated lists with ``#.`` to list items with a clearly defined order, otherwise, use bulleted lists with ``*``. Include a space between the bullet/number and the text. No blank line between elements, unless a sublist is present, but blank lines around the list. Sublist should have no spaces around elements. You should try to avoid more than two levels of lists if at all possible, and keep lists to between 3 and 10-20 elements; anything shorter should be written in prose, and anything longer should be simplified or broken into multiple lists/sublists.
* Use ``note::`` for general callouts, ``warning::`` to warn users against procedures with potential serious consequences, and ``important::`` for key points that users don't want to miss. However, use these sparingly, only when clearly called for. Always make them separate blocks, with a blank line between the start of the block, like:

```rst
.. Note::

   This is a note.

```


## Images/Figures

* Lower case file names and extensions, separate with hyphens, 3-character extensions
* For ease of visibility, images should be either full width, or 500 px if appropriate
* Use PNG for all images, except photographs over 100-200 KB as a PNG (use moderately compressed JPEG); avoid sizes above 2000 x 2000 or below 1000 x 1000 if full width, or half of each if half width
* GIFs should be compressed to 5 frames/s, should target a length of around 5-10 seconds, and should be either 690 px or 500 px, depending on the subject
* Always include alt text describing the content of the image


## Writing (All Languages)

* Follow the [OpenStack General Writing Guidelines](https://docs.openstack.org/doc-contrib-guide/writing-style/general-writing-guidelines.html)
* Maintain an explanatory rather than expository tone if appropriate for the language (i.e. in English, "How" rather than "What"; e.g. "Spyder can do XXX." -> "To do XXX, you can...")
* Focus on the user; this is documentation, not promotional material
* Try to use simple language if possible and avoid buzzwords, jargon and acronyms
* Make sure capitalization, spacing etc. of proper names and acronyms are correct and consistent per the original (or the canonical localized form if available)
* In text, use the full name for file types ("TIFF" and "JPEG", not "TIF" and "JPG"), and always use ``/`` as the path delimiter
* Must use ISO 8601 (YYYY-MM-DD HH:MM:SS, 24-hour format, with leading zeros) for all numeric dates and times. No convention is imposed for textual forms (e.g. January 1, 2018; 1 de abril de 2019; etc) so long as all three components are provided, the month names are written out in full, and the year is written as 4 digits.
* ``.`` must be used as the decimal separator in languages that at least partially use it (i.e. a native speaker would not be unfamiliar with its use), and suggested otherwise at the option of the translator to be consistent with its use in Python and  internet standards, and avoid the textual ambiguity of `,`; regardless of which is chosen, it is more important to use it consistently throughout the docs of a given language
* If a separator is used between groups of digits for readability, it must be the space to avoid ambiguity per ISO standard conventions
* Should use only SI/metric for units


## Writing (English)

* Standard written English; US spellings are nominally the default for consistency but not required, and any given page should keep to only one convention. Avoid dialect-specific words.
* AP style unless noted elsewhere here
* Avoid idioms, contractions and other constructs that might be unclear to non-native speakers
* Make sure capitalization, spacing etc. of proper names and acronyms are correct and consistent
* Must use ``.``, the period/point/full stop, as the decimal separator (e.g. pi is 3.14), to be consistent with its use in Python, internet standards and the language the English docs are written in
