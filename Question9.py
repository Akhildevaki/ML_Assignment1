#converting lbs into kilograms

lst=[]
n = int(input("Enter number of students :"))

for i in range(0,n):
    m = int(input())

    lst.append(m)

print(lst)

kgs = []

for i in lst:
    kgs.append(i*0.453592)

print("Output : "  ,kgs)