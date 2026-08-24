# CineBot

## Setup with UV

Install UV on Windows if it is not already available:

```console
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
uv --version
```

Initialize a new UV project (only needed when starting a project from scratch):

```console
uv init
```

Create the project environment and install the dependencies from `pyproject.toml` and `uv.lock`:

```console
uv sync
```

Run the application inside the project environment:

```console
uv run main.py
```

## UV Commands

Use these commands to manage the project:

```console
# Show UV version
uv --version

# Create or update the virtual environment and lockfile
uv sync

# Install dependencies without installing the project itself
uv sync --no-install-project

# Add a runtime dependency
uv add <package-name>

# Add a development dependency
uv add --dev <package-name>

# Remove a dependency
uv remove <package-name>

# Upgrade all dependencies allowed by pyproject.toml
uv lock --upgrade

# Upgrade one dependency
uv lock --upgrade-package <package-name>

# Install exactly what is recorded in uv.lock
uv sync --locked

# Run a command using the project environment
uv run <command>

# Run Python directly
uv run python

# Run the application
uv run main.py

# Show installed packages
uv pip list

# Install a package into the active environment without adding it to the project
uv pip install <package-name>

# Remove a package from the active environment
uv pip uninstall <package-name>
```

## Useful Checks

```console
# Check the project without changing the lockfile
uv lock --check

# Check that the environment matches the lockfile
uv sync --locked

# Display the project dependency tree
uv tree
```
