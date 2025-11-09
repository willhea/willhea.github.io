Start python virtual environment on Linux:

```bash
source /home/willhea/Documents/willhea.com/private/willhea.github.io_private/env/bin/activate
```

Start python virtual environment on macOS (preferred: cd into the repo first):

```bash
cd /Users/williamhea/Documents/Code/Websites/willhea.com/private/willhea.github.io_private
source env/bin/activate
```

Git notes
 - Run git commands from the repository root directory (`willhea.github.io_private`). If you run `git status` from `private` you'll see "fatal: not a git repository..." because `private` itself isn't a repo.
 - From any directory you can point git at the repo with `-C`:

```bash
git -C /Users/williamhea/Documents/Code/Websites/willhea.com/private/willhea.github.io_private status
```

Inspiration: https://www.mattleaverton.com/pages/about.html

Testing instructions:

```bash
make html RELATIVE=1
make devserver RELATIVE=1
```

# To Do:
1. Add uv for python.

