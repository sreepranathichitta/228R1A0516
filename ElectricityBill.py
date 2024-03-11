
units = float(input("Enter the Units: "))
if units > 0 and units <= 100:
    payment = units * 1.5
    fixedCharge = 25
elif units > 100 and units <= 200:
    payment = (100 * 1.5) + (units - 100) * 2.5
    fixedCharge = 50
elif units > 200 and units <= 300:
    payment =  (100 * 1.5) + (200 - 100) * 2.5 + (units - 200) * 4
    fixedCharge = 75
elif units > 300 and units <= 350:
    payment = (100 * 1.5) + (200 - 100) * 2.5 + (300 - 200) * 4 + (units - 300) * 5
    fixedCharge = 100
else:
    payment = 0
    fixedCharge = 1500

total = payment + fixedCharge

print(f"Your Electricity Bill amount is {total:.2f}")