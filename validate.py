# -*- coding: utf-8 -*-
"""
Desktop Alarm Project: Validate Module.

This module validates user inputs for time and video links.
"""

def check_alarm_input(alarm_time):
    """
    This function validates user input.
    
    The function checks if the values entered by the user for hours, minutes
    and seconds is in proper range or not.
        
    Args:
        alarm_input(list): Alarm input value as a list
        
    Returns: 
        is_valid_input(boolean): True if input format is correct else False
    """
    
    is_valid_input = False
    error_message = ''
    template = '{} should be less than {} and greater than equal to 0.'
    
    alarm_string = [n.strip() for n in alarm_time.split(":")]
    if sum([len(i) for i in alarm_string]) != 4:
        return (is_valid_input, 'Incorrect Format.')
    
    # [HH, mm]
    alarm_input = [int(n.strip()) for n in alarm_string.split(":")]
    if len(alarm_input) == 2:
        if alarm_input[0] in range(24): 
            if alarm_input[1] in range(60):
                is_valid_input = True
            else:
                error_message = template.format('Minutes', '60')
        else:
            error_message = template.format('Hours', '24')
    else:
        error_message = 'Invalid time.'
    return (is_valid_input, error_message)
  

def check_valid_characters(alarm_time):
    """
    This function checks if the input has any invalid character or not.
    
    Args:
        alarm_time(string): Alarm input as entered by the user
        
    Returns:
        has_valid_characters(boolean): True if input has valid characters
                                       else False
    """
    valid_characters = [chr(i) for i in range(48, 59)]
    valid_characters.append(' ')
    
    has_valid_characters = True
    error_message = ''
    
    for char in alarm_time:
        if char not in valid_characters:
            has_valid_characters = False
            error_message = 'Incorrect Format: Invalid character found.'
    return (has_valid_characters, error_message)        
