def main():
    expense_total = 0
    # Ask the user for their budget for the month
    budget = float(input('What is your budget for the month? '))
    # While loop if budget is less than or equal to zero
    while True:
        if budget <= 0:
            print("Enter a positive number and/or number greater than zero.")
            budget = float(input("Enter amount budgeted for the month:  "))
        else:
            # Create a variable to control the loop
            keep_going = 'y'
            # Calculate a series of expenses
            while keep_going == 'y':
                # Ask the user to enter an expense
                expense = float(input('Enter an expense (0 to quit:) '))
                # Validate expense less than zero
                if expense < 0:
                    print("Enter a positive expense.")
                elif expense > 0:
                # Calculate the remainder of the budget
                    budget -= expense
                    print('Your remaining budget is $%.2f.' % budget)
                    expense_total += expense
                    print('Your total expenses are $%.2f.' % expense_total)
                # Ask the user if they'd like to enter another expense
                keep_going = input('Do you want to calculate another expense (Enter y for yes) or zero to stop: ').lower()
            else:
                # Print result if expense is zero
                    if expense_total > budget:
                        over_budget = budget
                        print("You are", over_budget, "over budget. PLAN BETTER NEXT TIME!")
                    else:
                        print('Your remaining budget is $%.2f.' % budget)
                        print('Your total expenses are $%.2f.' % expense_total)   
                    break             
# Call the main function
main()
