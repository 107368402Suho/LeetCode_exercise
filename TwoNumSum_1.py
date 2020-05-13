'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''

def two_sum(nums, target):
    """这样写更直观，遍历列表同时查字典"""
    dct = {}
    for i, n in enumerate(nums):
        if target - n in dct:         # target - n 不在词典，说明num2没有找到，接着把下标，num1存进词典里。
            return [dct[target - n], i]  # 找到则返回 num1在词典中的value,即下标，和 i 即num2的下标
        dct[n] = i

result = two_sum([2,2,11,15],4)
print(result)