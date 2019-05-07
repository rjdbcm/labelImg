#!/bin/sh

brew install python@3
pip install --upgrade virtualenv 

# clonde labelimg source
rm -rf /tmp/SLGR-SuiteSetup
mkdir /tmp/SLGR-SuiteSetup
cd /tmp/SLGR-SuiteSetup
curl https://codeload.github.com/rjdbcm/slgrSuite/zip/master --output slgrSsuite.zip
unzip slgr-suite.zip
rm slgr-suite.zip

# setup python3 space
virtualenv --system-site-packages  -p python3 /tmp/SLGR-SuiteSetup/slgrSuite-py3
source /tmp/SLGR-SuiteSetup/slgrSuite-py3/bin/activate
cd slgrSuite-master

# build labelImg app
pip install py2app
pip install PyQt5 lxml
make qt5py3
rm -rf build dist
python setup.py py2app -A
mv "/tmp/SLGR-SuiteSetup/slgrSuite-master/dist/SLGR-Suite.app" /Applications
# deactivate python3
deactivate
cd ../
rm -rf /tmp/SLGR-SuiteSetup
echo 'DONE'