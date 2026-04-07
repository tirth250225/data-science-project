import streamlit as st

def apply_filters(df):
    st.sidebar.header("🔍 Filters")

    state_filter = st.sidebar.multiselect(
        "Select State",
        df["State"].unique(),
        default=df["State"].unique()
    )

    category_filter = st.sidebar.multiselect(
        "Select Category",
        df["Category"].unique(),
        default=df["Category"].unique()
    )

    filtered_df = df[
        (df["State"].isin(state_filter)) &
        (df["Category"].isin(category_filter))
    ]

import streamlit as st
import pandas as pd

def show_sidebar_filters(df):
    st.sidebar.header("Filters")

    # -----------------------------
    # Date Filter
    # -----------------------------
    min_date = df["Date"].min()
    max_date = df["Date"].max()

    start_date, end_date = st.sidebar.date_input(
        "Select Date Range",
        value=[min_date, max_date],
        min_value=min_date,
        max_value=max_date
    )

    # Ensure start_date <= end_date
    if start_date > end_date:
        st.sidebar.error("Start date must be before end date")
        start_date = min_date
        end_date = max_date

    filtered_df = df[(df["Date"] >= pd.to_datetime(start_date)) & 
                     (df["Date"] <= pd.to_datetime(end_date))]

    # -----------------------------
    # Other filters like State, Category
    # -----------------------------
    states = st.sidebar.multiselect(
        "Select State",
        options=df["State"].unique(),
        default=df["State"].unique()
    )

    categories = st.sidebar.multiselect(
        "Select Category",
        options=df["Category"].unique(),
        default=df["Category"].unique()
    )

    filtered_df = filtered_df[
        (filtered_df["State"].isin(states)) &
        (filtered_df["Category"].isin(categories))
    ]

    return filtered_df
    return filtered_df