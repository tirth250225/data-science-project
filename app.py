import streamlit as st
from data_loader import load_data
from frontend.header import show_header
from frontend.card import show_kpi_cards
from frontend.sidebar import show_sidebar_filters
from frontend.sections import (
    show_chart_section,
    show_india_sales_map,
    show_state_insights
)

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Sales Dashboard",
    layout="wide"
)

# -----------------------------
# SESSION LOGIN
# -----------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


# -----------------------------
# LOGIN PAGE
# -----------------------------
def login_page():
    st.title("🔐 Login to Dashboard")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login", key="login_btn"):
        if username == "admin" and password == "admin123":
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Invalid credentials ❌")


# -----------------------------
# DASHBOARD
# -----------------------------
def dashboard():
    df = load_data()

    # HEADER handles logout
    logout_clicked = show_header()

    if logout_clicked:
        st.session_state.logged_in = False
        st.rerun()

    filtered_df = show_sidebar_filters(df)

    show_kpi_cards(filtered_df)

    show_chart_section(filtered_df)

    show_india_sales_map(filtered_df)

    show_state_insights(filtered_df)

    st.divider()
    st.subheader("📋 Sales Data")
    st.dataframe(filtered_df, use_container_width=True)


# -----------------------------
# APP FLOW
# -----------------------------
if st.session_state.logged_in:
    dashboard()
else:
    login_page()