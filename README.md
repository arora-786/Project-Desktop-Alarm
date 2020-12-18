# Desktop Alarm Project

This project aims to demonstrate how to build simple user interface using 
tkinter library of python, and auto schedule run python script using windows 
task scheduler and batch file.

**Authors:**
* Deval
* Jonatas
* Saurabh
* Camilo

### Features

* The set alarm will run everyday at the time specified
* **Set Alarm Button:** Enables user to set alarm
* **Delete Button:** (under time) Enables user to delete alarm
* **Add Button:** Enables user add youtube video
* **Delete Button:** (under video) Enables user to delete video
* **All Alarms Button:** Enables user to see all the alarms that are set
* **All Videos Button:** Enables user to see all videos that are added

### How to run the code

1. Download all the files
2. Create a batch file (.bat) 
    * Provide the paths to Python exe and 'trigger_alarm.py' file.
    * Using windows task scheduler, schedule the batch file to run every 15 min
    * [Reference](https://datatofish.com/python-script-windows-scheduler/) to create batch file and scheduling python code.
3. Run user_interface.py to set the time and perform other operations.