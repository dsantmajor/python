## Python project folder structure

### Pipenv
We will make use of pipenv ,this will look through the folder structure and it doesnt like if the parent directory has a requirements.txt file
https://docs.pipenv.org/

## how to install Pipenv

``` pip3.6 install --user pipenv```

``` pipenv --python $(which python3.6)```
the abbove command will create a pipfile

```
➜  project_name git:(master) ✗ cat Pipfile
[[source]]

url = "https://pypi.python.org/simple"
verify_ssl = true
name = "pypi"


[dev-packages]



[packages]



[requires]

python_version = "3.6"
```
