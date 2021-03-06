n = int(input("unesite neki broj "))

deset = n//10  

n = n - deset * 10

petice = n//5

n = n - petice *5

dvice = n//2

n = n -dvice * 2

jedinice = n//1

n = n -jedinice *1

print(deset, petice, dvice, jedinice) 