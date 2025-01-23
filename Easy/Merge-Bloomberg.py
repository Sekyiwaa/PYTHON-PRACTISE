class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in nums1[:m]:
            nums2.append(i)
        
        nums2.sort()

        for i in range(len(nums1)):
            nums1[i] = nums2[i]
        
        print(nums1)

#nums1 = [-1,0,0,3,3,3,0,0,0]
#m = 6

#nums2 = [1,2,2]
#n = 3

#Solution().merge(nums1, m, nums2, n)
        