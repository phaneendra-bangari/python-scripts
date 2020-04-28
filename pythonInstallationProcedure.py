The standard Linux installation works on any system. However, it requires you to work at the Terminal and type commands to complete it. Some of the actual commands may vary by version of Linux. The information on Python installations provides some helpful tips that you can use in addition to the procedure that follows.

Navigate to the Python download site with your browser.

You see information regarding the latest version of Python.

Click the appropriate link for your version of Linux:

Python 3.3.4 compressed source tarball (any version of Linux)

Python 3.3.4 xzipped source tarball (better compression and faster download)

When asked whether you want to open or save the file, choose Save.

The Python source files begin downloading. Be patient: The source files require a minute or two to download.

Double-click the downloaded file.

The Archive Manager window opens. After the files are extracted, you see the Python 3.3.4 folder in the Archive Manager window.

Double-click the Python 3.3.4 folder.

The Archive Manager extracts the files to the Python 3.3.4 subfolder of your home folder.

Open a copy of Terminal.


The Terminal window appears. If you have never built any software on your system before, you must install the build essentials, SQLite, and bzip2 or the Python installation will fail. Otherwise, you can skip to Step 10 to begin working with Python immediately.

Type sudo apt-get install build-essential and press Enter.

Linux installs the Build Essential support required to build packages.

Type sudo apt-get install libsqlite3-dev and press Enter.

Linux installs the SQLite support required by Python for database manipulation.


Type sudo apt-get install libbz2-dev and press Enter.

Linux installs the bzip2 support required by Python for archive manipulation.

Type CD Python 3.3.4 in the Terminal window and press Enter.

Terminal changes directories to the Python 3.3.4 folder on your system.

Type ./configure and press Enter.

The script begins by checking the system build type and then performs a series of tasks based on the system you’re using. This process can require a minute or two because there is a large list of items to check.

Type make and press Enter.

Linux executes the make script to create the Python application software. The make process can require up to a minute — it depends on the processing speed of your system.

Type sudo make altinstall and press Enter.

The system may ask you for your administrator password. Type your password and press Enter. At this point, a number of tasks take place as the system installs Python on your system.
