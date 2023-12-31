# VendingMachine

## REQUIREMENT  
  
- Create a traditional vending machine logic in Python
- A vending machine that sells drink and snacks
- Each item in the menu has its own respective price
- Only accepts cash, cents not accepted (Only whole number allowed, no decimals)
- Return customer least amount of note(s), if any  

- For example:  
    - $5 coffee  
    - $100 payment  
    - $95 change/balance  

    Return note(s):
     - 1 * $50 note  
     - 2 * $20 note  
     - 1 * $5 note  
  
  
## HOW TO:  
  
- You may add items in the MENU as according to your preference following the existing format  
- You may change the Currency to suit your preference (e.g: USD, SGD, RM, AUD)  
- Run command "python vendingMachine.py" to start ordering
- You will be prompted "Order: ", place your order(s), you may repeat your order(s)
- Once order completed, you may proceed to checkout and make payment
    - To checkout:
        - Type "checkout()" in "Order: "
        - MAC/Unix: CTRL + C
        - Windows: [ CTRL + Z ], then ENTER
    
- After checkout, you will be prompted "Payment: "
    - Type the amount you want to pay
    - If still owing, continue feeding payment into the machine until amount owed is less than or equal 0.
    - You are not allowed to cancel payment halfway through

- Once payment is complete, it will return the least number of notes, if there is any change/balance.
  
  
Expected output:  
  
![Alt text](image.png)