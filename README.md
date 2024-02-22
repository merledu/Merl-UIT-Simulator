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



Next Go into the RISCV/r5pythonversion/templates folder and copy the path of m.txt file
Go into the RISCV/r5pythonversion/r5pythonversion/views.py file and change the path for the m.txt(The one we just copied) file according to your path file_values = open("/home/Desktop/Oxegon/Merl-UIT-Simulator/RISCV/r5pythonversion/templates/m.txt", "r")

Go into the RISCV/r5pythonversion folder and copy the path of m.txt file 
Next go into the Display_Info.py file (RISCV/r5pythonversion/r5pythonversion/Display_Info.py) and change 
file_values = open("/home/abdulrehman/Desktop/Oxegon/Merl-UIT-Simulator/RISCV/r5pythonversion/m.txt", "r")
to the path that you copied 


Then just go to the /Merl-UIT-Simulator/RISCV.r5pythonversion, then run below commands to run django local server and after that the provided link by previous command, open in your browser.

* python manage.py makemigrations
* python3 manage.py migrate
* python manage.py runserver

## Note:
There are some issues in Jump instructions, we will solve soon.
