"""
# ----------------------
# Created : 01-11-2021 11:07
# Licencing : (C) 2021 Dalimol Abraham, LYIT
#             Available under GNU public licence
# Description: 
# Author : Dalimol Abraham
# ----------------------
"""
class STUDENT:

    # def __init__(self, name, roll):
    #     print("Inside Init")
    #     self._name = name
    #     self._roll = roll
    #     print(self._name,self._roll)
    #
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    # @property
    # def student_details(self):
    #     print('Inside srudent details') #getter
    #     return self.name, self.roll


    # def stud_details(self):
    #     print('Inside property')
    #     print(self._name,self._roll)
    #     return self._name, self._roll
    #
    # @stud_details.setter
    # def stud_details(self, name, roll):
    #     print("Inside stud_details")
    #     self._name = name
    #     self._roll = roll
    #
    @property
    def display_details(self):
        print("Name : ", self.name,  ", Roll Number: ", self.roll)

        # return
