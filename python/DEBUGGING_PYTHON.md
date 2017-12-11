# Debugging Python

This tutorial focuses on using pdb to debug python.

## Create your buggy script


    echo '#!/usr/bin/env python
    import sys

    def foo():
        a = 1
        b = 2
        c = 1+b
        d = 4-c
        e = 1 - d/0.25
        f = 13.23 / (e + 3)
        g = f / 34
        r = g + 2 + 4 + + 100
        sys.stdout.write("And the answer is {}\n".format(r))

    try:
        foo()
    except:
        sys.stdout.write("*** Uh uh, this script failed, and the reason is hidden by this try/except ***\n")
    ' > ./buggy.py
    chmod a+x ./buggy.py

## Run it and debug with pdb

    ./buggy.py

You'll see that it fails.  To debug, you can use the
[pdb module](https://docs.python.org/2/library/pdb.html). We'll step into the
code right before the call to foo(), lmport pdb and add pdb.set_trace() to to
the line above.

    ....
    try:
        import pdb;
        pdb.set_trace()
        foo()
    ...

Now run it again:

    ./buggy

You'll get the following prompt:

    > /Users/jdubowy/tmp/tutorials/debuggingex/buggy.py(18)<module>()
    -> foo()
    (Pdb)

typing ```h <return>``` will give you

    Documented commands (type help <topic>):
    ========================================
    EOF    bt         cont      enable  jump  pp       run      unt
    a      c          continue  exit    l     q        s        until
    alias  cl         d         h       list  quit     step     up
    args   clear      debug     help    n     r        tbreak   w
    b      commands   disable   ignore  next  restart  u        whatis
    break  condition  down      j       p     return   unalias  where

    Miscellaneous help topics:
    ==========================
    exec  pdb

    Undocumented commands:
    ======================
    retval  rv

We'll use the ```step```/```s```, ```next```/```n```, and ```p```, commands.
Use ```s``` to step into foo.  Then, use ```n``` to step over each of the commands
in foo until you reach the failure.  You should see the following:

    (Pdb) s
    --Call--
    > /Users/jdubowy/tmp/tutorials/debuggingex/buggy.py(4)foo()
    -> def foo():
    (Pdb) n
    > /Users/jdubowy/tmp/tutorials/debuggingex/buggy.py(5)foo()
    -> a = 1
    (Pdb) n
    > /Users/jdubowy/tmp/tutorials/debuggingex/buggy.py(6)foo()
    -> b = 2
    (Pdb) n
    > /Users/jdubowy/tmp/tutorials/debuggingex/buggy.py(7)foo()
    -> c = 1+b
    (Pdb) n
    > /Users/jdubowy/tmp/tutorials/debuggingex/buggy.py(8)foo()
    -> d = 4-c
    (Pdb) n
    > /Users/jdubowy/tmp/tutorials/debuggingex/buggy.py(9)foo()
    -> e = 1 - d/0.25
    (Pdb) n
    > /Users/jdubowy/tmp/tutorials/debuggingex/buggy.py(10)foo()
    -> f = 13.23 / (e + 3)
    (Pdb) n
    ZeroDivisionError: 'float division by zero'
    > /Users/jdubowy/tmp/tutorials/debuggingex/buggy.py(10)foo()
    -> f = 13.23 / (e + 3)
    (Pdb) n
    --Return--
    > /Users/jdubowy/tmp/tutorials/debuggingex/buggy.py(10)foo()->None
    -> f = 13.23 / (e + 3)
    (Pdb) n
    ZeroDivisionError: 'float division by zero'
    > /Users/jdubowy/tmp/tutorials/debuggingex/buggy.py(18)<module>()
    -> foo()
    (Pdb)

The code failed at line 10, ```f = 13.23 / (e + 3)```.  The script is failing
because it's deviding by zero - i.e. ```e + 3``` == 0 and thus e == -3. We've
figured out the problem, but to try variable inspection, Kill the script (ctrl-c)
and repeat the above steps, this time stopping at line 10 to look at e:

    ...
    > /Users/jdubowy/tmp/tutorials/debuggingex/buggy.py(10)foo()
    -> f = 13.23 / (e + 3)
    (Pdb) p e
    -3.0

As we suspected, e == -3.

## Other commands

You can do a lot with just ```s```, ```n```, ```p```.  Other useful commands are
```continue```/```c``` for continuing execution, and ```b``` for setting breakpoints.
