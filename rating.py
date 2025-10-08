def addRating(spot_num):
    try:
        rating = int(input("Enter your rating (1-5): ").strip())
        if (rating < 1 or rating > 5):
            print("Invalid rating!")
            return
    except ValueError:
        print("Invalid input!")
        return
    with open("ratings.txt", "a") as f:
        f.write(f"{spot_num}:{rating}\n")
    print(f"Rating {rating} added successfully for spot {spot_num}!")
