def addHotelorRestaurants():
  num=input("Enter spot number to add a hotel or Restaurant")
  name=input("Enter hotel or restaurant name:").strip()
  if(name==""):
    print("Invalid Credentials!")
    return
  

  with open("hotels&Restaurant.txt","a") as f:
    f.write(f"{num},{name}\n")
  print(f"Hotels/Restaurant")