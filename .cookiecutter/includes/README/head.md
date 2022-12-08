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
