# User authentication

def register():
  name=input("Enter Your Name:")
  email=input("Enter Your Email:")
  password=input("Enter Your Password:")

  with open("users.txt","a") as f:
    f.write(f"{name},{email},{password}\n")
  print("Account successfully created!\n")

def login():
  email_login=input("Enter your email:")
  password_login=input("Enter password:")

  with open("users.txt","r") as f:
    lines=f.readlines()
  for line in lines:
    name,email_saved,password_saved=line.strip().split(",")
    if(email_login==email_saved and password_login==password_saved):
      print(f"Welcome {name}\n")
      return
  print("Invalid Credentials!\n")
