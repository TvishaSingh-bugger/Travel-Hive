def register():
  username=input("Enter your username:")
  password=input("Enter your password:")

  with open("users.txt","a") as f:
    f.write(f"{username},{password}\n")

  print("Registration successful!")


def login():
  username=input("Enter your username:")
  password=input("Enter your password:")

  try:
    with open("users.txt","r") as f:
      for line in f:
        userName,passWord=line.strip().split(",")
        if userName==username and passWord==password:
          print(f"Successfully logged in!")
          return username
    print("Invalid Credentials!")
    return None
  except:
    print("No user found!")
    return None
