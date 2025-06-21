<<<<<<< HEAD
print("Hello! Please Register!")
while True:
    nickname = input("Name~> ")
    password = input("Password~> ")
    with open('db.txt', 'r') as file:
        content = file.read()
    if f"{nickname} {password}" in content:
        print("Successful Login")
        input("Press ENTER to exit...")
        break
    else:
        print("Incorrect Name or Password")
=======
print("Hello! Please Register!")
while True:
    nickname = input("Name~> ")
    password = input("Password~> ")
    with open('C:/pj/Python/db.txt', 'r') as file:
        content = file.read()
    if f"{nickname} {password}" in content:
        print("Successful Login")
        input("Press ENTER to exit...")
        break
    else:
        print("Incorrect Name or Password")
>>>>>>> 136c7ff90a84c0d69493b0654692f38e85e31b4e
        continue