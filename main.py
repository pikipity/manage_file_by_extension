# encoding=utf-8
__author__ = 'wangze'

import os
import shutil

error=False

input_path=raw_input("Please input the path of files:\n")

if(not os.path.isdir(input_path)):
    print "Your input %s is not a path, or this path doesn't exist."%input_path
    error=True
else:
    output_path=raw_input("please input the path to store files:\n")
    if(not os.path.isdir(output_path)):
        os.makedirs(output_path)

if(error):
    print "There are some error. Please double check your path."
else:
    print "Start"
    if(input_path[len(input_path)-1]!='/'):
        input_path=input_path+'/'
    if(output_path[len(output_path)-1]!='/'):
        output_path=output_path+'/'
    file_list=os.listdir(input_path)
    print "Total %s files"%len(file_list)
    for x in range(0,len(file_list)):
        name_and_extention=os.path.splitext(file_list[x])
        extention=name_and_extention[len(name_and_extention)-1].lower()
        extention=extention[1:len(extention)]
        if(len(extention)!=0):
            if(not os.path.exists(output_path+extention)):
                os.makedirs(output_path+extention)
            shutil.copyfile(input_path+file_list[x],output_path+extention+'/'+file_list[x])
        print "%.3f"%((x+1.0)/len(file_list)*100)+"%"+": %sth file has been finished from %s to %s"%((x+1),input_path+file_list[x],output_path+extention+'/'+file_list[x])
    print "All Finish"