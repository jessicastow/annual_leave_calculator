# ANNUAL LEAVE CALCULATOR - INTERACTIVE PYTHON VERSION
# =====================================================

from datetime import datetime, timedelta

print('This program calculates annual leave entitlements and outstanding payments.')

def calculate_leave_summary(employee_name, start_date, end_date, annual_entitlement, leave_used, leave_paid):
    """Calculate and display annual leave summary"""
    
    # Convert string dates to datetime objects
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    
    # Calculate employment period
    days_worked = (end - start).days
    weeks_worked = days_worked / 7
    months_worked = round(weeks_worked / 4.33, 1)
    
    # Calculate leave entitlements
    leave_owed = (weeks_worked / 52) * annual_entitlement
    leave_remaining = leave_owed - leave_used
    final_leave_balance = leave_remaining - leave_paid
    
    # Print professional summary
    print("\n" + "=" * 60)
    print("           ANNUAL LEAVE CALCULATION SUMMARY")
    print("=" * 60)
    print()
    
    print(f"Employee: {employee_name}")
    print("Employment Period:")
    print(f"  Start Date: {start.strftime('%d %B %Y')}")
    print(f"  End Date: {end.strftime('%d %B %Y')}")
    print(f"  Total Days Worked: {days_worked} days")
    print(f"  Total Weeks Worked: {weeks_worked:.1f} weeks")
    print(f"  Total Months Worked: {months_worked} months")
    print()
    
    print("Annual Leave Calculation:")
    print(f"  Annual Entitlement: {annual_entitlement} days per year")
    print(f"  Pro-rata Leave Earned: {leave_owed:.2f} days")
    print(f"  Leave Days Used: {leave_used} days")
    print(f"  Leave Balance Before Payout: {leave_remaining:.2f} days")
    print()
    
    print("Leave Payout:")
    print(f"  Days Paid Out: {leave_paid} days")
    print(f"  Final Leave Balance: {final_leave_balance:.2f} days")
    print()
    
    if final_leave_balance > 0:
        print(f"OUTSTANDING: {final_leave_balance:.2f} days of leave remain unpaid")
    elif final_leave_balance < 0:
        print(f"OVERPAID: {abs(final_leave_balance):.2f} days of leave were overpaid")
    else:
        print("BALANCED: All leave has been appropriately accounted for")
    
    print()
    print("=" * 60)

def leave_calculator():
    """Interactive leave calculator function"""
    
    # Get employee details
    employee_name = str(input("Employee name: ")).strip()
    
    # Get employment dates
    start_date = input("Employment start date (format: yyyy-mm-dd): ").strip()
    end_date = input("Employment end date (format: yyyy-mm-dd): ").strip()
    
    # Validate date format
    try:
        datetime.strptime(start_date, "%Y-%m-%d")
        datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use yyyy-mm-dd format.")
        return leave_calculator()
    
    # Get annual entitlement
    entitlement_input = input("Annual leave entitlement in days (press Enter for 28): ").strip()
    if entitlement_input == "":
        annual_entitlement = 28
    else:
        try:
            annual_entitlement = int(entitlement_input)
        except ValueError:
            print("Invalid number. Using default of 28 days.")
            annual_entitlement = 28
    
    # Get leave used
    used_input = input("Days of leave already used (press Enter for 0): ").strip()
    if used_input == "":
        leave_used = 0
    else:
        try:
            leave_used = int(used_input)
        except ValueError:
            print("Invalid number. Using 0.")
            leave_used = 0
    
    # Get leave paid
    paid_input = input("Days of leave already paid out (press Enter for 0): ").strip()
    if paid_input == "":
        leave_paid = 0
    else:
        try:
            leave_paid = int(paid_input)
        except ValueError:
            print("Invalid number. Using 0.")
            leave_paid = 0
    
    # Calculate and display results
    calculate_leave_summary(employee_name, start_date, end_date, annual_entitlement, leave_used, leave_paid)
    
    # Ask if they want to calculate again
    again = input('\nWould you like to calculate for another employee? (yes/no): ').lower().strip()
    if again == 'yes' or again == 'y':
        print("\n" + "-" * 60)
        leave_calculator()
    else:
        print("Thank you for using the Annual Leave Calculator!")

# Start the interactive calculator
leave_calculator()

# Notes:
# - Add validation for reasonable date ranges (start < end)
# - Could add support for different date formats
# - Could add company-specific leave policies
# - Could export results to file


