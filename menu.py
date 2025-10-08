from authentication import register,login
from touristspot import addPlaces,viewPlaces
from hotelsAndrestaurants import addHotelorRestaurants
from review import addReview,viewReview
from rating import addRating
def main_menu():
    while True:
        print("Tourist Spot Review System\n")
        print("1. Register\n")
        print("2. Login\n")
        print("3. Exit\n")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            register()
        elif choice == "2":
            if login():
                user_dashboard()
        elif choice == "3":
            print("Exiting system...")
            break
        else:
            print("Invalid choice! Try again.")
def user_dashboard():
    while True:
        print("1. View Tourist Spots\n")
        print("2. Add Tourist Spot\n")
        print("3. Add Hotel/Restaurant\n")
        print("4. Add Review\n")
        print("5. View Reviews\n")
        print("6. View Ratings\n")
        print("7. Logout")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            viewPlaces()
        elif choice == "2":
            addPlaces()
        elif choice == "3":
            addHotelorRestaurants()
        elif choice == "4":
            viewPlaces()
            num = input("Enter Spot Number to review: ").strip()
            addReview(num)
        elif choice == "5":
            num = input("Enter Spot Number to view reviews: ").strip()
            viewReview(num)
        elif choice == "6":
            num = input("Enter Spot Number to view reviews: ").strip()
            addRating()
        elif choice=="7":
            print("Logging Out...\n")
            break
        else:
            print("Invalid choice! Try again.")