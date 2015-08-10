# git

This is by no means an exhaustive tutorial on git.  It's just a basic guide to
get aquainted with git.

## Why use git

I won't go into why git or other version control systems are good for projects
with multiple developers. Here are some reasons why you'd use it even if working
solo:

 - it makes reverting easy  (```git revert```)
 - you can play around with code, debug, etc. without worrying about remembering how to undo your changes (since you can easily revert, or you can work in another branch)
 - easy to backup and restore code (assuming you push your commits to a remote server, such as on github.com or bitbucket.org)
 - there are built in ways to maintain multiple versions of the code base
 - you can easily see the history of changes, and see the difference between different versions or states of the code
 - helps track down when bugs were introduced and where (see [```git bisect```](https://www.kernel.org/pub/software/scm/git/docs/git-bisect.html) and ```git blame```)
 - easy to share code (even if not collaborating)
 - in case you do end up collaborating on the code, you'll get all the git supports for collaboration
 - you can work on multiple features at without coupling the changes (using branches, or ```git stash``` to quickly make a change while having other changes in progress)

## Creating a repo from scratch

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

Then add and commit the new existing file.

    git add bar.py
    git commit -m "Iniitalizing repo with existing code - bar.py"

## Working with a remote repo

To push your changes to a remote repo, first create a new repo (such as on github,
https://github.com/organizations/YOUR_GITHUB_HANDLE_OR_ORGANIZATION/repositories/new),
and then add the remote to your local repo

    cd /path/to/repo/
    git remote add origin git@github.com:YOUR_GITHUB_HANDLE_OR_ORGANIZATION/REPO_NAME.git

And push your local commits (assuming your in the master branch):

    git push origin master

If you do end up collaborating, you can merge others' commits with ```git pull``, which is
effectively a ```git fetch origin``` followed by a ```git merge mater```. (You can use the
```--rebase``` option to rebase instead of merging othe fetched commits into your local repo.
See [```git rebase```](https://www.kernel.org/pub/software/scm/git/docs/git-rebase.html))