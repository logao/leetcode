from typing import List


# 给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1
# 成为一个有序数组。

# 说明：
# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
# 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。

# 示例：
# 输入：
# nums1 = [1,3,6,0,0,0], m = 3
# nums2 = [2,5,7],       n = 3
# 输出：[1,2,2,3,5,6]

class Solution:

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1_copy = nums1[:m]
        a = id(nums1)

        nums1[:] = []
        b = id(nums1)
        nums1 = []
        c = id(nums1)

        # 两个指针
        p1 = 0
        p2 = 0

        # 比较排序
        while p1 < m and p2 < n:
            if nums1_copy[p1] < nums2[p2]:
                nums1.append(nums1_copy[p1])
                p1 += 1
            else:
                nums1.append(nums2[p2])
                p2 += 1
        # 处理剩余数据
        if p1 < m:
            nums1[p1 + p2:] = nums1_copy[p1:]
        if p2 < n:
            nums1[p1 + p2:] = nums2[p2:]
        print(nums1)

    def merge1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[:] = sorted(nums1[:m] + nums2)
        print(nums1)
        #
        # i = 0
        # j = 0
        # k = None
        # while j < n and i < m:
        #     if nums1[i] <= nums2[j]:
        #         i += 1
        #     else:
        #         k = nums1[i]
        #         nums1[i] = nums2[j]
        #
        #     j += 1


# test
r = Solution()
print(r.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
