#!/usr/bin/python36
#__author__ == "Rekt77"

if __name__ == "__main__" :
    input_list = [4,6,1,2,9,4,5,2,3,4]
    print(input_list)
    
    for i in range(0,len(input_list)-1):
        MIN_VALUE = input_list[i]
        for j in range(i,len(input_list)):
            if MIN_VALUE > input_list[j]:                
                MIN_VALUE = input_list[j]
                print("MIN : %d"%MIN_VALUE)
                input_list[i],input_list[j] = input_list[j],input_list[i]
                print(input_list)   
        print("round : %d"%(i+1),end="\n\n")
                
        

    print (input_list)
        
        
