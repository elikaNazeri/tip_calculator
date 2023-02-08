print("welcome to the tip calculator ")
bill = int(input("what was the total bill? "))
tip = int(input("how much tip would you like to give? "))
people = int(input("how many people to split the bill?"))

tip_percent = tip / 100
total_bill = ( bill * (1 + tip_percent ) )
portion = (total_bill / people)


print("each person should pay: ",portion )
