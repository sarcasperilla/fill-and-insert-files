#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 18:45:26 2018

@author: michaelcasper
"""

# fillingGaps.py - Finds all files with a given prefix in a single folder and
# locates any gaps in the numbering. It will rename the files to close the gap.

import os
import shutil
import re


def filling_gaps(folder, prefix):
    filelist = os.listdir(folder)
    abs_working_dir = os.path.abspath(folder)
    file_count = 1
    for filename in filelist:
        if filename.startswith(prefix):
            suffix = re.compile(r'(\.\w+)$').search(filename).group()
            current_filename = find_current_filename(file_count, prefix, 
                                                     suffix)
            if filename == current_filename:
                file_count += 1
                continue
            else:
                old_filename = os.path.join(abs_working_dir, filename)
                new_filename = os.path.join(abs_working_dir, current_filename)
                print('Renaming %s\nto %s' % (old_filename, new_filename))
                print()
                shutil.move(old_filename, new_filename)
            file_count += 1
    print('Done.')


def find_current_filename(file_count, prefix, suffix):
    file_count = str(file_count)
    current_filename = prefix + file_count.rjust(3, '0') + suffix
    return current_filename
