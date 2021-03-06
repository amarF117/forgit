user = 1

admin = 2 

superAdmin = 4 

authorizationMask = admin | superAdmin 

userrole = int(input("enter role"))

print("you are in :" , (authorizationMask & userrole )) !=0 
