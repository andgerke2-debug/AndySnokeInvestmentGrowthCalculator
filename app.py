import streamlit as st
import pandas as pd

# Set up the app
st.set_page_config(page_title="Investment Growth Calculator", page_icon="💰")

st.title("💰 Investment Growth Calculator")
st.write("See how your investments could grow over time!")

# Get information from the user
st.header("Enter Your Investment Details")

initial = st.number_input(
    "Starting Investment ($)", min_value=0.0, value=1000.0, step=100.0
)

monthly = st.number_input(
    "Monthly Contribution ($)", min_value=0.0, value=200.0, step=50.0
)

rate = st.number_input(
    "Expected Annual Return (%)", min_value=0.0,
    max_value=100.0, value=7.0, step=0.5
)

years = st.number_input(
    "Number of Years", min_value=1, max_value=50, value=20
)

# Calculate investment growth
if st.button("Calculate Investment Growth"):

    balance = initial
    total_contributed = initial
    monthly_rate = rate / 100 / 12

    # Store results for the chart
    data = [{
        "Year": 0,
        "Investment Value": balance,
        "Total Contributions": total_contributed
    }]

    for year in range(1, years + 1):
        for month in range(12):
            balance = balance * (1 + monthly_rate) + monthly
            total_contributed += monthly

        data.append({
            "Year": year,
            "Investment Value": balance,
            "Total Contributions": total_contributed
        })

    investment_growth = balance - total_contributed

    # Display the results
    st.header("Your Investment Results")

    col1, col2, col3 = st.columns(3)

    col1.metric("Future Value", f"${balance:,.2f}")
    col2.metric("Money Contributed", f"${total_contributed:,.2f}")
    col3.metric("Investment Growth", f"${investment_growth:,.2f}")

    # Create a line chart
    df = pd.DataFrame(data)
    st.subheader("Investment Growth Over Time")
    st.line_chart(df.set_index("Year"))

    st.info(
        "This calculator assumes a constant annual return, "
        "compounded monthly, with contributions at the end of each month. "
        "Actual investment returns will vary."
    )
