def addSpot():
  spotName=input("Enter the name of the spot:")
  location=input("Enter the location:")
  category=input("Enter category (Hill,Temple,Beach,etc.):")
  description=input("Enter short description:")
  
  with open("spots.txt","a") as f:
    f.write(f"{spotName},{location},{category},{description}\n")
  print("Spot added successfully!")

def viewSpot():
  try:
    with open("spots.txt","r") as f:
      spots=f.readlines()
    if not spots:
      print("No spots found!")
      return
    for spot in spots:
      place,loca,cat,des=spot.strip().split(",",3)
      print(f"Spot:{place}\nLocation:{loca}\nCategory:{cat}\nDescription:{des}\n")
  except:
    print("No spots found")

def searchSpot():
  place=input("Enter spot to search:")
  try:
    with open("spots.txt","r") as f:
      spots=f.readlines()
    found=False
    for spot in spots:
      if place in spot:
        print(spot.strip())
        found=True
    if not found:
      print("No match found!")
  except:
    print("No spots found!")
