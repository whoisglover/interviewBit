class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        pivot = self.findPivot(A, 0, len(A)-1)
        if(pivot is -1):
            return self.binarySearch(A, 0, len(A)-1, B)
        if(A[pivot] is B):
            return pivot
        if(A[0] <= B):
            return self.binarySearch(A, 0, pivot-1, B)
        return self.binarySearch(A, pivot+1, len(A)-1, B)

    def findPivot(self, arr, low, high):
        if high < low:
            return -1
        if high is low:
            return low
        mid = (low+high)//2
        if(mid < high and arr[mid] > arr[mid+1]):
            return mid
        if(mid > low and arr[mid] < arr[mid-1]):
            return mid -1
        if(arr[low] >= arr[mid]):
            return self.findPivot(arr, low, mid -1)
        return self.findPivot(arr, mid + 1, high)
    def binarySearch(self, arr, low, high, target):
        if(high < low):
            return -1
        mid = (low + high)//2
        if(arr[mid] is target):
            return mid
        elif(target > arr[mid]):
            return self.binarySearch(arr, mid+1, high, target)
        else:
            return self.binarySearch(arr, low, mid-1, target)




if __name__ == '__main__':
    x =  [4, 5, 6, 7, 7, 0, 1, 2]
    test = [3,4,5,6,1,2]
    test2 = [0,10,22,34,45,51,60]
    target = 4
    z = Solution()
    result = z.findPivot(test, 0, len(test))
    result2 = z.binarySearch(test2, 0, len(test2), 10)
    result3 = z.search(x, 4)
    print(result3)
