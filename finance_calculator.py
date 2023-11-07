import math

#(i.P)/(1 - (1+i)^(-n))

def calculate_investment_s(principal, rate, time):
    future_value_s = principal*(1+(rate/100)*time)
    return future_value_s

def calculate_investment_c(principal, rate, time):
    future_value_c = principal* math.pow((1+(rate/100)),time)
    #*(1+rate*time)
    return future_value_c

def calculate_bond(principal, rate, time):
    rate = rate/1200
    time = time*12
    bond_value = (rate * principal)/(1 - (1+rate)**-time)
    return bond_value

def main():

    while True:

        print("=====================================")
        print(" Thee Deciders Financial Calculator  ")
        print("----------------Menu-----------------")
        print("=====================================")
        principal_input = float(input("Enter the principal amount: R "))
        principal = float(principal_input.replace(" ", ""))
        rate = float(input("Enter the annual interest rate (%): "))
        time = float(input("Enter the time period (in years): "))

        investment_type = input("Enter 'I' for investment or 'B' for bond: ")

        if investment_type.upper() == 'I':
            invest = input("Enter 'S' for Simple interest or 'C' for Compound interest: ")
            if invest.upper() == 'S':
                future_value_s = calculate_investment_s(principal, rate, time)
                print(f"The future value of your investment will be: R{future_value_s:.2f}")

            elif invest.upper() == 'C':
                future_value_c = calculate_investment_s(principal, rate, time)
                print(f"The future value of your investment will be: R{future_value_c:.2f}")

            else:
                print("Invalid input. Please enter 'S' for Simple interest or 'C' for compound.")

        elif investment_type.upper() == 'B':
            bond_value = calculate_bond(principal, rate, time)
            print(f"The value of the bond will be: R{bond_value:.2f}")

        else:
            print("Invalid input. Please enter 'I' for investment or 'B' for bond.")

if __name__ == "__main__":

    main()
