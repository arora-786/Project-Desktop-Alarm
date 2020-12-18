# -*- coding: utf-8 -*-
"""
Desktop Alarm Project: Alarm Trigger Module.
"""

import random
import requests
import webbrowser
import datetime
import time
import logging


def _convert_time(input_time):
    """
    This function converts input time in seconds.
    
    Args:
        input_time(string): Input time
        
    Returns:
        input_time_seconds(int): Time in seconds.
    """
    
    # Number of seconds in an Hour, Minute, and Second
    seconds_hms = [3600, 60, 1]
    input_time_list = [int(i.strip()) for i in input_time.split(":")]
    input_time_seconds = sum([i * j 
                              for i, j in zip(seconds_hms, input_time_list)])
    return input_time_seconds
    
def trigger_alarm():
    """
    Function to trigger alarm.
    """
    
    logging.basicConfig(filename='alarm_LOGS.log',
                    format='%(levelname)s %(asctime)s :: %(message)s',
                    level=logging.DEBUG)
    triggering_interval = 900 #15 minutes to seconds
    current_time = datetime.datetime.now()
    
    with open('all_alarms.txt', 'r') as file:
        alarms = [i + ':00' for i in file.readlines() if len(i.strip()) > 0]
    
    if len(alarms) < 1:
        return
    
    seconds_time_list = []
    for alarm in alarms:
        seconds_time_list.append(_convert_time(alarm))
        
    current_time_seconds = _convert_time(
            str(current_time.hour) + ':' + 
            str(current_time.minute) + ':' + str(current_time.second))
        
    time_diff_list = []
    for seconds_time in seconds_time_list:
        time_diff = seconds_time - current_time_seconds
        if time_diff > 0 and time_diff < triggering_interval:
            time_diff_list.append(time_diff)
    
    if len(time_diff_list) < 1:
        return
    
    time_diff_list.sort()
    diff_list = [time_diff_list[0]]
    diff_list.extend(
            [time_diff_list[i+1] - time_diff_list[i] 
            for i in range(len(time_diff_list) - 1)])
        
    with open("youtube_alarm_videos.txt", "r") as alarm_file:
        videos = alarm_file.readlines()
        
    #Opens a random youtube video from a set of youtube videos
    #x=random.choice(videos)
    for diff in diff_list:
        try:
           #r = requests.head(x)
           print('Next alarm will go off in {} seconds'.format(diff))
           time.sleep(diff)
           logging.debug("Wake up!: Its time! Playing your favourite video!")
           webbrowser.open(random.choice(videos))
        except requests.ConnectionError:
           logging.debug("FAIL: The input link is invalid")
           
trigger_alarm()