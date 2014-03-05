snooword
========

Generates a Markdown keyword report from a subreddit.

Installation
------------

For *mad(1)*, an in-terminal Markdown renderer:
* git submodule init
* git submodule update  
  
pip install praw

Usage
-----

At minimum, update SUBREDDIT and KEYWORDS in the script.  
  
./snooword will display the results in the application defined in *$PAGER* . (Usually *less*.)

To-Do
-----
* Include post bodies in search
* Highlight keywords
* Multiple subreddits
* Save report to file
* Sort comments
* OAuth2 (?)

