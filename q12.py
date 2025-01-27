location = input().strip().lower()  # "home" or "school"
lunch_prepared = input().strip().lower()  # "yes" or "no"

if location == "home":
    print("You can have lunch at home.")
elif location == "school":
    if lunch_prepared == "yes":
        print("Bring your lunch.")
    elif lunch_prepared == "no":
        print("Buy lunch at school.")
else:
    print("Check your location and lunch status.")
