# -*- coding: utf-8 -*-
""" 
Desktop Alarm Project: User Interface Module. 

This module creates the Desktop Alarm user interface.    
"""

import tkinter as tk
from tkinter import font, messagebox
import alarm as al


def set_alarm():
    """ 
    This function enables the user to set alarm time.    
    """

    alarm_time = alarm_time_field.get()
    status = al.update_alarm(alarm_time)
    if not status[0]:
        messagebox.showinfo('Error', status[1])
    if status[0]:
        messagebox.showinfo('Info', status[1])
        # check 
        master.destroy()
        
def delete_alarm():
    """ 
    This function enables the user to delete alarm.    
    """
    
    alarm_time = alarm_time_field.get()
    status = al.update_alarm(alarm_time, 'delete')
    if not status[0]:
        messagebox.showinfo('Error', status[1])
    if status[0]:
        messagebox.showinfo('Info', status[1])
        
def get_all_alarms():
    """
    This function enables user to see all the active alarms.
    """
    
    msg = al.get_alarm_list()
    if msg == 'No alarms are set.':
        title = 'Info'
    else:
        title = 'List Of Alarms'
    messagebox.showinfo(title, msg)

def add_video():
    """
    This function enables user to add video to the videos file.
    """
    
    video = url_field.get()
    msg = al.update_video(video)
    messagebox.showinfo('Info', msg)

def delete_video():
    """
    This function enables user to delete video from videos file.
    """
    
    video = url_field.get()
    msg = al.update_video(video, 'delete')
    messagebox.showinfo('Info', msg)
    
def get_all_videos():
    """
    This function enables user to see all the videos present in videos file.
    """
    
    msg = al.get_video_list()
    if msg == 'No videos found.':
        title = 'Info'
    else:
        title = 'List Of Videos'
    messagebox.showinfo(title, msg)
    
# Creating main frame of the application.
master = tk.Tk()
master.geometry('270x300')
master.title('Desktop Alarm')
master.maxsize(270, 300)
master.minsize(270, 300) 

tk.Label(master, text=' ').grid(row=0, column=0, rowspan=2)

# Creating application header
title_font = font.Font(size=20, weight='bold')
title = tk.Label(master, text='     Alarm Clock', font=title_font)
title.grid(row=0, column=1, rowspan=2, columnspan=4)

# Creating 'Time' label
tk.Label(master, text=' ').grid(row=2, column=0)
font_size = font.Font(size=12)
tk.Label(master, text='   Time :', font=font_size).grid(
        row=3, column=0, rowspan=1, columnspan=2)

# Creating widget for user to enter time. 
alarm_time_field = tk.Entry(master)
alarm_time_field.grid(row=3, column=2, columnspan=4)
tk.Label(master, text='HH : mm \n(24 hour format)').grid(
        row=4, column=2, columnspan=4)

# Creating button to set alarm time
add_alarm_button = tk.Button(master, text='Set Alarm',
                             command=set_alarm, width=9)
add_alarm_button.grid(row=5, column=2)

# Creating button to delete alarm
delete_alarm_button = tk.Button(master, text='Delete',
                                command=delete_alarm, width=9)
delete_alarm_button.grid(row=5, column=4)

# Creating 'Video' label
tk.Label(master, text=' ').grid(row=6)
tk.Label(master, text=' Video :', font=font_size).grid(
        row=7, column=0, rowspan=2, columnspan=2)

# Creating widget for user to enter video link
url_field = tk.Entry(master)
url_field.grid(row=7, column=2, columnspan=4)

# Creating button to add video link
add_button = tk.Button(master, text='Add', command=add_video, width=9)
add_button.grid(row=9, column=2)

# Creating button to delete video link
delete_button = tk.Button(master, text='Delete',
                          command=delete_video, width=9)
delete_button.grid(row=9, column=4)


tk.Label(master, text=' ').grid(row=10)

# Creating button to get list of active alarms
all_alarms = tk.Button(master, text='All Alarms',
                       command=get_all_alarms, width=15)
all_alarms.grid(row=11, column=2, columnspan=4)

# Creating button to get list of videos
all_videos = tk.Button(master, text='All Videos',
                       command=get_all_videos, width=15)
all_videos.grid(row=12, column=2, columnspan=4)

tk.mainloop()