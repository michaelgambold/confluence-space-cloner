# Confluence Space Cloner

This project is designed to clone a templated Confluence space into a new space
so that the default setup is done automatically.

## Dependencies

This project is built using `Python` and uses `Poetry` for dependency management.
To setup your development environment the easiest way is to use Pyenv for
Python version management. Follow
[here](https://github.com/pyenv/pyenv#set-up-your-shell-environment-for-pyenv)
for information on installing Pyenv from the maintainer.

You should then install `pipx` to install Poetry. The instructions can be found
[here](https://pypa.github.io/pipx/installation/).

You can then install poetry with `pipx install poetry`.

## Makefile

A `Makefile` has been created to make running common commands easier. See below
for sample commands

```bash
# Install production dependencies
$ make install

# Install dev + prod dependencies
# $ make install-dev

# Run the app
$ make run
```

## Configuration

This application reads configuration settings via environment variables. When
running locally a `.env` file can be created with the required environment
variables.

If you populate environment variables via a different method then you don't
need a `.env` file.

A list of environment variables is included below.

| Name | Type | Sample | Notes |
|------|------|--------|-------|
| A    | int  |  `0`   |       |