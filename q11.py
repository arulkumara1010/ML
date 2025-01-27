raining = input().strip().lower()  # "yes" or "no"
temperature = int(input().strip())  # Temperature in Celsius

if raining == "yes" and temperature < 30:
    print("Take an umbrella.")
elif raining == "no" and temperature >= 20:
    print("No need for an umbrella.")
else:
    print("Check the weather again.")
