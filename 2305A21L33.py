import streamlit as st

# Define the STAR_DELTA function
def STAR_DELTA(R1, R2, R3):
    """
    Converts Star connection resistances (R1, R2, R3) to Delta connection resistances (R12, R23, R31).
    """
    R_sum = R1 * R2 + R2 * R3 + R3 * R1
    R12 = R_sum / R3 if R3 != 0 else 0
    R23 = R_sum / R1 if R1 != 0 else 0
    R31 = R_sum / R2 if R2 != 0 else 0
    return R12, R23, R31

# Streamlit app title
st.title("02341A0259-PS4: STAR to DELTA Resistance Calculator")

# Input fields for R1, R2, R3
st.header("Enter Star Connection Resistances:")
R1 = st.number_input("R1 (in ohms):", min_value=0.0, format="%.2f", step=0.01)
R2 = st.number_input("R2 (in ohms):", min_value=0.0, format="%.2f", step=0.01)
R3 = st.number_input("R3 (in ohms):", min_value=0.0, format="%.2f", step=0.01)

# Compute Delta resistances when the button is clicked
if st.button("Compute"):
    R12, R23, R31 = STAR_DELTA(R1, R2, R3)
    
    # Display results
    st.subheader("Delta Connection Resistances:")
    st.write(f"R12: {R12:.2f} ohms")
    st.write(f"R23: {R23:.2f} ohms")
    st.write(f"R31: {R31:.2f} ohms")
import streamlit as st

# Define the STAR_DELTA function
def STAR_DELTA(R1, R2, R3):
    """
    Converts Star connection resistances (R1, R2, R3) to Delta connection resistances (R12, R23, R31).
    """
    R_sum = R1 * R2 + R2 * R3 + R3 * R1
    R12 = R_sum / R3 if R3 != 0 else 0
    R23 = R_sum / R1 if R1 != 0 else 0
    R31 = R_sum / R2 if R2 != 0 else 0
    return R12, R23, R31

# Streamlit app title
st.title(" 2305A21L33-PS4 :STAR to DELTA Resistance Calculator")

# Input fields for R1, R2, R3
st.header("Enter Star Connection Resistances:")
R1 = st.number_input("R1 (in ohms):", min_value=0.0, format="%.2f", step=0.01)
R2 = st.number_input("R2 (in ohms):", min_value=0.0, format="%.2f", step=0.01)
R3 = st.number_input("R3 (in ohms):", min_value=0.0, format="%.2f", step=0.01)

# Compute Delta resistances when the button is clicked
if st.button("Compute"):
    R12, R23, R31 = STAR_DELTA(R1, R2, R3)
    
    # Display results
    st.subheader("Delta Connection Resistances:")
    st.write(f"R12: {R12:.2f} ohms")
    st.write(f"R23: {R23:.2f} ohms")
    st.write(f"R31: {R31:.2f} ohms")