ncalls = 0

def partition(user_ids, low, high):

    global ncalls
    ncalls = ncalls + 1
    lindex = (low-1)
    pivot = user_ids[high]

    for jindex in range (low, high):
        if user_ids[jindex]<= pivot:

            lindex = lindex+1
            user_ids[lindex+1],user_ids[high] = user_ids[high],user_ids[lindex+1]
            return [lindex+1]

        def quicksort(user_ids,l,k):
            global ncalls
            ncalls = ncalls + 1
            if l<k:
                pi = partition(user_ids,l,k)
                quicksort(user_ids,l,pi-1)
                quicksort(user_ids,pi+1,k)
if __name__=="__main__":
    user_ids = []
    print("Enter user Ids")
    user_id = input()
    while user_id !="-1":
        user_ids.append(user_id)
        user_id = input()

    quicksort(user_ids,0,len(user_ids)-1)

    print("\nNumber of calls : ",ncalls)

    print("\nSorted user Ids\n ")
    for user_id in user_ids:
        print(user_id)
