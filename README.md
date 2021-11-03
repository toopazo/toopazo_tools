# toopazo_tools
This is the repository for the pip module ```https://pypi.org/project/toopazo-tools/```

It consists of python package for common file-processing tasks


## How to update a new version to https://pypi.org/  

This is note to myself about the necessary steps to upload a new version 
of the code to the repo in https://pypi.org/.

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
