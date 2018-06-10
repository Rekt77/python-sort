__author__ = "Rekt77"

def QuickSort(input_list,start,end):
    
    i,j = start,end
    
    if start < end:
        
        while i < j :

            stdKey = input_list[start]
            i,j = start,end
            
            while i <= end and stdKey>=input_list[i]:
                i+=1

            while j >= 0 and stdKey<input_list[j]:
                j-=1

            if(i<j):
                input_list[i],input_list[j] = input_list[j],input_list[i]
            else:
                input_list[start],input_list[j] = input_list[j],input_list[start]

        QuickSort(input_list,start,j-1)
        QuickSort(input_list,j+1,end)

def QuickSort2(input_list):
    if len(input_list) < 2:
        return input_list
    
    middle = input_list[0]
    less = [i for i in input_list[1:] if i<= middle]
    greater = [i for i in input_list[1:] if i>middle]

    input_list = QuickSort2(less) + [middle] + QuickSort2(greater)

    return input_list
    
if __name__ == "__main__" :
    input_list = [10,9,7,8, 13, 2, 6, 1, 4,3]
    QuickSort(input_list,0,len(input_list)-1)
    print(input_list)
    input_list = [10,9,8,7, 6, 5, 4, 3, 2,1]
    print(QuickSort2(input_list))
    

        
            
