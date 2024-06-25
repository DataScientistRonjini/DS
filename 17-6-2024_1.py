# Container with most water
height=[4,7,5,10]
i=0
j=len(height)-1
max_area=0
while i<j:
    short_height=min(height[i],height[j])
    area=short_height*abs(i-j)
    max_area=max(max_area,area)
    if height[i]<height[j]:
        i+=1
    else:
        j-=1
print(max_area)

