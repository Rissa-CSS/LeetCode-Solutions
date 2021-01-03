class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
         #List that stores the answer
        self.answer =[]
        # Loops through the list of numbers 
        for i in range(len(nums)):
            #Loops through the list of numbers starting from the number next to
            # the number the outer loop.
            for j in range(1,len(nums)):
                # Checks if the two numbers are equal to the target
                # not equal to each other and not already in the list
                if ((nums[i] + nums[j]) == target) & (i != j)&(i not in self.answer) & (j not in self.answer):
                    #Adds the two numbers to the list
                    self.answer.append(i)
                    self.answer.append(j)
        # Returns answer list             
        return self.answer
    
def main():
    nums = [3,3]
    target = 6
    # calls the function
    print(Solution.twoSum(nums,target))
    
        
        
