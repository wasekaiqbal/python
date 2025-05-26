'''print("exam eligibility checker")

med_cause=input("did you have any medical cause? \n use Y for yes and \n use N for no \n answer:")

atten = int(input("input the perchentage of your attendence throughout the term: "))

if med_cause == 'Y' :

    print("you are allowed to sit for the exam")
else:
    if atten >= 75:
        print("you are allowed to sit for the exam")
    else:
        print("you are not allowed to sit for the exam")
        '''

print("lets check electricity bill")

#taking units of wlectricity consumed by te user
unit = float(input("enter the amount of units of electricity consumed: "))

#surcharged = extra tax
#for units less than 50, bill = unit*2.60

if unit < 50:
    amount = unit* 2.60
    surcharge = 25

#got between 51-100 , for 1st 50 units, 50*2.60=130
# for this case bill = unit * 3.25

elif unit >= 50 and unit <= 100:
    amount = 130 + ((unit-50) * 3.25)
    surcharge = 35

# for 2nd 50, 50*3.25 = 152.50

elif unit > 100 and unit <= 200:
    amount = 130 + 162.50 + ((unit-100) * 5.26)
    surcharge = 45

else:
    amount = 130 + 162.50 + 526 + ((unit-200) * 8.45)
    surcharge = 75

total = amount + surcharge
print("\n electricty bill = " ,total)
