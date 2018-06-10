__author__ = "Rekt77"

def mergeSort(input_list):
    if len(input_list) > 1 :

        mid = int(len(input_list)/2)
        
        Leftlist = input_list[:mid]
        Rightlist = input_list[mid:]

        mergeSort(Left_list)
        mergeSort(Right_list)

        Lidx,Ridx,idx = 0,0,0

        while Lidx < len(Leftlist) and Ridx < len(Rightlist):
            if Leftlist[Lidx] < Rightlist[Ridx] :
                input_list[idx] = Leftlist[Lidx]
                Lidx+=1
            else:
                input_list[idx] = Rightlist[Ridx]
                Ridx+=1

            idx += 1

        while Lidx < len(Leftlist):
            input_list[idx] = Leftlist[Lidx]
            Lidx += 1
            idx += 1


        while Ridx < len(Rightlist):
            input_list[idx] = Rightlist[Ridx]
            Ridx += 1
            idx += 1

if __name__ == "__main__":
    input_list = [4,5,2,2,1,2,3,9,4,5,8,7]
    mergeSort(input_list)
    print(input_list)
