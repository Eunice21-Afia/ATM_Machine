

# **ATM Machine System**  

A Python-based ATM simulation project that allows users to perform essential banking operations such as deposits, withdrawals, and balance checks. The application supports existing users and allows new users to create accounts.  

---

## **Features**  
- **User Authentication**: Validates card numbers and PINs for existing users.  
- **Account Management**: Enables new users to create accounts with a unique card number and PIN.  
- **Banking Operations**:  
  - **Deposit**: Add funds to your account balance.  
  - **Withdrawal**: Withdraw funds, with insufficient balance checks.  
  - **Balance Inquiry**: View the current account balance.  
- **User-Friendly Navigation**: Command-line interface with prompts for each action.  

---

## **How to Use**  

### **1. Login for Existing Users**  
- Enter your card number and PIN.  
- After successful login, choose from the following options:  
  - **Deposit**: Add money to your account.  
  - **Withdraw**: Withdraw money (checks for sufficient funds).  
  - **Balance Inquiry**: View current account balance.  
  - **Quit**: Exit the session.  

### **2. Create a New Account**  
- Enter your first name, last name, and date of birth (used for generating a unique card number).  
- Set a 4-digit PIN.  
- Your new account will have an initial balance of $0.00.  

---

## **Requirements**  
- Python 3.x installed on your machine.  

---

## **How to Run the Application**  
1. Clone or download the repository to your local machine.  
2. Navigate to the project folder.  
3. Run the script using Python:  
   ```bash  
   python atm_project.py  
   ```  
4. Follow the on-screen instructions to interact with the ATM system.  

---

## **Folder Structure**  
```
ATM_Project/
├── atm_project.py   # Main application file
```

---

## **Sample Usage**  

### **Login Example**  
1. Run the program and select "l" to login.  
2. Enter your card number and PIN.  
3. Perform actions like deposits, withdrawals, and balance checks.  

**Example Output:**  
```plaintext  
Welcome to Paddys ATM Machine System  
Enter l to login or c to create an account with us: l  
Please enter your card number: 2345 4558 9875 3576  
Now enter your pin code: 1234  
Success, you have logged in successfully  
Enter d to make a deposit, b to check account balance, w to withdraw, or q to quit: b  
Your account balance is $170.00  
```

### **Create Account Example**  
1. Select "c" to create a new account.  
2. Enter your personal details and set a PIN.  
3. Your account and card number are generated, and you can start using the system.  

**Example Output:**  
```plaintext  
Answer the questions to create an account  
Enter your first name: John  
Enter your last name: Doe  
Enter the first digit of birth month, first digit of day, and last two digits of year (e.g., 12/17/2003 -> 1103): 1223  
Enter a 4-digit pin: 5678  
Congrats! John, your account with card number 0000 1234 4567 1223 has been created.  
```

---

## **Future Enhancements**  
- Support for transferring funds between accounts.  
- Persistent data storage for card numbers, PINs, and balances.  
- GUI-based interface for better usability.  

---

## **Security Note**  
- Card numbers and PINs are stored in memory during the session. Ensure you secure the runtime environment.  
- Future versions will implement encryption for sensitive data.  

