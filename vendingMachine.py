import math

currency = "$"

def main():

    menu = {
        "Coke": 5.00,
        "Sprite": 3.00,
        "Pepsi": 15.00,
        "Mountain Dew": 13.00,
        "Lipton Tea": 11.00,
        "Minute Maid": 12.00,
        "Tropicana": 19.00,
        "Nescafe": 3.00,
        "Snickers": 6.00,
        "Mars": 9.00,
        "Oat25": 8.00,
        "Gatorade": 7.00,
        "100 Plus": 4.00,
        "7 Up": 4.00,
        
    }
    
    total = 0

    print('WELCOME TO GIONET VENDING MACHINE!')
    
    while True:
        try:
            userInput = str(input('Order: ')).title()
            
        except EOFError:
            break
        
        except KeyboardInterrupt:
            return
        
        if userInput.lower() == 'checkout()':
            break
        
        if userInput in menu:
            price = menu[userInput]
            total += price
            print(f'Total: {currency}{total:.2f}')
        
        else:
            print("Item not in list, please try again!")
    
    while True:
        if total <= 0:
            break
        
        try:
            # Calculate change 
            payment = int(input(f'Payment: {currency}'))
            
            if payment > 0:
                total -= payment
                print(calculate_change(total))

        # Only accept whole number
        except ValueError:
            print('Please insert a valid whole number.')
        
        # Order cancel after checkout
        except EOFError:
            print('You have not complete the payment!')
            continue
        
        except KeyboardInterrupt:
            print('')
            print('Order canceled, thank you.')
    
    least_notes_calculation_greedy(total)
    print('Thank you, please come again!')

# Greedy method (exhuasting largest to smallest)
def least_notes_calculation_greedy(amount):
    number_of_notes = {}
    notes = [100, 50, 20, 10, 5, 1]
    
    remaining_amount = amount * -1
    
    for i in notes:
        notes_count = remaining_amount // i
        number_of_notes[f"{i}"] = int(notes_count)
        remaining_amount -= notes_count * i
            
    for a, b in number_of_notes.items():
        print(f"{currency}{a}: {b}")

# Calculate change
def calculate_change(total):
    change = total * -1
    return f"Change: {currency}{change:.2f}" if total < 0 else f"Remaining: {currency}{total}"


if __name__ == '__main__':
    main()
    
    
