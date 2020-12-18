# -*- coding: utf-8 -*-
"""
Desktop Alarm: Alarm Module.

This module contains methods that update alarm time video links in the
associated text files.
"""

import validate
import logging


def _update_alarm_file(alarm_time, ops):
    """
    Function to update alarm file.
    
    This function updates all_alarms.txt file.
    
    Args:
        alarm_time(string): Alarm time set by the user.
        ops(string): Operation to be performed (add/delete).
        
    Returns:
        msg(string): Message for user once action has been performed.
    """
    
    with open('all_alarms.txt', 'a+') as alarm_file:
        alarm_file.seek(0)
        
        alarm_list = alarm_file.readlines()
        alarm_file.seek(0)
        alarm_file.truncate()
                    
        condition_1 = alarm_time in alarm_list
        condition_2 = alarm_time + '\n' in alarm_list
        
        if ops == 'add':
            if condition_1 | condition_2:
                msg = 'Alarm already set for this time!'
            else:
                if len(alarm_list) > 0:
                    alarm_list[-1] = alarm_list[-1] + '\n'
                alarm_list.append(alarm_time)
                msg = 'Alarm is set for {} everyday'.format(alarm_time)
                
        if ops == 'delete':
            if condition_1:
                alarm_list.remove(alarm_time)
                msg = 'Alarm at {} hours has been deleted'.format(alarm_time)
            elif condition_2:
                alarm_list.remove(alarm_time + '\n')
                msg = 'Alarm at {} hours has been deleted'.format(alarm_time)
            else:
                msg = 'Alarm not found!'
        alarm_file.writelines(alarm_list)
    return msg

 
def get_alarm_list():
    """
    Function to get list alarms set by the user.
    
    Returns:
        msg(string): Message for user once action has been performed.    
    """
    
    with open('all_alarms.txt', 'r') as alarm_file:
        alarm_list = alarm_file.readlines()
        if len(alarm_list) == 0:
            msg = 'No alarms are set.'
        else:
            msg = ''.join(alarm_list)
        return msg

               
def update_alarm(alarm_time, ops='add'):
    """ 
    Function to check and update alarm.
    
    Args:
        alarm_time(string): Alarm time set by the user.
        ops(string): Operation to be performed (add/delete).
    """
    
    logging.basicConfig(filename='alarm_LOGS.log',
                    format='%(levelname)s %(asctime)s :: %(message)s',
                    level=logging.DEBUG)
    
    # Check for blank input
    if len(alarm_time.strip()) > 0:    
        logging.debug("PASS: Input is provided.")
        
        # Check for valid characters in the user input
        status = validate.check_valid_characters(alarm_time)
        if status[0]:
            logging.debug("PASS: Input does not have special characters.")
    
            # Check if time entered by user is correct
            status = validate.check_alarm_input(alarm_time)
            if status[0]:
                logging.debug("PASS: Time entered by user is valid.")
                msg = _update_alarm_file(alarm_time, ops)
                return (True, msg)
            else:
                logging.critical("FAIL: Please enter time in correct format")
                return status
        else:
            logging.critical("FAIL: Special characters detected.")
            return status
    else:
        logging.critical("FAIL: No value provided.")
        return (False, 'No value provided.')
        
def _update_video_file(video, ops):
    """
    Function to update videos file.
    
    This function adds or deletes video links from the videos file.
    
    Args:
        video(string): Video link as entered by the user.
        ops(string): Action (add/delete) requested by the user.
        
    Returns:
        msg(string): Message for user once action has been performed.
    """
    
    with open('youtube_alarm_videos.txt', 'a+') as video_file:
        video_file.seek(0)
        
        video_list = video_file.readlines()
        video_file.seek(0)
        video_file.truncate()
                    
        condition_1 = video in video_list
        condition_2 = video + '\n' in video_list

        if ops == 'add':
            if condition_1 | condition_2:
                msg = 'Video already added!'
            else:
                if len(video_list) > 0:
                    video_list[-1] = video_list[-1] + '\n'
                video_list.append(video)
                msg = 'Video has been added.\nLink: {}'.format(video)
                
        if ops == 'delete':
            if condition_1:
                video_list.remove(video)
                msg = 'Video has been deleted.\nLink: {}'.format(video)
            elif condition_2:
                video_list.remove(video + '\n')
                msg = 'Video has been deleted.\nLink: {}'.format(video)
            else:
                msg = 'Video not found!'
        video_file.writelines(video_list)
    return msg
                 
def get_video_list():
    """
    Function to get list videos.
    
    Returns:
        msg(string): Message for user once action has been performed.
    """
    
    with open('youtube_alarm_videos.txt', 'r') as video_file:
        video_list = video_file.readlines()
        if len(video_list) == 0:
            msg = 'No videos found.'
        else:
            msg = '\n'.join(video_list)
        return msg
    
def update_video(video, ops='add'):
    """
    Function to add or delete video from videos file.
    """
    
    condition_1 = 'https://www.youtube.com/watch?v=' not in video
    condition_2 = len(video.strip()) != 43
    
    if condition_1 | condition_2:
        return 'Not a valid youtube link.'
    return _update_video_file(video, ops)