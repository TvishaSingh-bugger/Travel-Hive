def addHotel():
  name=input("Enter Hotel Name:")
  location=input("Enter Hotel location:")
  rating=input("Enter hotel rating(1-5):")

  with open("hotels.txt","a") as f:
    f.write(f"{name},{location},{rating}\n")
  print("Hotel added successfully!")


def viewHotels():
  try:
    with open("hotels.txt","r") as f:
      for line in f:
        nm,loca,rate=line.strip().split(",")
        print(f"Hotel:{nm}\nLocation:{loca}\nRating:{rate}\n")
  except:
    print("File not found!")

def searchHotel():
  search=input("Enter the hotel name to search:")
  found=False
  try:
    with open("hotels.txt","r") as f:
      for line in f:
        nm,loca,rate=line.strip().split(",")
        if search in nm:
          print(f"Hotel:{nm}\nLocation:{loca}\nRating:{rate}\n")
          found=True
    if not found:
      print("No such Hotel name found!")
  except:
    print("No file found!")
