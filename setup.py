from os import path
from setuptools import setup


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name="tox-envfile",
    version="0.0.1",
    py_modules=["tox_envfile"],
    entry_points={"tox": ["envfile = tox_envfile"]},
    install_requires=["python-dotenv"],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
