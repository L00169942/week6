"""
# ----------------------
# Created : 03-11-2021 09:46
# Licencing : (C) 2021 Dalimol Abraham, LYIT
#             Available under GNU public licence
# Description: 
# Author : Dalimol Abraham
# ----------------------
"""
from annotation.student_Class import STUDENT
from annotation.room_Class import ROOM
from annotation.module_Clas import MODULE
if __name__ == '__main__':
    print('First Step')
    details = STUDENT("Dalimol Abraham", "L00169942")
    details.display_details

    # print('Second')
    ModName = MODULE(1, 'Python')
    print(ModName.display_mod_details)

    print('Third')
    RoomDet = ROOM(2409)
    print(RoomDet.display_class_details)

    print("Thank you for using my application")
