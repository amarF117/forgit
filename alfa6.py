number = (1,2,3,4,5,6,7,8,9) 

count_odd = 0

count_even = 0

for x in number:
    if not x %2:
        count_even+=1
    else:
        count_odd+=1
print("broj je paran", count_even )
print("broj je neparan ", count_odd)