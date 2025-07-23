#leetcode
#1695. Maximum Erasure Value
#link:https://leetcode.com/problems/maximum-erasure-value/description/
#T.C : O(n)
#S.C : O(1)

nums = [4,2,4,5,6]

n = len(nums)

i = 0
j = 0
total = 0
result = 0

st = set()

while j < n:
    if nums[j] not in st:
        total += nums[j]
        st.add(nums[j])
        result = max(result, total)
        j += 1
    else:
        while i < n and nums[j] in st:
            st.remove(nums[i])
            total -= nums[i]
            i += 1

print(result)
