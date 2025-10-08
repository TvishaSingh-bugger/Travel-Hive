def addReview(num):
  name=input("Enter Your Name:")
  review=input("Enter Your Review:")
  if(review==""):
    print("No review!")
    return
  with open("Reviews.txt","a") as f:
    f.write(f"{num}:{name}:{review}\n")
  print("Review added Successfully!")


def viewReview(num):
  with open("Reviews.txt","r") as f:
    lines=f.readlines()
  print(f"Review for spot {num}")
  found=False
  for line in lines:
    line_part=line.strip().split(":",2)
    number,name,review=line_part
    if(str(num)==number):
      print(f"{name}:{review}")
      found=True


  if not found:

    print("No reviews!")

    
     

  

  