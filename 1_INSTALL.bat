@ECHO OFF
CLS
curl -L "https://www.python.org/ftp/python/3.9.5/python-3.9.5-amd64.exe" -O %~dp0\python-3.9.5-amd64.exe
%~dp0\python-3.9.5-amd64.exe /quiet SimpleInstall=1 InstallAllUsers=1 PrependPath=1 Include_test=0 Include_launcher=0 Include_tcltk=0
pause
python -m venv venv
pip3 install xlrd openpyxl pandas
pause
