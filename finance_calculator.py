import math

def calculate_investment_s(principal, rate, time):
    """This function calculates simple interest"""
    future_value_s = principal*(1+(rate/100)*time)
    return future_value_s

def calculate_investment_c(principal, rate, time):
    """This function calculates the compound interest"""
    future_value_c = principal* math.pow((1+(rate/100)),time)
    return future_value_c

def calculate_bond(principal, rate, time):
    """This function calculates the bond"""
    rate = rate/1200
    time = time*12
    bond_value = (rate * principal)/(1 - (1+rate)**-time)
    return bond_value

def main():
    while True:
        print("=================================================================")
        print("               Thee Deciders Financial Calculator                ")
        print("------------------------------Menu-------------------------------")
        print("=================================================================")
        while True:
            investment_type = input("\nEnter 'I' for investment or 'B' for bond: ")
            if investment_type.upper() == 'I':
                while True:
                    principal_input = input("Enter the principal amount: R ")
                    cleaned_principal_input = principal_input.replace(" ","").strip()
                    if cleaned_principal_input.replace(".","",1).isdigit():
                        principal = float(cleaned_principal_input)
                        break
                    else:
                        print("Invalid input. Enter a valid amount (Numeric)")
                        
                while True:
                        rate_input = input("Enter the annual interest rate (%): ")
                        cleaned_rate = rate_input.replace(" ","").strip()
                        if cleaned_rate.replace(".","",1).isdigit():
                            rate = float(cleaned_rate)
                            if rate <= 100:
                                break
                            else:
                                print("Rate must be equal or less than 100")
                        else:
                            print("Invalid rate. Enter a valid rate.")
                while True:
                    time_input = input("Enter the time period (in years): ")
                    cleaned_time = time_input.replace(" ","").strip()
                    if cleaned_time.replace(".","",1).isdigit():
                        time = float(cleaned_time)
                        break
                    else:
                        print("Invalid input. Enter valid time")

                while True:
                    invest = input("Enter 'S' for Simple interest or 'C' for Compound interest: ")
                    if invest.upper() == 'S':
                        future_value_s = calculate_investment_s(principal, rate, time)
                        print(f"The future value of your investment will be: R{future_value_s:.2f}")
                        break
                        
                    elif invest.upper() == 'C':
                        future_value_c = calculate_investment_c(principal, rate, time)
                        print(f"The future value of your investment will be: R{future_value_c:.2f}")
                        break
                    
                    else:
                        print("Invalid input. Please enter 'S' for Simple interest or 'C' for compound.")

            elif investment_type.upper() == 'B':
                while True:
                    #principal_input = input("Enter the principal amount: R ")
                    #cleaned_principal_input = clean_input(principal_input)
                    principal_input = input("Enter the principal amount: R ")
                    #cleaned_principal_input = clean_input(principal_input)
                    cleaned_principal_input = principal_input.replace(" ","").strip()
                    if cleaned_principal_input.replace(".","",1).isdigit():
                        principal = float(cleaned_principal_input)
                        break
                    else:
                        print("Invalid input. Enter a valid amount (Numeric)")
                        
                while True:
                    rate_input = input("Enter the annual interest rate (%): ")
                    cleaned_rate = rate_input.replace(" ","").strip()
                    if cleaned_rate.replace(".","",1).isdigit():
                        rate = float(cleaned_rate)
                        if rate <= 100:
                            break
                        else:
                            print("Rate must be equal or less than 100")
                    else:
                        print("Invalid rate. Enter a valid rate.")
                while True:
                    time_input = input("Enter the time period (in years): ")
                    cleaned_time = time_input.replace(" ","").strip()
                    if cleaned_time.replace(".","",1).isdigit():
                        time = float(cleaned_time)
                        break
                    else:
                        print("Invalid input. Enter valid time")

                bond_value = calculate_bond(principal, rate, time)
                print(f"The value of the bond will be: R{bond_value:.2f}")
                break
            else:
                print("Invalid input. Please enter 'I' for investment or 'B' for bond.")
            
            another_calculation = input("Do you want to perform another calculation? (yes/no): ")
            while another_calculation.upper() not in ['Y', 'N','YES','NO']:
                print("Invalid input. Please enter 'yes' or 'no'.")
                another_calculation = input("Do you want to perform another calculation? (yes/no): ")
            
            if another_calculation.upper() == 'NO':
                break

if __name__ == "__main__":
    main()
