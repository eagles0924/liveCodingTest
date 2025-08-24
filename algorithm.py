#%%
# 15. 3Sum
nums = [-1,0,1,2,-1,-4]
ans = []
for i in range(len(nums)-2):
    j = i + 1; k = j + 1
    while k <= len(nums) - 1:
        if nums[i] + nums[j] + nums[k] == 0:
            ans.append([nums[i], nums[j], nums[k]])
        if (j == len(nums)-2) and (k == len(nums)-1):
            break
        elif (k == len(nums)-1):
            j += 1; k = j + 1
        else:
            k += 1
print(ans)

#%%
nums = [3, 2, 4]
nums.sort()
target = 6
ans = []

left = 0; right = len(nums) - 1
while left < right:
    current_sum = nums[left] + nums[right]
    if current_sum == target:
        ans.append(left); ans.append(right)
        break
    elif current_sum < target:
        left +=  1
    else:
        right -= 1
print(ans)
# %%
