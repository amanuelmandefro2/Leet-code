class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i = 0
        j = 0
        ans = []
        while i < len(nums1) and j < len(nums2):
            if nums2[j] > nums1[i]:
                i += 1
            elif nums2[j] < nums1[i]:
                j += 1
            else:
                ans.append(nums1[i])
                j += 1
                i += 1
        return ans                 
        