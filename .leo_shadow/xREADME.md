#--unknown-language--@+leo-ver=4-thin
#--unknown-language--@+node:peckj.20130206111755.1399:@shadow README.md
#--unknown-language--@@nocolor
#--unknown-language--@@language plain
#--unknown-language--@@tabwidth -2
Grinder
=======

A gamification wrapper around Python, inspired by [vigil](https://github.com/munificent/vigil)

Overview
--------
Grinder is a gamified version of Python, in which you have to incrementally unlock the usage of 
various modules.  Grinder does this by checking your code against a recorded statistics file, and
preventing it from running if there are any imports that you have not unlocked.  Unlocking imports
costs Gold, and Gold is earned by running programs successfully - programs which have unhandled
exceptions cost you Gold!

This program/language/toy is an entry in the [February 2013 PLTGames Competition](http://www.pltgames.com/competition/2013/2)

License
-------
WTFPL.

Requirements
------------
  - Python 2.7
  - A command line of some sort
  - A deranged personality that likes grinding

Usage
-----
Running `grinder` without any parameters shows you usage:

    $ ./grinder
    
    Grinder is used as follows
      ./grinder myprogram.py
        -> runs myprogram.py if all the imports are unlocked
      ./grinder stats
        -> prints your Gold and unlocked imports
      ./grinder shop
        -> opens up the shop to spend your Gold on unlocking imports
      ./grinder cheat
        -> allows you to cheat - gives you 1000 Gold
      ./grinder help
        -> prints this help info
      ./grinder about
        -> prints some version and author info

Here's some example output, checking stats:

    $ ./grinder stats
    Your grinder stats:
    Gold: 362
    Unlocked modules:
      os
      sys
      re

Here's a program with a bunch of failing modules:

    $ ./grinder test.py
    Error! Module one not unlocked!
    Error! Module two not unlocked!
    Error! Module three not unlocked!
    Error! Module four not unlocked!
    Error! Module five not unlocked!
    Error! Module six not unlocked!
    Error! Module seven not unlocked!
    Error! Module eight not unlocked!
    Error! Module nine not unlocked!
    Error! Module ten not unlocked!
    Error! Module eleven not unlocked!
    Error! Module twelve not unlocked!
    Error! Module thirteen not unlocked!
    
Here's a user unlocking the modules needed to run a program (yes, I cheated.):

    $ ./grinder test2.py
    Error! Module sys not unlocked!
    
    $ ./grinder shop
    Welcome to the Grinder shop!
    Your grinder stats:
    Gold: 2000
    Unlocked modules:
    Commands that can be entered below:
      b modulename
        -> unlocks modulename -- costs 500 gold
      q
        -> quits shopping
    command?> b sys
    purchase module sys? (y/n)> y
    purchased module sys
    Your grinder stats:
    Gold: 1500
    Unlocked modules:
      sys
    Commands that can be entered below:
      b modulename
        -> unlocks modulename -- costs 500 gold
      q
        -> quits shopping
    command?> q
    Bye!
    
    $ ./grinder test2.py
    cygwin
    
After this, you'll see that you've earned some Gold:
    
    $ ./grinder stats
    Your grinder stats:
    Gold: 1530
    Unlocked modules:
      sys
      
By uncommenting the last line, we see what happens
when a program throws an exception:

    $ ./grinder stats
    Your grinder stats:
    Gold: 1530
    Unlocked modules:
      sys
    
    $ ./grinder test2.py
    cygwin
    Error running program!
    
    list index out of range
    
    $ ./grinder stats
    Your grinder stats:
    Gold: 1461
    Unlocked modules:
      sys
      
You lost Gold!


#--unknown-language--@-node:peckj.20130206111755.1399:@shadow README.md
#--unknown-language--@-leo
