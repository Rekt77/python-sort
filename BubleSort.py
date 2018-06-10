#!/usr/bin/python36
#__author__ == "Rekt77"


if __name__ == "__main__":
    input_list=[9,8,9,7,5,4,2,3,1]

    for i in range(0,len(input_list)-1):
        for j in range(0,len(input_list)-1):
            if input_list[j] > input_list[j+1] :
                input_list[j], input_list[j+1] = input_list[j+1],input_list[j]

    print(input_list)
    
