<a href="https://github.com/hypothesis/tox-envfile/actions/workflows/ci.yml?query=branch%3Amain"><img src="https://img.shields.io/github/actions/workflow/status/hypothesis/tox-envfile/ci.yml?branch=main"></a>
<a href="https://pypi.org/project/tox-envfile"><img src="https://img.shields.io/pypi/v/tox-envfile"></a>
<a><img src="https://img.shields.io/badge/python-3.12 | 3.11 | 3.10 | 3.9-success"></a>
<a href="https://github.com/hypothesis/tox-envfile/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-BSD--2--Clause-success"></a>
<a href="https://github.com/hypothesis/cookiecutters/tree/main/pypackage"><img src="https://img.shields.io/badge/cookiecutter-pypackage-success"></a>
<a href="https://black.readthedocs.io/en/stable/"><img src="https://img.shields.io/badge/code%20style-black-000000"></a>

# tox-envfile

Load env files in your tox envs.

tox-envfile reads environment variables from a file named `.devdata.env` in the
same directory as your `tox.ini` file and adds them to the environment that tox
runs your commands in.

This is a pretty dumb plugin for now: all of the environment variables in
`.devdata.env` will be loaded into the environment for every tox env that you
run, unconditionally. Any existing envvars with conflicting names will be
overwritten. Only a single environment file is supported and it must be named
`.devdata.env`.

env File Format
---------------

[python-dotenv](https://saurabh-kumar.com/python-dotenv/) is used for the env file parsing.

The `.devdata.env` file should be an env file with contents that look like
this:

```shell
# a comment that will be ignored.
REDIS_ADDRESS=localhost:6379
MEANING_OF_LIFE=42
MULTILINE_VAR="hello\nworld"
```

Or like this:

```shell
export S3_BUCKET=YOURS3BUCKET
export SECRET_KEY=YOURSECRETKEYGOESHERE
```

POSIX variable expansion works, using variables from the environment or from
earlier lines in the env file:

```shell
CONFIG_PATH=${HOME}/.config/foo
DOMAIN=example.org
EMAIL=admin@${DOMAIN}
```

## Setting up Your tox-envfile Development Environment

First you'll need to install:

* [Git](https://git-scm.com/).
  On Ubuntu: `sudo apt install git`, on macOS: `brew install git`.
* [GNU Make](https://www.gnu.org/software/make/).
  This is probably already installed, run `make --version` to check.
* [pyenv](https://github.com/pyenv/pyenv).
  Follow the instructions in pyenv's README to install it.
  The **Homebrew** method works best on macOS.
  The **Basic GitHub Checkout** method works best on Ubuntu.
  You _don't_ need to set up pyenv's shell integration ("shims"), you can
  [use pyenv without shims](https://github.com/pyenv/pyenv#using-pyenv-without-shims).

Then to set up your development environment:

```terminal
git clone https://github.com/hypothesis/tox-envfile.git
cd tox-envfile
make help
```

## Releasing a New Version of the Project

1. First, to get PyPI publishing working you need to go to:
   <https://github.com/organizations/hypothesis/settings/secrets/actions/PYPI_TOKEN>
   and add tox-envfile to the `PYPI_TOKEN` secret's selected
   repositories.

2. Now that the tox-envfile project has access to the `PYPI_TOKEN` secret
   you can release a new version by just [creating a new GitHub release](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository).
   Publishing a new GitHub release will automatically trigger
   [a GitHub Actions workflow](.github/workflows/pypi.yml)
   that will build the new version of your Python package and upload it to
   <https://pypi.org/project/tox-envfile>.

## Changing the Project's Python Versions

To change what versions of Python the project uses:

1. Change the Python versions in the
   [cookiecutter.json](.cookiecutter/cookiecutter.json) file. For example:

   ```json
   "python_versions": "3.10.4, 3.9.12",
   ```

2. Re-run the cookiecutter template:

   ```terminal
   make template
   ```

3. Commit everything to git and send a pull request

## Changing the Project's Python Dependencies

To change the production dependencies in the `setup.cfg` file:

1. Change the dependencies in the [`.cookiecutter/includes/setuptools/install_requires`](.cookiecutter/includes/setuptools/install_requires) file.
   If this file doesn't exist yet create it and add some dependencies to it.
   For example:

   ```
   pyramid
   sqlalchemy
   celery
   ```

2. Re-run the cookiecutter template:

   ```terminal
   make template
   ```

3. Commit everything to git and send a pull request

To change the project's formatting, linting and test dependencies:

1. Change the dependencies in the [`.cookiecutter/includes/tox/deps`](.cookiecutter/includes/tox/deps) file.
   If this file doesn't exist yet create it and add some dependencies to it.
   Use tox's [factor-conditional settings](https://tox.wiki/en/latest/config.html#factors-and-factor-conditional-settings)
   to limit which environment(s) each dependency is used in.
   For example:

   ```
   lint: flake8,
   format: autopep8,
   lint,tests: pytest-faker,
   ```

2. Re-run the cookiecutter template:

   ```terminal
   make template
   ```

3. Commit everything to git and send a pull request

Testing Manually
----------------

To test it manually you can install your local development copy of
`tox-envfile` into the local development environment of another tox-using
project such as
[cookiecutter-pypackage-test](https://github.com/hypothesis/cookiecutter-pypackage-test):

1. Install a local development copy of `cookiecutter-pypackage-test` in a temporary directory:

   ```terminal
   git clone https://github.com/hypothesis/cookiecutter-pypackage-test.git /tmp/cookiecutter-pypackage-test
   ```

2. Run `cookiecutter-pypackage-test`'s `make sure` command to make sure that
   everything is working and to trigger tox to create its `.tox/.tox`
   venv:

   ```terminal
   make --directory "/tmp/cookiecutter-pypackage-test" sure
   ```

3. Uninstall the production copy of `tox-envfile` from `cookiecutter-pypackage-test`'s `.tox/.tox` venv:

   ```terminal
   /tmp/cookiecutter-pypackage-test/.tox/.tox/bin/pip uninstall tox-envfile
   ```

4. Install your local development copy of `tox-envfile` into `cookiecutter-pypackage-test`'s `.tox/.tox` venv:

   ```terminal
   /tmp/cookiecutter-pypackage-test/.tox/.tox/bin/pip install -e .
   ```

5. Now `cookiecutter-pypackage-test` commands will use your local development copy of `tox-envfile`:

   ```terminal
   make --directory "/tmp/cookiecutter-pypackage-test" test
   ```
