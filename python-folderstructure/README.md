## Python project folder structure

Table of contents
=================

1. [Introduction](#introduction)
2. [Use pipenv instead of requirements.txt](#pipenvinstall)
    1. [How to install pipenv](#install-pipenv)
3. [Python Package](#python-package)
4. [Make the package installable](#setup-py)
5. [Another paragraph](#paragraph4)

Introduction
-------------

This project will define the scafolding for all my python projects.We will improve this page as we learn from experience and blogs and practice.

Pre-requisites 
---------------

- Ensure ```pip``` and ```pipenv``` are installed.
- Clone the repo as a template: ```git clone git@github.com:dsantmajor/python-folderstructure```
- Fetch dependencies ```make install```
- activate virtual env ```pipenv shell```


## Use pipenv instead of requirements.txt <a name="paragraph1"></a> 



We will make use of pipenv ,this will look through the folder structure and it doesnt like if the parent directory has a requirements.txt file
https://docs.pipenv.org/

Install-Pipenv
-------------

### How to install Pipenv

``` pip3.6 install --user pipenv```

``` pipenv --python $(which python3.6)```

the abbove command will create a pipfile


**Contents of the pipfile :**

```
[[source]]

url = "https://pypi.python.org/simple"
verify_ssl = true
name = "pypi"


[dev-packages]



[packages]



[requires]

python_version = "3.6"

```

Python-package
--------------

### How to create a python package

We will use the __init__.py this is a special type of file, this lets python as it is searching through directories to figure out what the structure is ,what the packages and modules

Setup-py
--------

### Setup.py 
This is the most import file to make the package installable
We will use setuptools , its a libarary that 
## Another paragraph <a name="paragraph2"></a>
The second paragraph text
## Another paragraph <a name="paragraph3"></a>
The third paragraph text
## Another paragraph <a name="paragraph4"></a>
The fourth paragraph text



### Pipenv
We will make use of pipenv ,this will look through the folder structure and it doesnt like if the parent directory has a requirements.txt file
https://docs.pipenv.org/

## how to install Pipenv

``` pip3.6 install --user pipenv```

``` pipenv --python $(which python3.6)```

the abbove command will create a pipfile


**Contents of the pipfile :**

```
[[source]]

url = "https://pypi.python.org/simple"
verify_ssl = true
name = "pypi"


[dev-packages]



[packages]



[requires]

python_version = "3.6"

```
