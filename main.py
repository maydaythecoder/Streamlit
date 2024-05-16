import math
import pandas as pd
import streamlit as st

st.title('MortgageMate')

st.write('### Input Data')
col1, col2 = st.columns(2)
homeValue = col1.number_input("Home Value", min_value=0, value=500000)
deposit = col1.number_input("Deposit", min_value=0, value=100000)
interestRate = col2.number_input("Interest Rate (in %)", min_value=0.0, value=5.5)
loanTerm = col2.number_input("Loan Term ( in years)", min_value=1, value=30)

loanAmount = homeValue - deposit
monthlyInterestRate = (interestRate / 100) / 12
numberOfPayments = loanTerm * 12
monthlyPayment = (
        loanAmount
        * (monthlyInterestRate * (1 + monthlyInterestRate) ** numberOfPayments)
        / ((1 + monthlyInterestRate) ** numberOfPayments - 1)
)

totalPayments = monthlyPayment * numberOfPayments
totalInterest = totalPayments - loanAmount

st.write('### Repayments')
col1, col2, col3 = st.columns(3)
col1.metric(label='Monthly Repayments', value=f"${monthlyPayment:,.2f}")
col2.metric(label='Total Repayments', value=f"${totalPayments:,.0f}")
col3.metric(label='Total Interest', value=f"${totalInterest:,.0f}")

schedule = []
remainingBalance = loanAmount

for i in range(1, numberOfPayments + 1):
    interestPayment = remainingBalance * monthlyInterestRate
    principalPayment = monthlyPayment - interestPayment
    remainingBalance -= principalPayment
    year = math.ceil(i / 12)
    schedule.append(
        [
            i,
            monthlyPayment,
            principalPayment,
            interestPayment,
            remainingBalance,
            year,
        ]
    )

df = pd.DataFrame(
    schedule,
    columns=["Month", "Payments", "Principal", "Interest", "Remaining Balance", "Year"],
)
st.write('### Payment Schedule')
paymentDF = df[["Year", "Remaining Balance"]].groupby("Year").min()
st.line_chart(paymentDF)
