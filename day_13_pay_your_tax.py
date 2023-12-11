# Day 13, Pay your Tax

def your_vat():
    while True:
        try:
            usr_input_price = int(input("Enter the price of the item: ")) 
            usr_input_vat = int(input("Enter the VAT amount as a %: "))

            if usr_input_price > 0 and usr_input_vat > 0:
                vat_price = usr_input_price + (usr_input_price * (usr_input_vat/100))
                return vat_price
            else:
                print("Enter a positive intger value")
        except ValueError:
            print("Enter a positive number")

func_call = your_vat()
print(func_call)

# Extra Challenge: Pyramid of Snakes

def python_snakes(num):
    snake = "🐍"

    for i in range(num):
        snake_emoji = snake * (1 * i + 1)
        print(snake_emoji)

python_snakes(7)