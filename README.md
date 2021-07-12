# Multiple Choice Predictive Typing

## Installation

Clone this repository

``` shell
 $ git clone git@github.com:dyershov/multiple-choice-predictive-typing.git
 $ cd multiple-choice-predictive-typing
```

After cloning, you have two installation options:
* installing into user environment;
* installing into `conda` environment.

The former option is more convenient, but it pollutes the environment
with all dependencies, which may later be in conflict with multiple
python packages. The latter option requires more upfront steps, but
isolates the project completely in a separate viral environment.

### Installing into user environment

Add the following into your shell startup script (e.g., `~/.bashrc` for bash)

``` shell
# add local executable path
PATH=$PATH:${HOME}/.local/bin
```

Install python pip using your package manager. In Ubuntu, you need to do the following

``` shell
 $ sudo apt update
 $ sudo apt install python3-pip
```

Install this package

``` shell
 $ pip install --user -e .
```

### Installing into `conda` environmetns

Create and activate `conda` environment

``` shell
 $ conda create -n mcpt python=3.9
 $ conda activate mcpt
```

Install this package

``` shell
 $ pip install -e .
```

## Running the application

If you chose to install this package into user environment, simply run the app

``` shell
 $ mcpt
```
However, if you chose `conda` environments, then you have to activate it first before running the app

``` shell
 $ conda activate mcpt
 $ mcpt
```

### Dictionaries

By default the word completion uses `english-10k` dictionary that
contains ten thousand most common English words. It is possible to use
different dictionaries for word completion module. For example,
`russian-news` provides a collection of Russian words mostly used
during Russian news programs. If you wish to use this dictionary,
then run as follows:

``` shell
$ mcpt -d russian-news
```

Note that the alphabet will be chosen automatically based on the
dictionary.
