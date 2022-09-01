#Basic Operations performed on a lists

ages = [19,22,19,24,20,25,26,24,25,24]

#Sorting the list
ages.sort()
print(ages)

#finding maximum element in the list
maximum = max(ages)
print("Maximum Element is " , maximum)

#finding minimum element in the list
minimum = min(ages)
print("Minimum Element is " , minimum)

#Adding max age to the list
ages.append(maximum)
print("After Adding maximum element : ",ages)

#Adding min age to the list
ages.append(minimum)
print("After Adding maximum element : ",ages)

#median in a list
if len(ages) % 2 != 0 :
    median = ((len(ages) + 1) /2-1)
else:
    m1 = int(len(ages)/2 - 1)
    m2 = int(len(ages)/2)
    median = (ages[m1] + ages[m2]) / 2

print("The median is : " , median)

#printing average of the ages
print("The average is: ", sum(ages) / len(ages))

#printing range of ages
print("The range is : " , max(ages) - min(ages))