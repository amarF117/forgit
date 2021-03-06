blacklist = ["peter", "jhon", "sally"]
user = []


while True:
    newuser = input("username")
    if newuser in blacklist:
        print("Sorry, you cen not enter")
    else:
        user.append(newuser)
print("current user")
print(users)