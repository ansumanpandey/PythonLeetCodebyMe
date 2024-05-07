class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        result= False
        count=0
        a=set(nums)
        for i in range(len(nums)-2):
            if nums[i]>nums[i+1] or nums[i]==nums[i+1]:
                i=i+1
            elif len(a)<3:
                break;
            else:
                    for j in range(i+1,len(nums)-1):
                        if j<len(nums)-1:
                            if nums[i]<nums[j]:
                                for k in range(j+1, len(nums)):
                                    if nums[j]<nums[k]:
                                        count=count+1
            if count>=1:
                result=True
                break;                                                                
        return result
