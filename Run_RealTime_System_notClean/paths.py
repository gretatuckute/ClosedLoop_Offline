# -*- coding: utf-8 -*-
'''
Initialization of paths for EEG scripts, stimuli scripts, subjects directory, and data directory.
'''

import os

def base_dir_init(): # Base directory for ClosedLoop GitHub
    this_base_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    return this_base_dir

def gitlab_dir_init(): # Base directory for GitLab (storage of files). Different from the Scripts directory (GitHub)
    gitlab_dir = 'C:\\Users\\nicped\\Documents\\GitLab\\project'
    return gitlab_dir

def script_path_init():
    script_path = base_dir_init() + '\Scripts'
    return script_path

def data_path_init(): # Data (images) storage directory
    data_path = gitlab_dir_init() + '\data'
    return data_path

def subject_path_init(): # Subjects directory, for storing EEG data 
    subject_path = gitlab_dir_init() + '\SUBJECTS'
    return subject_path


if __name__ == '__main__':
    base_dir = base_dir_init()
    print('====== Current directory ======')
    print(base_dir)
   