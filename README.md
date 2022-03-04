This repo sets up a Python env to develop data science notebooks and scripts.

# Installation instructions

Important: all along the installation, follow terminal on-screen instruction to add paths etc

1. Make sure to have Python3.8 installed on your machine, if it's not the case:

   - install [HomeBrew](https://brew.sh/index_fr):

   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

   - install [Pyenv](https://github.com/pyenv/pyenv/blob/master/README.md) via Brew:

   ```bash
   brew install pyenv
   ```

   - configure your shell environment to activate pyenv (see [instructions](https://github.com/pyenv/pyenv#basic-github-checkout) according to your shell)
   - install Python3.8 via Pyenv:

   ```bash
   pyenv install 3.8
   ```

   Nb: if you encounter issues you can try another Python version but we can't ensure reproducibility

2. Make sure to have Poetry installed, if it's not the case:

   - install [Poetry](https://python-poetry.org/docs/):

   ```bash
   curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
   ```

3. Now move into the repository, that you should have cloned on your machine:

```bash
cd ...
```

4. Install the environment:

```bash
poetry env use 3.8
poetry install
```

Nb: adapt to your Python version if you installed another one

# How to use
You can now use your environment to execute Jupyter Lab:

```bash
poetry run jupyter lab
```

# Possible issues

- make sure to build poetry env from root of the project
- on M1 macs: try using native Python 3.8 and above... Known issues with some packages, check forums for compatible versions or alternative solutions
