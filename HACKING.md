# Setting up Your tox-envfile Development Environment

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
cd tox_envfile
make help
```

Releasing a New Version of the Project
--------------------------------------

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

Changing the Project's Python Versions
--------------------------------------

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

Changing the Project's Python Dependencies
------------------------------------------

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
`tox-recreate` into the local development environment of another tox-using
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

3. Uninstall the production copy of `tox-recreate` from `cookiecutter-pypackage-test`'s `.tox/.tox` venv:

   ```terminal
   /tmp/cookiecutter-pypackage-test/.tox/.tox/bin/pip uninstall tox-recreate
   ```

4. Install your local development copy of tox-recreate into `cookiecutter-pypackage-test`'s `.tox/.tox` venv:

   ```terminal
   /tmp/cookiecutter-pypackage-test/.tox/.tox/bin/pip install -e .
   ```

5. Now `cookiecutter-pypackage-test` commands will use your local development copy of `tox-recreate`:

   ```terminal
   make --directory "/tmp/cookiecutter-pypackage-test" test
   ```
