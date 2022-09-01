it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#length of the set it_companies
print("length of the set it_companies is : ", len(it_companies))

#adding "twitter" to the ser it_companies
it_companies.add("twitter")
print(it_companies)

#adding multiple elements to the set
companies = {"cognizant","tata","tcs"}
it_companies.update(companies)
print("After adding multiple companies : ", it_companies)

#difference between remove and discard
#remove funtion throws an error if the specified item is not in the set
#discard funtion doesn't throw any error and the set remains unchanged

#Join A and B
print(A.union(B))

#Intersection of A and B
print(A.intersection(B))

#Is A Subset of B
print(A.issubset(B))

#Are A and B disjoint sets
print(A.isdisjoint(B))

#Join A with B and B with A
print(B.union(A))
print(A.union(B))

#Symmetric difference between A and B
print(A.symmetric_difference(B))

#Deleting all the elements in set it_companies
set.clear(it_companies)
print(it_companies)

#Deleting all the elements in set A
set.clear(A)
print(A)

#Deleting all the elements in set B
set.clear(B)
print(B)

#Converting the list of ages to set
ages_set = set(age)
print(ages_set)

#Compare the length of the list and set
length_list = len(age)
length_set = len(ages_set)

if(length_list == length_set):
    print("length is same")
else:
    print("length is not same")