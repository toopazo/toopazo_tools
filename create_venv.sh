
# Remove any previous venv
rm -r venv

# Install virtualenv
python_ver=$(./create_venv.py --pver); ${python_ver} -m venv venv
# python3.7 -m venv venv
# python3.8 -m venv venv
# python3.9 -m venv venv

# activate it
source venv/bin/activate

# Install libraries
python -m ensurepip --upgrade
python -m pip install --upgrade pip
python -m pip install -U scipy
python -m pip install -U numpu
python -m pip install -U matplotlib
#python -m pip install -U pyserial
#python -m pip install -U mavsdk
#python -m pip install -U pymavlink
# python -m pip install aioconsole
# sudo apt-get install can-utils
#python -m pip install -U python-can
#python -m pip install -U net-tools
#python -m pip install -U pyqt5
python -m pip install -U pandas

