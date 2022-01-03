# toopazo_tools
Python package for common file-processing tasks

There is a bash file to automate the creation of a python virtual environment

```
. ./create_venv.sh
```

## Update package stored in a git repo (e.g. Github)

1. Open setup.py and increment the version (e.g., version='1.0.3' to version='1.0.4'). 
   This can be done automatically by running 
   ```
   python increment_setup_version.py
   ```
2. Upload the new version to the repo
    ```
   git status
   git add .
   git commit -m "new version of this python package"
   git push      
    ```
6. Install the package on another remote/project/environment etc
    ```
    python -m pip install git+https://github.com/toopazo/toopazo_tools.git
    ```
 

## Update package stored in PyPi

I wrote a bash file to automate the update and uploading process to pypi. 
It is can be executed in the terminal using

```
. ./update_library.sh
```

The steps involved are taken from https://widdowquinn.github.io/coding/update-pypi-package/

1. Update local packages for distribution
    ```
    python3 -m pip install --user --upgrade setuptools wheel
    python3 -m pip install --user --upgrade twine 
    ```
2. Open setup.py and change the version, e.g., version='1.0.3'. 
   This can be done automatically by running 
   ```
   python increment_setup_version.py
   ```
3. It is sometimes neccessary to delete the build/ and dist/ folder
    ```
    rm -r build/*
    rm -r dist/*
    ```
4. Create distribution packages on your local machine, and check
the dist/ directory for the new version files
    ```
    python3 setup.py sdist bdist_wheel
    ```
5. Upload the distribution files to https://pypi.org/ server
    ```
    python3 -m twine upload dist/*
    ```
6. Install the package from https://pypi.org/ server
    ```
    python3 -m pip install -U toopazo-tools
    ```
