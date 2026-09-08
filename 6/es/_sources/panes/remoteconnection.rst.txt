.. _panes-remote:

#########################
Remote Connection Manager
#########################

The **Remote Connections Manager** allows you to create, initiate and manage connections to external servers as well as local containers and VMs for remote development and execution of your code.
Connecting to a remote host and opening a new :ref:`panes-console` on it allows running code, browsing files and using other Spyder features just as if you were working on your local machine.

It uses the standard, widely-used `SSH protocol`_, which allows you to create a secure connection to remote servers, cloud resources and high-performance computing clusters, as well as local Docker containers, virtual machines (including Windows Subsystem for Linux v2), and headless devices such as the Raspberry Pi.
Additionally, it supports connecting to `JupyterHub`_ servers run by your company, institution or organization and using their shared Jupyter Server environments, without the limitations of the traditional notebook interface.
No configuration is required on the remote host, aside from ensuring an SSH or JupyterHub server is running and accessible.

.. _SSH protocol: https://en.wikipedia.org/wiki/Secure_Shell
.. _JupyterHub: https://jupyter.org/hub

The remote connections manager can be accessed under :menuselection:`Tools --> Manage remote connections`, and you can use :menuselection:`Consoles --> New console in remote server` to open new consoles on remote servers you've already configured.



.. _panes-remote-create:

=========================
Creating a new connection
=========================

To set up a connection to a new remote server, open the remote connections manager and click :guilabel:`New connection`.
You can then configure the settings appropriate to the connection method.

If your institution already has a `JupyterHub`_ server you'd like to connect to, select the :guilabel:`JupyterHub` tab.
Otherwise, if you want to connect to most other types of hosts, you'll want to use the default :guilabel:`SSH`.
Either way, you'll just need to make sure JupyterHub or SSH is available on the remote machine, and you have the appropriate credentials to connect to it.


.. _panes-remote-create-ssh:

SSH connection
~~~~~~~~~~~~~~

To create a new SSH connection, you need to enter several key details:

#. Select your authentication method, :guilabel:`Password` or :guilabel:`Key file`.

   .. note::

      :guilabel:`Password` uses your normal username and password that you would enter when logging in to your account on the machine, while :guilabel:`Key file` uses a SSH private key you've generated with `ssh-keygen`_ and already registered with the remote machine.
      If you're unsure, try :guilabel:`Password` to start, or ask the person who set up the host you are trying to connect to.

#. Type a :guilabel:`Name` for the connection, which is just used to identify it in within the Spyder interface.

#. Enter the IP address or hostname of the device to connect to in :guilabel:`Remote address or host`

#. If you or your administrator has configured different SSH port than the default ``22`` on the remote machine (the port the SSH daemon, ``sshd``, is listening on), enter it in the :guilabel:`Port` field.

#. Type the :guilabel:`Username` of the account you want to connect to.

#. If using a :guilabel:`Password`, enter it in the corresponding field. If using a :guilabel:`Key file`, navigate to where it is located (often under :file:`{YOUR_HOME_DIR}/.ssh/` and called :file:`id_rsa` or similar) and enter its passphrase, if you've set one.

#. Finally, you can optionally set the path to a `SSH configuration file`_, which can contain additional advanced options for the host you set above as well as filling in default values for the previous fields.

.. _ssh-keygen: https://www.ssh.com/academy/ssh/keygen

.. _SSH configuration file: https://www.ssh.com/academy/ssh/config


Finally, click :guilabel:`Connect` to initiate the connection to the host, which will automatically validate and securely save all the provided details and autonomously set up the server Spyder needs to connect to on the remote host, so everything is ready for you to launch your first console.

Alternatively, you can click :guilabel:`Save` to store the details you've entered in a new connection without actually trying to connect.


.. _panes-remote-create-jupyterhub:

JupyterHub connection
~~~~~~~~~~~~~~~~~~~~~

If connecting to a existing JupyterHub server, the process is much simpler than SSH.
Just enter what you would like to :guilabel:`Name` the connection in the Spyder interface, the :guilabel:`Server URL` to the JupyterHub server to connect to, and the access :guilabel:`Token` you were provided.
Then, click :guilabel:`Connect` to connect to the server and save the provided details for future use.
If you have questions about how to obtain a token, ask the person who set up the JupyterHub server or your system administrator.

.. tip::

    To enable all of Spyder's features when working with an existing JupyterHub deployment, ask the person who set up the server to install the `Spyder-Remote-Services`_ Jupyter Server extension.

.. _Spyder-Remote-Services: https://github.com/spyder-ide/spyder-remote-services



.. _panes-remote-manage:

=============================
Manage an existing connection
=============================

You can view the remote connections you've already created by browsing and selecting them from the left panel of the remote connections manager.
The :guilabel:`Connection status` tab shows basic details of the connection, its current state, a log of connection events and any errors to help troubleshoot problems.
Under the :guilabel:`Connection info` tab, you can update any of the details you entered when :ref:`panes-remote-create`, using the :guilabel:`Save` button at the bottom to save your changes.
Use the :guilabel:`Connect` button to initiate the selected connection, or the :guilabel:`Remove` button to delete it.



