# 27. 移除元素
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        # 定义一个指针，指向列表的最后一个元素
        end = len(nums) - 1
        # 定义一个指针，指向列表的第一个元素
        i = 0
        # 当i指针小于等于end指针时，循环执行
        while i<= end :
            # 如果i指针等于end指针，说明已经遍历完整个列表
            if i == end:
                # 如果最后一个元素等于val，将end指针减1
                if nums[i] == val:
                    end = end - 1
                # 跳出循环
                break
            # 如果当前元素等于val，将最后一个元素赋值给当前元素，并将end指针减1
            if nums[i] == val: 
                nums[i] = nums[end]
                end = end - 1

            else:
                i = i + 1

        return end + 1
nums = [3,2,2,3]
val = 3

Solution.removeElement(None,nums,val)
print(nums)