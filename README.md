Problems Solving
================

    /!\ Caution:
        Reading through this solutions might be spoiling yourself.

This repository contains my (public) problem-solving solutions.


Compile, Run, and Test
----------------------

If any, input from `stdin` will be provide with `input.in` file. Look out for some problems that I might not provide `input.in` myself -- such as in Code Jam directory. You can find the input from their site.


### Python

All solutions in Python is written for version 3 of the language (i.e. use `python3` to run), somes might compatible with `python2` or `pypy`. I've already dump a shebang header that point to `python3` in most (but not all) of the solutions, but testing with other version still possible by specify name of interpreter from command line. e.g.

    $ head solution.py
    #!/usr/bin/env python3
    ...
    $ ./solution.py                     # invoke program with python3 as an interpreter.
    $ python3 solution.py               # same as above.
    $ pypy solution.py                  # invoke program with pypy as an interpreter.

Also if some solutions is written in 1-linear style, file extension will be ended with `.1l.py`, hope you like it :D

    $ ./solution.1l.py                  # sould be same as ./solution.py


### C++

Compile with C++11 standard, or above. e.g.

    $ g++ --std=c++11 solution.cpp      # use C++11 standard.
    $ g++ --std=c++0x solution.cpp      # same(?) as above.
    $ g++ --std=c++1y solution.cpp      # use C++14 standard, this might not yet wildly acceptable by some judges.

Set default compiling option can also be done within `.bashrc` this way:

    $ grep g++ ./bashrc
    alias g++="g++ --std=c++11"
    $ g++ solution.cpp                  # now use C++11 standard without need of specify it over and over.
    $ \g++ solution.cpp                 # fall back to C++98 standard.

If not given output filename, a solution file will be named `a.out`, so here is how to invoke it:

    $ ./a.out                           # invoke program


### Haskell

Two options here: for quick test use `runhaskell` to interprete code on the fly, or for timing real usage, compile with `ghc` first then run.

    $ runhaskell solution.hs            # fast: interprete code on the fly.
    $ ghc solution.hs                   # faster: compile first run later.
    $ ghc -O2 solution.hs               # fastest: tell compiler to optimize it.
    $ ./solution                        # invoke program


After testing programs, you might want to run `git clean -df` to delete compiled solution from harddisk to save spaces.


Problems Source
---------------

- ACM-ICPC
- Google Code Jam
- Code Forces
