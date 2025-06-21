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
        continue