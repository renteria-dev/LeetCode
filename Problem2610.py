class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        histogram=[0]*201 
        maximum=0
        result=[]
        #Histogram of nums
        for num in nums:
            histogram[num]+=1
            maximum= max(maximum,histogram[num])
        #creation of empty list
        for i in range(maximum):
            result.append([])
        #Filling the lists
        for num in nums:
            if histogram[num]>0:
                result[histogram[num]-1].append(num)
                histogram[num]-=1
        return result