.. _connecting-external-kernel:
.. _panes-remote-existing:

=========================================
Connecting to existing kernels (advanced)
=========================================

.. caution::

   This is an advanced feature for connecting to existing running kernels, which is substantially more complicated and less capable than creating and managing a connection with Spyder using the Remote Connections Manager.
   If possible, we recommend using the latter instead unless your use case requires it.

You can connect to external local and remote kernels (including those managed by Jupyter Notebook or QtConsole) through the :guilabel:`Connect to an existing kernel` dialog under the :guilabel:`Consoles` menu.
For this feature to work, a compatible version of the ``spyder-kernels`` package :ref:`must be installed <troubleshooting-common-kernel-version>` in the environment or machine in which the external kernel is running.

.. image:: /images/console/console-menu.png
   :alt: Connect to external kernel dialog of the Spyder IPython console


.. _panes-console-external-local:
.. _panes-remote-existing-local:

Connect to a local kernel
~~~~~~~~~~~~~~~~~~~~~~~~~

To connect to a local kernel that is already running (e.g. one started by Jupyter notebook),

#. Run ``%connect_info`` in the notebook or console you want to connect to, and copy the name of its kernel connection file, shown after ``jupyter <app> --existing``.

   .. image:: /images/console/console-connect-local-step1.gif
      :alt: Running connect_info in a Jupyter notebook

#. In Spyder, click :guilabel:`Connect to an existing kernel` from the :guilabel:`Consoles` menu, and paste the name of the :guilabel:`Connection file` from the previous step.

   As a convenience, kernel ID numbers (e.g. ``1234``) entered in the connection file path field will be expanded to the full path of the file, i.e. :file:`{jupyter/runtime/dir/path}/kernal-{id}.json`.

   .. image:: /images/console/console-connect-local-step2.gif
      :alt: Copying the connection filename into Spyder's dialog

#. Click :guilabel:`OK` to connect to the kernel.

   .. image:: /images/console/console-connect-local-step3.gif
      :alt: Connecting to the kernel and running basic commands.


.. _panes-console-external-remote:
.. _panes-remote-existing-remote:

Connect to a remote kernel
~~~~~~~~~~~~~~~~~~~~~~~~~~

To connect to a kernel on a remote machine,

#. Launch a Spyder kernel on the remote host if one is not already running, with ``python -m spyder_kernels.console``.

   .. image:: /images/console/console-connect-remote-step1.gif
      :alt: Staring a Spyder kernel on a remote machine

#. Copy the kernel's connection file (:file:`{jupyter/runtime/dir/path}/kernel-{pid}.json`) to the machine you're running Spyder on.

   You can get :file:`{jupyter/runtime/dir/path}` by executing ``jupyter --runtime-dir`` in the same Python environment as the kernel.
   Usually, the connection file you are looking for will be one of the newest in this directory, corresponding to the time you started the external kernel.

   .. image:: /images/console/console-connect-remote-step2.gif
      :alt: Using SCP to copy the connection file to the local machine

#. Click :guilabel:`Connect to an existing kernel` from the :guilabel:`Consoles` menu, and browse for or enter the path to the connection file from the previous step.

   As a convenience, kernel ID numbers (e.g. ``1234``) entered in the connection file path field will be expanded to :file:`{jupyter/runtime/dir/path}/kernal-{id}.json` on your local machine, if you've copied the connection file there.

   .. image:: /images/console/console-connect-remote-step3.gif
      :alt: Opening the connect to kernel dialog and browsing for the path

#. Check the :guilabel:`This is a remote kernel (via SSH)` box and enter the :guilabel:`Hostname` or IP address, username and port to connect to on the remote machine.
   Then, enter *either* :file:`{username}`'s password on the remote machine, or browse to an SSH keyfile (typically in the :file:`.ssh` directory in your home folder on the local machine, often called :file:`id_rsa` or similar) registered on it; only one is needed to connect.
   If you check :guilabel:`Save connection settings`, these details will be remembered and filled for you automatically next time you open the dialog.

   Note that :guilabel:`Port` is the port number on your remote machine that the SSH daemon (``sshd``) is listening on, typically ``22`` unless you or your administrator has configured it otherwise.

   .. image:: /images/console/console-connect-remote-step4.gif
      :alt: Entering pre-filled SSH details into the connection dialog

#. Click :guilabel:`OK` to connect to the remote kernel

   .. image:: /images/console/console-connect-remote-step5.gif
      :alt: Connecting to the remote kernel and running basic commands

For more technical details about connecting to remote kernels, see the `Connecting to a remote kernel`_ page in the IPython Cookbook.

.. _Connecting to a remote kernel: https://github.com/ipython/ipython/wiki/Cookbook:-Connecting-to-a-remote-kernel-via-ssh



.. _panes-remote-related:

=============
Related panes
=============

* :ref:`panes-console`
* :ref:`panes-editor`
