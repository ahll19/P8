# P8 - Mattek8 \#(GROUP NUMBER)
- [P8 - Mattek8 #(GROUP NUMBER)](#p8---mattek8-group-number)
  - [Python Installation](#python-installation)
    - [1. Create the Venv](#1-create-the-venv)
    - [2. Install Dependencies](#2-install-dependencies)
  - [Structure of the Repository](#structure-of-the-repository)
    - [LICENSE](#license)
    - [requirements.txt](#requirementstxt)
  - [The `Source` Directory](#the-source-directory)
    - [Modules](#modules)

## Python Installation
### 1. Create the Venv
First create a python virtual environment with `Python3.11.1`. Then source virtual environment.

### 2. Install Dependencies
In the root directory of the repository you'll find the file `requirements.txt`. By running
```
pip install -r requirements.txt
```
you'll install all necessary dependencies to use this repository.

## Structure of the Repository
All code implemented in this repository can be found in the `Source` directory. All other files in the root directory are described in the following sections.

### LICENSE
This repository implements the MIT license. Any code taken from this repository is free to implement in any other open source project, but may not be implemented in proprietary products of any kind.

### requirements.txt
The installation of python dependecies is described in the [Install Dependencies](#2-install-dependencies) section. This file contains all dependencies necessary for this repository.

## The `Source` Directory
This directory houses all of the code used in this repository. All scripts meant for direct execution are in the root of `Source/`. This directory also Contains the `Modules/` directory.

### Modules
All tools used throughit this repository are located in this directory. Subdirectories of `Modules/` should serve to group tools based on their use-case. Each subdirectory in `Modules/` should serve as a module in and of itself, from which classes and useful functions can be imported.

The folder contains a few test scripts to get you started.