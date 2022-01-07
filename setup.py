import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="find-unused-imports",
    author="Prince Roshan",
    author_email="princekrroshan01@gmail.com",
    url="https://github.com/Agent-Hellboy/find-unused-import",
    description=(
        "My solution to find_unused_import problem of python"
    ),
    long_description=read("README.md"),
    license="MIT",
    py_modules=["src/find_unused_imports","src/nodes"],
    entry_points={"console_scripts": ["find_unused_imports = find_unused_imports:find_unused_import"]},
    install_requires=["click"],
    include_package_data=True,
)