
# # 15. 3Sum
# nums = [-1,0,1,2,-1,-4]
# ans = []
# for i in range(len(nums)-2):
#     j = i + 1; k = j + 1
#     while k <= len(nums) - 1:
#         if nums[i] + nums[j] + nums[k] == 0:
#             ans.append([nums[i], nums[j], nums[k]])
#         if (j == len(nums)-2) and (k == len(nums)-1):
#             break
#         elif (k == len(nums)-1):
#             j += 1; k = j + 1
#         else:
#             k += 1
# print(ans)


# nums = [3, 2, 4]
# nums.sort()
# target = 6
# ans = []

# left = 0; right = len(nums) - 1
# while left < right:
#     current_sum = nums[left] + nums[right]
#     if current_sum == target:
#         ans.append(left); ans.append(right)
#         break
#     elif current_sum < target:
#         left +=  1
#     else:
#         right -= 1
# print(ans)


height = [0,1,0,2,1,0,1,3,2,1,2,1]
# def ar(height):
#     left = 0; right = len(height) - 1; elev = 0
#     area = 0
#     while elev <= max(height):
#         cnt = 0
#         while height.count(elev) < 2:
#             cnt += height[elev]
#             elev += 1
#             if elev > max(height):
#                 return area
#         while height[left] < elev+1:
#             left += 1
#         while height[right] < elev+1:
#             right -= 1
#         check = len([i for i in height[left:right+1] if i <= elev])
#         area = area + check
#         elev += 1
#     return area
# print(ar(height))


if len(height) < 3:
    ans = 0

left, right = 0, len(height) - 1
left_max = right_max = water = 0

while left < right:
    if height[left] < height[right]:
        if height[left] >= left_max:
            left_max = height[left]
        else:
            water += left_max - height[left]
        left += 1
    else:
        if height[right] >= right_max:
            right_max = height[right]
        else:
            water += right_max - height[right]
        right -= 1

ans = water
print(ans)