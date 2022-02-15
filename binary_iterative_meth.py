
def binary_search(list1,n):
    low=0
    high=len(list1)-1
    mid =0

    while low<=high:
    #for getting int result
        mid=(high+low) //2

    #Check if n is present in the mid
    if list1 [mid]<n:
        low=mid+1

    #if n is greater ,compare to the right of the mid
    elif list1 [mid]>n:
        high =mid-1

#if n is smaller,compare to the left of the mid
    else:
        return mid
#element was not present on the list

    return -1
#initialize the list

list1 =[12,45,5,67,3,455]
n=0

#function call
result= binary_search (list1,n)

if result != -1:  
    print("Element is present at index", str(result))  
else:  
    print("Element is not present in list1")  

