#Search and rotated array unique elements
#num[] [7,8,9,1,2,3,4,5,6] target=1 then o/p [1,2,3,4,5,6,7,8,9] 

#Linear search O(N) 
#Binary search n,n/2,n/4 but we cannot take this here because 2<8 where 8 is in the left handside
# So here we need to identify the sorted array 




def search(arr, k):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == k:
            return mid

        # Check if the left half is sorted
        if arr[low] <= arr[mid]:
            if arr[low] <= k <= arr[mid]:
                high = mid - 1  # Search in the left half
            else:
                low = mid + 1   # Search in the right half
        # Otherwise, the right half must be sorted
        else:
            if arr[mid] <= k <= arr[high]:
                low = mid + 1  # Search in the right half
            else:
                high = mid - 1  # Search in the left half

    return -1  # Element not found

