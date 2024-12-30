card_num = ["2345 4558 9875 3576", "1000 2000 3000 5000", "0987 3456 7653 1234", "6789 2344 6758 1986", "4987 4355 2345 0957"]
pin = [1234, 5678, 2340, 9870, 9999]
balance =[170.00,150.00,100.00,100.00,100.00]

def old_user():
    is_valid = False
    card_ver = input("Please enter your card number: ")
    pin_ver = int(input("Now enter your pin code: "))
    for i in range(len(card_num)):
        if card_ver == card_num[i]  and pin_ver == pin[i]:
            j = i
            print("Success, you have logged in successfully")
            while True:
                process = input("Enter d to make a deposit, b to check account balance, w to withdraw, or q to quit: ") 
                if process == "d":
                    deposit = float(input("How much would you like to deposit: "))
                    balance[j] += deposit
                    print(deposit, "was added to your balance.")
                    print("New balance:", balance[j])
                elif process == "b":
                    print("Your account balance is", balance[j])
                elif process == "w":
                    withdraw = float(input("How much do you want to withdraw? "))
                    if withdraw <= balance[j]:
                        balance[j] -= withdraw
                        print("Amount withdrawn:", withdraw, "New balance:",balance[j] )
                    else:
                        print("Insufficient funds.")
                elif process == "q":
                    break
                else:
                    print("Invalid input")
            is_valid = True
            break 
    if not is_valid:
        print("Sorry, your card number or pin is incorrect. Try again ")

print ("Welcome to Paddys ATM Machine System")
user = input ("Enter l to login or c to create an account with us: ")

if user == "l":
    old_user()

elif user == "c":
    print("Answer the questions to create an account ")
    f_name = input("Enter your first name: ")
    l_name = input("Enter your last name: ")
    dob = input("Enter the first digit of birth month, first digit of day and last two digits of year i.e if DOB is 12/17/2003, enter 1103")
    new_card = "0000 1234 4567 "+ dob
    new_pin  = int(input("Enter a 4-digit pin: "))
    print("Congrats!", f_name, "your account with card number", new_card, "has been created.")
    card_num.append(new_card)
    pin.append(new_pin)
    balance.append(0.00)
    old_user()

        

   

        
    

