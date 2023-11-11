class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero, curridx, two = 0, 0, len(nums) -1

        while curridx <= two:
            if nums[curridx] == 0:
                nums[zero], nums[curridx] = nums[curridx], nums[zero]
                curridx += 1
                zero += 1
            elif nums[curridx] == 2:
                nums[two], nums[curridx] = nums[curridx], nums[two]
                two -= 1
            else:
                curridx += 1
