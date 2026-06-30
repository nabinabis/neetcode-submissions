class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
#else loop throo and add until you get the target?
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return [i,j]



           
