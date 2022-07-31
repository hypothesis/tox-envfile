import os.path

import dotenv
import pluggy

hookimpl = pluggy.HookimplMarker("tox")


@hookimpl
def tox_configure(config):
    envvars = dotenv.dotenv_values(os.path.join(config.toxinidir, ".devdata.env"))

    for envconfig in config.envconfigs.values():
        for name, value in envvars.items():
            envconfig.setenv[name] = value
