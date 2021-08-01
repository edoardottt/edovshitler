# edovshitler 👾 🎮

<p align="center">
  <img src="https://github.com/edoardottt/edovshitler/blob/master/edo.png">
  <br>
  <img src="https://img.shields.io/badge/python-3.6-blue.svg"/>
  <a href="https://www.codacy.com/manual/edoardottt/edovshitler?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=edoardottt/edovshitler&amp;utm_campaign=Badge_Grade"><img src="https://api.codacy.com/project/badge/Grade/c31d18b0dbfb42d992390aa0b987bd6b"/></a>
  <img src="https://github.com/edoardottt/images/blob/main/scilla/win10.svg"/>
</p>

It works nicely on Windows, maybe Linux testing...  
edovshitler is a simple game I enjoyed making it. It's made using Python with pygame library and SQLite3.

Get Started :mega:
---------

 **Build it with pyinstaller**

To create your own executable file with your changes:

- Download pyinstaller: `pip install pyinstaller`

- then execute(inside the edovshitler folder): `pyinstaller --onefile game.py`

(The .exe is inside /dist folder)

All the files you see in dist folder except the executable file are mandatory (images and script used by .exe file)

It can run on Windows 10 | 8.1 | 8 | 7 | Vista


Description :mega:
---------

It's developed with pygame 1.9.5 library that helps game creating. It's a 2D game, based on Alien (a similar pc game). The game controls are:

- Left arrow key = move to left
      
- Right arrow key = move to right
      
- Space key = shoot the enemies
      
- P key = Pause and resume the game
      
It stores the record (maximum bombs avoided, maximum missiles shooted and maximum enemies killed) in the result.db database (SQLite3). 


Download :satellite:
----------

- `git clone https://github.com/edoardottt/edovshitler.git`

Usage :computer:
---------

1. Download the repository

2. Execute the /dist/initdb.py file for initialize the database (or follow the step 4)

3. How to play: 

      3a. run the edovshitler.bat file by clicking two times on it
      
      OR
      
      3b. with a command prompt in edovshitler folder type edovshitler and ENTER
            
      OR
      
      3c. double click on /dist/game.exe file
      
4. If you want to reset the database:

      4a. run the reset.bat file by clicking two times on it
      
      OR
      
      4b. with a command prompt in edovshitler folder type reset and ENTER
      
      OR
      
      4c. double click on /dist/initdb.py file
      
5. Have fun playing it!
:zap::zap::zap:


Versioning :books:
---------

[v0.1.2](https://github.com/edoardottt/edovshitler/releases/tag/v0.1.2)

- Add release on pip

[v0.1.1](https://github.com/edoardottt/edovshitler/releases/tag/v0.1.1)

- Add a Menu
- Add a pause/resume game option

[v0.1](https://github.com/edoardottt/edovshitler/releases/tag/v0.1)
      
- First release


License 📝
-------

This repository is under [MIT License](https://github.com/edoardottt/edovshitler/blob/master/LICENSE).  
[edoardoottavianelli.it](https://www.edoardoottavianelli.it) to contact me.
