# git

This is by no means an exhaustive tutorial on git.  It's just a basic guide to
get acquainted with git.  Also, it's a work in progress...

## Why use git

I won't go into why git or other version control systems are good for projects
with multiple developers. Here are some reasons why you'd use it even if working
solo:

 - You don't lose anything (well, at least not anything that was every committed).  You can recover anything that's in the repo history. If you get in the habit of commiting frequently, you'll likely stop commenting out code code; you just delete it.
 - Reverting is easy. (See [```git revert```](https://www.kernel.org/pub/software/scm/git/docs/git-revert.html)). You can play around with code, debug, etc. without worrying about remembering how to undo your changes. You can always get back to a previous state.
 - You can use git to backup and restore code (assuming you push your commits to a remote server, such as on github.com or bitbucket.org)
 - You can use branches to maintain multiple versions of the code base, or parallel lines of development.  (See [```git branch```](https://www.kernel.org/pub/software/scm/git/docs/git-branch.html).  See also [```git stash```](https://www.kernel.org/pub/software/scm/git/docs/git-stash.html), which is useful for quickly making a change when you have other changes in progress.)
 - You can easily see the history of changes, and see the difference between different versions or states of the code.  If you've been away from the code for some time, you can easily see what you most recently did. (See [```git log```](https://www.kernel.org/pub/software/scm/git/docs/git-log.html))
 - Git helps with tracking down when and where bugs were introduced. (see [```git bisect```](https://www.kernel.org/pub/software/scm/git/docs/git-bisect.html) and [```git blame```](https://www.kernel.org/pub/software/scm/git/docs/git-blame.html))
 - You can easily work on the same code base on multiple computers (e.g. on your home and work computers).  Git handles merging the work you do on your various computers.
 - Git facilitates sharing code (even if not collaborating).
 - In case you do end up collaborating on the code, you'll get all that git supports for collaboration.

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

Run it:

    $ ./pyecho.py
    > foo
    foo
    > bar
    bar
    >

Kill it (ctrl-c) and then add and commit the script to the git repo

    git add pyecho.py
    git commit -m "Initial version of pyecho.py"

Now let's say you change the prompt from '>' to '>>':

    sed -i.bak -e 's/"> "/">> "/' pyecho.py

Run it to see the change

    $ ./pyecho.py
    >> foo
    foo
    >> bar
    bar
    >>

Kill it (ctrl-c) and add the change:

    git add -p

Notice the use of ```-p``` in ```git add -p```.  This lets you cherry pick 'hunks'
of code changes to include in your commit.  In the current case, there's only one
'hunk'.  You'll see:

    $ git add -p
    diff --git a/pyecho.py b/pyecho.py
    index 6cc3ace..1f0707b 100755
    --- a/pyecho.py
    +++ b/pyecho.py
    @@ -2,7 +2,7 @@
     import sys

     while True:
    -    sys.stdout.write("> ")
    +    sys.stdout.write(">> ")
         line = raw_input()
         sys.stdout.write(line + "\n")

    Stage this hunk [y,n,q,a,d,/,e,?]? y

In cases where you have lots of pending code changes, ```-p``` lets commit
subsets of hunks that logically go together.

Commit the change

    git commit -m "Changed prompt"

Now, try the following:

    git status

You'll see:

    $ git status
    On branch master
    Untracked files:
      (use "git add <file>..." to include in what will be committed)

            pyecho.py.bak

    nothing added to commit but untracked files present (use "git add" to track)

The ```pyecho.py.bak``` is an artifact of using sed.  Since you don't want to commit
it to the repo, you can tell git to ignore it.

    echo "*.bak" > .gitignore

Now, if you do a git status, you'll no longer see ```pyecho.py.bak```, though you'll see
the new .gitignore:

    $ git status
    On branch master
    Untracked files:
      (use "git add <file>..." to include in what will be committed)

            .gitignore

    nothing added to commit but untracked files present (use "git add" to track)

Add and commit .gitignore:

    git add .gitignore
    git commit -m "Ignore *.bak files"

git status will now tell you that you have no more pending changes or untracked files,
even though ```pyecho.py.bak``` still exists

    $ git status
    On branch master
    nothing to commit, working directory clean

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

If you do end up collaborating, you can merge others' commits with ```git pull```, which is
effectively a ```git fetch origin``` followed by a ```git merge master```. (You can use the
```--rebase``` option to rebase instead of merging othe fetched commits into your local repo.
See [```git rebase```](https://www.kernel.org/pub/software/scm/git/docs/git-rebase.html))

## More advanced usage

### Revert

If you want to undo your last commit:

    git revert
    git commit

Git will create a message for you, which you can override or modify if you wish.
Git will open up the message in your default text editor.  (You can [configure
git to use an alternative editor](https://duckduckgo.com/?q=git+configure+editor).)

If you want to revert a commit that's not necessarily your last one:

    git revert COMMITGUID
    git commit

### Branches

To create a new branch:

    git checkout -b my-new-branch

This will create a branch off of your current branch (which often is
```master```).  Once in this branch, commit and merge as you normally would.
Let's say you're working with a remote repo, and other develpoers are commiting
changes to master. When you want to fetch and merge the commits from master, use
the following:

    git fetch
    git merge master

When you're ready to merge your branch back into master, checkout master
and merge your branch

    git checkout master
    git merge my-new-branch

When you're done with your branch, delete it:

    git branch -d my-new-branch

List the branches to confirm that it was deleted:

    $ git br -a
    * master

## Conveniences

### Git Config

To configure git, create a file ```.gitconfig``` in your home directory.  Here's an example:

    [user]
        name = Joe Doe
        email = joedoe@gmail.com
    [core]
        excludesfile = $HOME/.gitignore
        editor = emacs
    [color]
        diff = auto
        status = auto
        branch = auto
    [github]
        user = mygithubhandle
    [remote.origin]
        push = HEAD
    [branch]
      autosetupmerge = true
    [alias]
      st = status
      br = branch
      co = checkout
      df = diff
      lg = log -p
      ls = log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit --date=relative
      lnm = log HEAD ^master

### Git Command Tab Completion

...TODO: fill in this section....

### Bash Prompt Customization

You can customize your bash prompt to include information about the git repo you're in.
For example (from https://gist.github.com/802970):

    #############################
    # git prompt
    # https://gist.github.com/802970
    #############################
            RED="\[\033[0;31m\]"
         YELLOW="\[\033[0;33m\]"
          GREEN="\[\033[0;32m\]"
           BLUE="\[\033[0;34m\]"
      LIGHT_RED="\[\033[1;31m\]"
    LIGHT_GREEN="\[\033[1;32m\]"
          WHITE="\[\033[1;37m\]"
     LIGHT_GRAY="\[\033[0;37m\]"
     COLOR_NONE="\[\e[0m\]"

    function parse_git_branch {

      git rev-parse --git-dir &> /dev/null
      git_status="$(git status 2> /dev/null)"
      branch_pattern="On branch ([^${IFS}]*)"
      no_branch_pattern="Not currently on any branch"
      remote_pattern="Your branch is (.*) of"
      diverge_pattern="Your branch and (.*) have diverged"
      if [[ ! ${git_status}} =~ "working directory clean" ]]; then
        state="${RED}!"
      fi
      # add an else if or two here if you want to get more specific
      if [[ ${git_status} =~ ${remote_pattern} ]]; then
        if [[ ${BASH_REMATCH[1]} == "ahead" ]]; then
          remote="${YELLOW}^"
        else
          remote="${YELLOW}v"
        fi
      fi
      if [[ ${git_status} =~ ${diverge_pattern} ]]; then
        remote="${YELLOW}b"
      fi
      if [[ ${git_status} =~ ${branch_pattern} ]]; then
        branch=${BASH_REMATCH[1]}
        echo " (${branch})${remote}${state}"
      elif [[ ${git_status} =~ ${no_branch_pattern} ]]; then
        echo " (no branch)"
      fi
    }

    function prompt_func() {
        previous_return_value=$?;
        prompt="\D{%Y-%m-%dT%H:%M:%S%z} ${TITLEBAR}${COLOR_NONE}$(whoami)@$(uname -n):\w${GREEN}"
        prompt+=" $(parse_git_branch)${COLOR_NONE} "
        if test $previous_return_value -eq 0
        then
            PS1="${prompt}$ "
        else
            PS1="${prompt}${RED}\$${COLOR_NONE} "
        fi
    }

    PROMPT_COMMAND=prompt_func
    #############################
    # end git prompt
    #############################
