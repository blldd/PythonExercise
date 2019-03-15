# -*- coding:UTF-8 -*-

flag = True
nums = []
while flag:
    input_num = raw_input("Enter a number:")
    # print input_num
    # print int(input_num)
    # print type(input_num)
    if input_num.isdigit():
        nums.append(int(input_num))
    else:
        flag = False

# print nums
nums = sorted(nums)
print nums
length = len(nums)
# print length
if length % 2 == 0:
    print (nums[length//2-1] + nums[length//2]) / 2.0
else:
    print nums[length//2]