import streamlit as st
#input data
st.write('# Input data')
col1,col2=st.columns(2)
ebit=col1.number_input('Earnings beofre tax and interest in thousand $',min_value=0,placeholder=50)
tax_rate=col1.number_input('Tax rate')
depreciation =col2.number_input('Depreciation & Amortization (Non-cash expenses)')
nwc_change=col2.number_input('Change in Net Working Captial (compare to previous period)')
capex=col1.number_input('Capital Expenditures (CapEx)')
# Calculating FCFF
fcff=ebit*1000*(1-tax_rate/100)+depreciation-nwc_change-capex
#Submit button
submit=st.button('Calculate')

if submit:
    st.metric(label='Your FCFF: ' , value=fcff)
