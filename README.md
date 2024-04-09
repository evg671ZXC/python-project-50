### Hexlet tests and linter status:

[![Actions Status](https://github.com/evg671ZXC/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/evg671ZXC/python-project-50/actions)
[![gendiff](https://github.com/evg671ZXC/python-project-50/actions/workflows/gendiff-check.yml/badge.svg)](https://github.com/evg671ZXC/python-project-50/actions/workflows/gendiff-check.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/584e23a061bc0b9fb819/maintainability)](https://codeclimate.com/github/evg671ZXC/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/584e23a061bc0b9fb819/test_coverage)](https://codeclimate.com/github/evg671ZXC/python-project-50/test_coverage)

# Gendiff

Compares two configuration files and shows a difference

## Installation and how to use

_Tested on CPython 3.10_

#### Cloned this repository into its current folder:

```
git clone https://github.com/evg671ZXC/python-project-50.git
```

#### For the package to work correctly it is necessary to use [Poetry](https://python-poetry.org/):

\*_If this setting is not needed, run the command:_

```
poetry config virtualenvs.in-project true
```

#### After execution, commands from the [Makefile](https://guides.hexlet.io/ru/makefile-as-task-runner/) will become available to us:

\*_It's recommended not to install third-party packages in the global environment_

```
make install
```

#### This command collects archives of source code:

```
make build
```

#### To install a package from the operating system, use the command:

```
make package-install
```

### Let's check that everything was installed correctly:

```
gendiff -h
```

## Description

### Comparison of json and yaml/yml format files

[![asciicast](https://asciinema.org/a/647948.svg)](https://asciinema.org/a/647948)

[![asciicast](https://asciinema.org/a/650834.svg)](https://asciinema.org/a/650834)

### Support for comparing nested structures and displaying them visually

#### -f stylish (_default_)

[![asciicast](https://asciinema.org/a/651777.svg)](https://asciinema.org/a/651777)

#### -f plain

[![asciicast](https://asciinema.org/a/651778.svg)](https://asciinema.org/a/651778)

### Get the program skeleton you need to enter the command: `-f json`

[![asciicast](https://asciinema.org/a/651784.svg)](https://asciinema.org/a/651784)
