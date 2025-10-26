from authentication import register,login
from spots import addSpot,viewSpot,searchSpot
from reviews import addReview,viewReview
from quesAns import askQues,ansQues,viewQuestion
from hotels import addHotel,viewHotels,searchHotel



currentUser=None
while True:
  print("Tourist Spot Review System")
  print("1.Register")
  print("2.Login")
  print("3.Add Spot")
  print("4.View Spot")
  print("5.Search Spot")
  print("6.Add Review")
  print("7.View Reviews")
  print("8.Ask Questions")
  print("9.View Questions")
  print("10.Add Answer to Question")
  print("11.Add Hotel")
  print("12.View Hotel")
  print("13.Search Hotel")
  print("14.Exit")

  choice=input("Enter your choice(1-14):")
  if choice=="1":
    register()
  elif choice=="2":
    currentUser=login()
  elif choice=="3":
    addSpot()
  elif choice=="4":
    viewSpot()
  elif choice=="5":
    searchSpot()
  elif choice=="6":
    if currentUser:
      addReview(currentUser)
    else:
      print("You are not logged in!")
  elif choice=="7":
    viewReview()
  elif choice=="8":
    if currentUser:
      askQues(currentUser)
    else:
      print("You are not logged in")
  elif choice=="9":
    viewQuestion()
  elif choice=="10":
    ansQues()

  elif choice=="11":
    addHotel()
  elif choice=="12":
    viewHotels()
  elif choice=="13":
    searchHotel()
  elif choice=="14":
    print("Exiting..")
    break
  else:
    print("Invalid choice!")
        elif choice=="7":
            print("Logging Out...\n")
            break
        else:

            print("Invalid choice! Try again.")
