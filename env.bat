echo set the pythonpath 

echo %~dp0
set PYBTALL_HOME=%~dp0

set PYTHONPATH=%PYTHONPATH%;%PYBTALL_HOME%src
echo PYTHONPATH=%PYTHONPATH%