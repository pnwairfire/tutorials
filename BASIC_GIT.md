# git

This is by no means an exhaustive tutorial on git.  It's just a basic guide to
get aquainted with git.

## Why use git

...

## Creating repo from scratch

Let's create a simple project that contains a python script that
echos what you type.  First create a new directory and initilize
the git repo

    mkdir pyecho
    cd pyecho
    git init

Create the script:

    echo '#!/usr/bin/env python
    import sys

    while True:
        sys.stdout.write("> ")
        line = raw_input()
        sys.stdout.write(line + "\n")
    ' > pyecho.py

    chmod 755 pyecho.py

Add and commit the script to the git repo

    git add pyecho.py
    git commit -m "Initial version of pyecho.py"

Now let's say you change the prompt from '>' to '>>':

    sed -i.bak -e 's/"> "/">> "/' pyecho.py

Now add and commit the change:

    git add -p
    git commit -m "Changed prompt"

Notice that ```git add -p``` ....

Now, try the following:

    git status

You'll see..... You can tell git to ignore.....

    echo "*.bak" > .gitignore

Now, if you do a git status...... Add and commit .gitignore

    git add .gitignore
    git commit -m "Ignore *.bak files"


You'll see that

## Creating a repo out of existing code

Let's say you already have a directory, ```foo```, containing one file,
```bar.py```, which we want to keep in a git repo.  First initialize the repo

    cd /path/to/foo/
    git init

Add...
