Vista Test Framework (VTF)
===================
### Version 1.4.00883

Testing Environment
-------------

#### Configuration
The following files are located at the root level of the test folder.
> 1 - config.ini
>
> - **[DEFAULT]** - set the _base\_dir_ to your test folder's local path.
> - **[LOGGING]** - set the _log\_level_ to the level of logging messages you want to display during test runs; the values may be CRITICAL, ERROR, WARNING, INFO, TRACE, or DEBUG. The DEBUG shows all possible messages, whereas CRITICAL only shows critical type messages.
> - **[USER]** - set the _name_, _username_, and _mail_ to your values

> 2 - book.py
>
> This file does not exist inside the VTF package, so you'll need to create it. Create the file at the root level, name it 'book.py'. Add this line inside the file:
> "password = '{your system password}'"

#### Python Packages

> **python /lib/site-packages**

> - selenium - download the current selenium web driver for Chrome; use the Python version found at http://www.seleniumhq.org/download/ If you have pip and Git Bash installed, then you can simply do ...
>```
pip install -U selenium
```
> - colorama - used by logging; debug adds coloration to different debug levels.
> - names - mandatory package for generating names in several of the test cases.
> - pip - useful to install and update these packages
> - pymssql - mandatory package for access to our MS SQL database

#### 3rd Party Tools

> **Useful tools**

> - Git Bash - handles the git commands for the VTF repository
> - Console 2.00.148 Marko Bozikovic - add the Git Bash and PowerShell shells to this console. Handy if you want all shells in one place.
> **NOTE:** We use PowerShell to manually run the automated tests, for example ...
> ```
> .\vtf.py .\case\regression\edit_directory.py
> ```