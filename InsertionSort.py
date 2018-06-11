#!/usr/bin/python36
__author__ = "Rekt77"

if __name__ == "__main__" :
    input_list = [4,6,1,2,9,4,5,2,3,4]

    for i in range(0,len(input_list)):
        idx_value = input_list[i]
        idx = i
        
        while idx > 0 and input_list[idx-1] >idx_value:
            input_list[idx],input_list[idx-1] = input_list[idx-1],input_list[idx]
            idx  = idx - 1

    print(input_list)
            
            
