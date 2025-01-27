knowledge_base = {"Japan": "Tokyo", "Canada": "Ottawa", "France": "Paris"}

while True:
    option = int(input().strip())
    
    if option == 1:  # Query Capital
        country = input().strip()
        capital = knowledge_base.get(country, "Unknown")
        print(capital)
    elif option == 2:  # Add Country-Capital Pair
        country = input().strip()
        capital = input().strip()
        knowledge_base[country] = capital
        print(f"Added successfully: {country} - {capital}")
    elif option == 3:  # Exit Program
        break
