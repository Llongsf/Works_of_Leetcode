# 盛水最多的容器
height = [1,8,6,2,5,4,8,3,7]
# s代表面积
i = 0
j = len(height) - 1
s = 0
while i < j:
    if height[i] < height[j]:
        s = max(s,height[i]*(j-i))
        i+=1
    else:
        s = max(s,height[j]*(j-i))
        j-=1
print(s)