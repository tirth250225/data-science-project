import streamlit as st
from config import PAGE_TITLE
from data_loader import load_data
from filters import apply_filters
from metrics import show_metrics
from charts import show_charts

# -----------------------------
# LOGIN FUNCTION
# -----------------------------
def login():
    st.title("🔐 Login to Dashboard")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "1234":
            st.session_state["logged_in"] = True
        else:
            st.error("Invalid username or password")

# -----------------------------
# SESSION CONTROL
# -----------------------------
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

# -----------------------------
# MAIN APP
# -----------------------------
if not st.session_state["logged_in"]:
    login()
else:
    st.set_page_config(page_title=PAGE_TITLE, layout="wide")

    st.title("📊 Sales Analytics Dashboard")

    # Logout button
    if st.button("Logout"):
        st.session_state["logged_in"] = False
        st.rerun()

    df = load_data()
    filtered_df = apply_filters(df)

    show_metrics(filtered_df)
    st.divider()
    show_charts(filtered_df)

    st.subheader("📋 Sales Data")
    st.dataframe(filtered_df, use_container_width=True)