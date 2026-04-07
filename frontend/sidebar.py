import streamlit as st


def show_sidebar_filters(df):
    st.sidebar.markdown("""
    <div style="
        background-color:#1E1E1E;
        padding:15px;
        border-radius:15px;
        margin-bottom:20px;
    ">
        <h3 style="color:white; margin:0;">🔍 Filters</h3>
        <p style="color:#A0A0A0; margin-top:6px;">
            Select filters for dashboard
        </p>
    </div>
    """, unsafe_allow_html=True)

    state_filter = st.sidebar.multiselect(
        "Select State",
        options=sorted(df["State"].unique()),
        default=sorted(df["State"].unique())
    )

    category_filter = st.sidebar.multiselect(
        "Select Category",
        options=sorted(df["Category"].unique()),
        default=sorted(df["Category"].unique())
    )

    filtered_df = df[
        (df["State"].isin(state_filter)) &
        (df["Category"].isin(category_filter))
    ]

    return filtered_df