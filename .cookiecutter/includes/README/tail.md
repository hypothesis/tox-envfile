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
