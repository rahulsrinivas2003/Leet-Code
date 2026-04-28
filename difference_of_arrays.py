class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        o1 = []
        o2 = []
        answer = []

        for num in nums1:

            if num not in nums2:

                o1.append(num)
        
        for num in nums2:

            if num not in nums1:

                o2.append(num)
        
        answer.append(o1)
        answer.append(o2)

        return answer