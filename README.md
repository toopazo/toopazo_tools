# toopazo_pylib
A personal python library for common file-processing tasks

Important links
- https://packaging.python.org/tutorials/packaging-projects/
- https://test.pypi.org/manage/account/token/
- https://test.pypi.org/project/tpylib-pkg-toopazo/

Note to myself: Commands to upload a new version of this python package. 
This is taken from https://widdowquinn.github.io/coding/update-pypi-package/

1. Update local packages for distribution
    ```
    python3 -m pip install --user --upgrade setuptools wheel
    python3 -m pip install --user --upgrade twine 
    ```
2. Open setup.py and change the version, e.g., version='1.0.3'. It is also recomended to delete the build/ folder
    ```
    rm -r build/*
    ```
3. Create distribution packages on your local machine, and check the dist/ directory for the new version files
    ```
    python3 setup.py sdist bdist_wheel
    ```
4. Upload the distribution files to pypi’s test server
    ```
    python3 -m twine upload --repository testpypi dist/*
    ```
5. Install the distribution files from pypi’s test server
    ```
    python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps tpylib-pkg-toopazo
    ```



