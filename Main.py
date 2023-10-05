# Ask the user to enter a year
year = int(input("Enter a year: "))

# Check if the year is divisible by 4
if year % 4 == 0:

  # Check if the year is divisible by 100
  if year % 100 == 0:

    # Check if the year is divisible by 400
    if year % 400 == 0:
      print(f"{year} is a leap year")
    else:
      print(f"{year} is not a leap year")
  else:
    print(f"{year} is a leap year")
else:
  print(f"{year} is not a leap year")
