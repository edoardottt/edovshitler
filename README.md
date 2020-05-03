# edovshitler 👾 🎮

edovshitler is a simple game for computers that I enjoyed making it. It's made using Python, especially with pygame library and SQLite3.

[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/c31d18b0dbfb42d992390aa0b987bd6b)](https://www.codacy.com/manual/edoardottt/edovshitler?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=edoardottt/edovshitler&amp;utm_campaign=Badge_Grade)
![win-build-success-badge](https://github.com/edoardottt/twitterBot/blob/master/images/win-build-success-badge.svg)

![edo](https://github.com/edoardottt/edovshitler/blob/master/edo.png)

--------------------------
DESCRIPTION :mega:
--------------------------

**The files in the first level are used to develop the game. In dist,build and pycache folders, there are files built with pyinstaller **

It's important that all the files that are in dist folder stay in dist folder.

It's developed with pygame 1.9.5 library that helps game creating. It's a 2D game, based on Alien (a similar pc game). The game controls are:

- Left arrow key = move to left
      
- Right arrow key = move to right
      
- Space key = shoot the enemies
      
- P key = Pause and resume the game
      
It stores the record (maximum bombs avoided, maximum missiles shooted and maximum enemies killed) in the result.db database (SQLite3). 

It's built with 'pyinstaller --onefile file.py' command.
To create your own executable file with your changes:

For download pyinstaller, execute:

      pip install pyinstaller

And then (inside the edovshitler folder) :

      pyinstaller --onefile game.py

(The .exe is into /dist)

All the files you see in dist folder except the executable file are mandatory (images and script used by .exe file)

It can run on Windows 10 | 8.1 | 8 | 7 | Vista

--------------------------
DOWNLOAD :satellite:
--------------------------

WITH PIP --> pip install edovshitler

GIT command on prompt: git -clone https://github.com/edoardottt/edovshitler.git

Download by Browser on: https://github.com/edoardottt/edovshitler

--------------------------
USAGE :computer:
--------------------------

1) Download the repository

2) Execute the /dist/initdb.py file for initialize the database (or follow the step 4)

3) How to play: 

      3a) run the edovshitler.bat file by clicking two times on it
      
      OR
      
      3b) with a command prompt in edovshitler folder type edovshitler and ENTER
            
      OR
      
      3c) double click on /dist/game.exe file
      
4) If you want to reset the database:

      4a) run the reset.bat file by clicking two times on it
      
      OR
      
      4b) with a command prompt in edovshitler folder type reset and ENTER
      
      OR
      
      4c) double click on /dist/initdb.py file
      
5) Have fun playing it!
:zap::zap::zap:

--------------------------
VERSIONING :books:
--------------------------
[v0.1.2](https://github.com/edoardottt/edovshitler/releases/tag/v0.1.2)

      - Added release on pip

[v0.1.1](https://github.com/edoardottt/edovshitler/releases/tag/v0.1.1)

      - Added a Menu
      - Added a pause/resume game option

[v0.1](https://github.com/edoardottt/edovshitler/releases/tag/v0.1)
      
      - First release

--------------------------
If you liked it drop a :star:
--------------------------

https://www.edoardoottavianelli.it for contact me.

                  Edoardo Ottavianelli ©
