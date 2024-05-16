# Mortgage Repayments Calculator

This is a Streamlit application that calculates mortgage repayments based on user inputs for home value, deposit, interest rate, and loan term. It provides a user-friendly interface for entering the required information and displays the monthly repayments, total repayments, and total interest. Additionally, it generates a payment schedule and visualizes the remaining balance over the loan term using a line chart.

## Features

- User inputs for home value, deposit, interest rate, and loan term
- Calculation of monthly repayments, total repayments, and total interest
- Generation of a payment schedule with monthly details (payment number, payment amount, principal, interest, and remaining balance)
- Visualization of the remaining balance over the loan term using a line chart

## Requirements

- Python
- Streamlit
- Pandas


## Usage

1. Install the required packages: 
```
pip install streamlit
```
```
pip install pandas
```
2. Save the provided code as a Python file (e.g., `mortgage_calculator.py`).
3. Run the Streamlit app:
```
streamlit run mortgage_calculator.py
```
4. The app will open in your default web browser, allowing you to interact with the mortgage repayments calculator.

## How It Works

1. The user inputs the home value, deposit, interest rate, and loan term.
2. The code calculates the loan amount by subtracting the deposit from the home value.
3. Using the loan amount, interest rate, and loan term, the code computes the monthly repayments, total repayments, and total interest.
4. The calculated values are displayed in the app using Streamlit's metric components.
5. A payment schedule is generated, showing the monthly details (payment number, payment amount, principal, interest, and remaining balance) for each payment over the loan term.
6. The remaining balance for each year is extracted from the payment schedule and visualized using a line chart.

## Customization

You can customize the app by modifying the code as needed. For example, you can change the default values for the inputs, adjust the layout and styling, or add additional functionality.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
