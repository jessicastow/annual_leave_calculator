# Annual Leave Calculator 🏖️ 💼 📅

This code was written to fulfill the need for accurate annual leave calculations and outstanding payment tracking for employees and employers.

### The problem
When employees leave their jobs, calculating the exact amount of annual leave owed can be complex and time-consuming. HR departments and small business owners often struggle with:
- Pro-rata leave calculations based on employment duration
- Tracking leave already taken versus leave earned
- Determining outstanding payments or overpayments
- Creating professional summaries for final pay calculations

Manual calculations are prone to errors and can lead to disputes between employers and employees. Many organizations rely on spreadsheets or manual calculations, which is inefficient and can result in incorrect payments.

In order to save time and ensure accuracy, I developed a [python script](annual_leave_calculator.py) that automatically calculates annual leave entitlements, tracks usage, and determines final outstanding balances with a professional summary output.

### 💡 Source
This code was inspired by the need for accurate leave calculations during employment transitions and the desire to create a user-friendly tool that both HR professionals and individual employees can use.

### 🧮 Calculation Method
The calculator uses standard pro-rata annual leave calculations:
- **Leave Earned** = (Weeks Worked ÷ 52) × Annual Entitlement
- **Leave Balance** = Leave Earned - Leave Used - Leave Paid
- Provides clear indication of outstanding payments, overpayments, or balanced accounts

### 🏃‍♀️ Run

There are two ways to run this script:
1. The interactive Python script can be run here [Trinket.io](https://trinket.io/python3/171561a9c746?outputOnly=true&runOption=run&showInstructions=true
).

2. Alternatively, copy the Python code from [Leave.rmd](Leave.rmd) into any Python environment to try out the program.

### My solution, explained

My code made use of the following variables and arguments:

- `employee_name`: Name of the employee (input). The user will be asked to enter the employee's name.
- `start_date`: Employment start date (input). Must be in yyyy-mm-dd format.
- `end_date`: Employment end date (input). Must be in yyyy-mm-dd format.
- `annual_entitlement`: Total annual leave days per year (input, defaults to 28). Standard entitlements vary by country/company.
- `leave_used`: Number of leave days already taken during employment (input, defaults to 0).
- `leave_paid`: Number of leave days already paid out (input, defaults to 0).
- `days_worked`: Calculated total employment duration in days.
- `weeks_worked`: Calculated employment duration in weeks (used for pro-rata calculations).
- `leave_owed`: Calculated pro-rata leave earned based on employment duration.
- `final_leave_balance`: Final calculation showing outstanding leave (positive = owed to employee, negative = overpaid).
- `again`: Asks the user whether they would like to calculate for another employee. If the user answers 'yes', the script runs again.

### Features
- **Interactive prompts**: User-friendly step-by-step input collection
- **Input validation**: Checks date formats and handles invalid entries gracefully
- **Professional output**: Generates a formatted summary suitable for HR records
- **Error handling**: Provides defaults and clear error messages
- **Recursive functionality**: Calculate for multiple employees in one session
- **Flexible defaults**: Press Enter to use common values (28 days annual leave, 0 for unused fields)

Any feedback on my solution is welcome! Email me: stowjess@gmail.com

### Notes/Updates to do...

1. Add validation for reasonable date ranges (start date must be before end date)
2. Add support for different date formats (dd/mm/yyyy, mm-dd-yyyy, etc.)
3. Include company-specific leave policies (public holidays, additional entitlements)
4. Add export functionality to save results to PDF or CSV files
5. Include weekend/public holiday exclusions for more precise calculations
6. Add support for part-time employees with pro-rata annual entitlements
7. Add a calculation for the value of leave based on monthly / annual salary
