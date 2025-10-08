def addPlaces():
    name = input("Enter tourist spot: ").strip()
    if name == "":
        print("No Spot entered!")
        return

    try:
       with open("tourist.txt","r") as f:
          lines=f.readlines()
          num=len(lines)+1
    except FileNotFoundError:
       num=1

    with open("tourist.txt","a") as f:
       f.write(f"{num},{name}\n")
    print(f"Tourist spot '{name}' added successfully")
    

def viewPlaces():
  with open("tourist.txt","r") as f:
    lines=f.readlines()

    print("Tourist Spots in Uttrakhand:\n")
    for line in lines:
      line_part=line.strip().split(",")
      num=line_part[0]
      name=line_part[1]

      print(f"{num}.{name}")
    print()

  
  




