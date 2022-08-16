# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 21:04:26 2022

@author: USER
"""

def square_odd(pylist):
    square_list = [number*number for number in pylist if number % 2 != 0]
    return square_list


