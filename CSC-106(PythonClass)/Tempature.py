#use a while loop to loop the code and it may be helpful in updating our code in the future
while True:
    #here we ask what the tempature and age are of the patient
    temp = float(input("What is your temperature? "))
    age = str(input("Is the patient an Adult, Child or Baby? "))
    #checking the tempature and age and producing a result
    if (temp <= 95):
        print("Hypothermia - SEEK CARE")
        #we break so that the code does not loop again
        break

    elif (temp >= 95.1 and temp <= 96.9):
        print("Low but possible normal")
        break

    elif (temp >= 95.1 and temp <= 96.9) and (age == "Baby"):
        print("Low - SEEK CARE")
        break

    elif (temp >= 97.0 and temp <= 98.6):
        print("Normal")
        break

    elif (temp >= 98.6 and temp <=100.4):
        print("Normal or low grade fever")
        break

    elif (temp >= 98.6 and temp <=100.4) and (age == "Baby"):
        print("Low grade fever")
        break

    elif (temp >= 100.4 and temp <= 103):
        print("Fever")
        break

    elif (temp >= 100.4 and temp <= 103) and (age == "Baby"):
        print("Fever - SEEK CARE")
        break

    elif (temp >= 103):
        print("High fever - CALL YOUR DOCTOR")
        break

    elif (temp >= 103) and (age == "Baby"):
        print("High fever - SEEK CARE")
        break

    else:
        print("Try again")
        break