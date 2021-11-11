"""
# ----------------------
# Created : 01-11-2021 11:18
# Licencing : (C) 2021 Dalimol Abraham, LYIT
#             Available under GNU public licence
# Description: 
# Author : Dalimol Abraham
# ----------------------
"""
class MODULE:

    def __init__(self, mod_num, mod_name):
        self._mod_name = mod_name
        self._mod_num = mod_num

    @property
    def mod_details(self):
        return self._mod_name, self._mod_num

    @mod_details.setter
    def mod_details(self, value):
        print('Inside mod_details')
        self._mod_name = value

    @property
    def display_mod_details(self):
        print("Module name: {}".format(self._mod_name))
        print("Module number: {}".format(self._mod_num))
