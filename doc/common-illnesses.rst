################
Common Illnesses
################

===================
Kernel not starting
===================

1. wrong version
2. wrong installation
3. shadowing built in by naming variable as python module 

==============
Autocompletion
==============

Spyder uses the third party python packages ``rope`` and ``jedi`` to suggest completions, display function signature popups, retrieve help and docstrings, and the like. As these tools aren't perfect, problems can occasionally pop up.
While most such issues lie outside of Spyder's control, either with those packages themselves or the code that is being introspected, here are some commonly reported issues and solutions.

===============
Plugin Problems
===============

If the error mentions or involves a Spyder plug-in, such as
``spyder-autopep8``, ``spyder-terminal``, or ``spyder-notebook``, please check
those repositories to see if an issue was already opened, and report it there
if not. Unfortunately, Spyder has recently lost its funding, so those
projects are on hold for now; see the relevant wiki page
<https://github.com/spyder-ide/spyder/wiki/Anaconda-stopped-funding-Spyder>
for more details, and Open Collective <https://opencollective.com/spyder>
to help support the project and help it continue and improve.
In the meantime, you might need to uninstall the plug-in if you can't avoid it
or fix it on your own, at least for now.