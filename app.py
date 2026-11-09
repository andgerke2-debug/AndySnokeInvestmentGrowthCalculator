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
