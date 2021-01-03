class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Joins the two sorted arrays and sort them again
        nums1 += nums2
        nums1.sort()
        
        # Checks if the length of the list is even or odd
        if (len(nums1))%2 !=0:
            #Finds the median and returns the value at that location
            self.median = (len(nums1))/2
            return nums1[self.median]
        else:
            #Finds the midpoint
            self.median = (len(nums1))/2
            # Returns the average of the midpoint and the value before it 
            return float((nums1[self.median] + nums1[self.median -1]))/2
def main():
    nums1 = [1,2]
    nums2 = [3,4]
    #Calls the function
    print(solution.findMedianSortedArrays(nums1,nums2))
