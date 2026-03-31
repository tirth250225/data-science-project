import streamlit as st

def apply_filters(df):
    st.sidebar.header("Filters")

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

    return filtered_df