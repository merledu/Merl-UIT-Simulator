# Merl-UIT-Simulator (Oxygen)
To run this on locally on your computer just install python3 and pip3.

## Windows:
* https://www.python.org/downloads/
## Linux:
* sudo apt update && sudo apt install python3

After installing the python3, run below command in terminal to install pip.
* sudo apt update && sudo apt install python3-pip


After installing the python3 and pip, run below command in your cmd to install Django. 
* python -m pip install Django



```Next Go to
RISCV/r5pythonversion/templates folder and copy the path of m.txt file
```

```Go to
RISCV/r5pythonversion/r5pythonversion/views.py
```

```change the path
RISCV/r5pythonversion/r5pythonversion/views.py

file_values = open("/home/Desktop/Oxegon/Merl-UIT-Simulator/RISCV/r5pythonversion/templates/m.txt", "r")
replace with the path u copied
```

```Next Go to
 RISCV/r5pythonversion folder and copy the path of m.txt file 
```

```go into
Display_Info.py file (RISCV/r5pythonversion/r5pythonversion/Display_Info.py)
and change 
file_values = open("/home/abdulrehman/Desktop/Oxegon/Merl-UIT-Simulator/RISCV/r5pythonversion/m.txt", "r")
to the path that you copied
```



Then just go to the /Merl-UIT-Simulator/RISCV.r5pythonversion, then run below commands to run django local server and after that the provided link by previous command, open in your browser.

* python manage.py makemigrations
* python3 manage.py migrate
* python manage.py runserver

## Note:
There are some issues in Jump instructions, we will solve soon.
