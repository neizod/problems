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
    $ g++ --std=c++1y solution.cpp      # use C++14 standard, not yet accepted by some judges.

Set default compiling option can also be done within `.bashrc` this way:

    $ grep g++ ./bashrc
    alias g++="g++ --std=c++11"
    $ g++ solution.cpp                  # now use C++11 standard by default.
    $ \g++ solution.cpp                 # fall back to C++98 standard.

If not given output filename, a solution file will be named `a.out`, so here is how to invoke it:

    $ ./a.out                           # invoke program


### Haskell

Two options here: for quick test use `runhaskell` to interprete code on the fly, or for timing real usage, compile with `ghc` first then run.

    $ runhaskell solution.hs            # fast: interprete code on the fly.
    $ ghc solution.hs                   # faster: compile first run later.
    $ ghc -O2 solution.hs               # fastest: tell compiler to optimize it.
    $ ./solution                        # invoke program

### Smart Testing

A simple way to test is to type in all this text:

    $ ./solution                        # or ./a.out, or ./solution.py, or blah blah blah
    input line 1
    input line 2
    input line ...
    Ctrl-D                              # require by some problems that need EOF at the end.
    output line 1
    output line 2
    output line ...

To save those typing strokes (and reduce typing errors), a redirection technique can be use here with `<<` symbol, follow by EOF mark, input text, and EOF mark again. e.g.

    $ ./solution << E
    input line 1
    input line 2
    input line ...
    E
    output line 1
    output line 2
    output line ...

Or save the entire input text to a file. This time use just `<` then follow by filename. Be sure to end line in UNIX style (`\n`), not Windows style (`\r\n`).

    $ cat problem.in
    input line 1
    input line 2
    input line ...
    $ ./solution < problem.in    
    output line 1
    output line 2
    output line ...

Finally, this test can be nearly full automation with the use of `diff` program, and `answer.out` output file. i.e.

    $ ./solution < problem.in | diff - answer.out
    $                                   # corrected answer will return prompt w/o complain.


### Clean Up

After testing programs, you might want to run `git clean -df` to delete compiled solution from harddisk to save spaces. This action will also delete other files that is not yet recognize into Git repository, so use with your own risk.


Problems Source
---------------

- ACM-ICPC
- Google Code Jam
- Code Forces
