"# pybtall" 



### usage

1. dos command line with python interpreter
>env.bat
>python PyBluez-0.22\examples\simple\inquiry.py
performing inquiry...
found 4 devices
  00:1F:20:F8:43:70 - Bluetooth Mouse M336/M337/M535
  94:35:0A:9A:44:B5 - HS3000
  00:15:83:3A:E9:6A - mikechenday.ddns.net
  00:18:60:F9:50:7A - acer S56

2. use vscode
>env.bat
>code.exe

### lincense


opp, GPL3, pybluez
pybluez, GPL3, 

### real test
prepare a remote phone, acer and install bluetooth-ftp app
enter PyOBEX3\examples folder

>python inquiry_sdp.py

>python pbapclient.py 00:18:60:F9:50:7A

>python pushclient.py 00:18:60:F9:50:7A 23 hello.txt

>python get_files.py 00:18:60:F9:50:7A /

