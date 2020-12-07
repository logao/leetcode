from typing import List


# 原地算法
# 在计算机科学中，一个原地算法（in-place algorithm）是一种使用小的，固定数量的额外之空间来转换资料的算法。
# 当算法执行时，输入的资料通常会被要输出的部份覆盖掉。不是原地算法有时候称为非原地（not-in-place）或不得其所（out-of-place）。

# 给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
# 不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

# 示例 1:
# 给定数组 nums = [1,1,2],
# 函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。
# 你不需要考虑数组中超出新长度后面的元素。

# 示例 2:
# 给定 nums = [0,0,1,1,1,2,2,3,3,4],
# 函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。
# 你不需要考虑数组中超出新长度后面的元素。

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        i = 0
        j = i + 1
        while j < len(nums):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
            j += 1
        i += 1
        return i

    def removeDuplicates3(self, nums: List[int]) -> int:
        res = len(nums)
        for i, v in enumerate(nums):
            j = i + 1
            while j < res:
                if nums[j] == v:
                    self.reRanage(nums, j, v)
                    res -= 1
                    continue
                j += 1
        print(nums)
        return res

    def reRanage(self, nums: List[int], j: int, v: int):
        k = j
        while k < len(nums) - 1:
            tmp = nums[k]
            nums[k] = nums[k + 1]
            nums[k + 1] = tmp
            k += 1
        nums[k] = v

    def removeDuplicates2(self, nums: List[int]) -> int:
        for i, v in enumerate(nums):
            if v is None:
                continue
            if i == len(nums) - 1:
                break
            j = i + 1
            while j < len(nums):
                if i == j:
                    j += 1
                    continue
                if v == nums[j]:
                    nums[j] = None
                j += 1
        print(nums)
        tmpRes = 0
        for i, v in enumerate(nums):
            if v is None:
                # v,nums[i] is null
                k = i + 1
                while k < len(nums):
                    if nums[k] is None:
                        k += 1
                        continue
                    else:
                        nums[i] = nums[k]
                        nums[k] = None
                        break
            if nums[i] is not None:
                tmpRes += 1
            else:
                break
        return tmpRes


# test
res = Solution()
result = res.removeDuplicates([1, 1, 1])
print(result)
