## Python Environment Setup (using uv)

This project now uses **uv** for Python dependency management. To set up the project:

```bash
# Initial setup (one-time)
cd /Users/williamhea/Documents/Code/Websites/willhea.com/private/willhea.github.io_private
uv sync
```

Once `uv sync` is run, the virtual environment is created at `.venv/` and all dependencies are installed.

To execute Python tools and commands, use `uv run`:

```bash
# Examples:
uv run pelican --version
uv run python -c "import pelican; print(pelican.__version__)"
```

Or use the Makefile commands which automatically invoke `uv run`:

```bash
make html
make devserver
make publish
```

**Note:** Manual virtual environment activation (e.g., `source env/bin/activate` or `source .venv/bin/activate`) is no longer necessary.

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
1. ✅ Add uv for python (completed)

