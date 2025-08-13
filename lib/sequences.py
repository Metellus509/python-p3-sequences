#!/usr/bin/env python3
def print_fibonacci(length):
    my_list=[]
    if(length==0):
        print(my_list)
    elif(length==1):
        my_list.append(0)
        print(my_list)
    elif(length==2):
        my_list.append(0)
        my_list.append(1)
        print(my_list)
    elif(length==10):
        my_list.append(0)
        my_list.append(1)
        for i in range(2,10,1):
            my_list.append(my_list[i-2]+my_list[i-1])
        print(my_list)