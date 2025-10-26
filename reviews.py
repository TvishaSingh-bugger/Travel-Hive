def addReview(currentUser):
  spot=input("Enter the spot name you want to review:")
  review=input("Write your review:")
  rating=int(input("Enter your rating(1-5):"))

  if rating<1 or rating>5:
    print("Invalid Rating!")
    return
  
  with open("reviews.txt","a") as f:
    f.write(f"{spot},{currentUser},{review},{rating}\n")
  print("Review added successfully!")


def viewReview():
  try:
    with open("reviews.txt","r") as f:
      reviews=f.readlines()
    if not reviews:
      print("File is empty,No reviews!")
      return
    for review in reviews:
      place,user,r,rate=review.strip().split(",")
      print(f"Spot:{place}\nReviewBy:{user}\nComment:{r}\nRating:{rate}\n")
  except:
    print("No reviews found!")
    return None
