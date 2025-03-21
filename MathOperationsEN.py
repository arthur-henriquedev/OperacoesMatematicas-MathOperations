#Data collection
while True: 
    value_a = int(input("Type the value a: "))
    value_b = int(input("Type the value b: "))

#Logic operations
    addition = value_a + value_b
    subtraction = value_a - value_b    
    multiplication = value_a * value_b   
    division = value_a / value_b

#Confirmação de valores
    print("The values are: ", value_a, " e ", value_b)
    
    continuation = input("Do you want to continue with these values? (Y/N): ").strip().upper()

#Mathematical process  
    if continuation == "Y": 
        while True:  
            print("Choose a mathematical operator (+, -, *, /):")
            operation = input().strip()

            if operation == "+":
                print("The result is: ", addition)
                break  
            elif operation == "-":
                print("The result is: ", subtraction)
                break
            elif operation == "*":
                print("The result is: ", multiplication)
                break
            elif operation == "/":
                print("The result is: ", division)
                break
            else:
                print("Invalid input, insert a valid mathematical operator (+, -, *, /):")

         
    elif continuation == "N": 
        print("Reinsert new values.")
        continue