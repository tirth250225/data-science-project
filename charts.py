import streamlit as st
import plotly.express as px

def show_charts(df):
    col1, col2 = st.columns(2)

    with col1:
        fig1 = px.bar(
            df.groupby("Category")["Sales"].sum().reset_index(),
            x="Category",
            y="Sales",
            title="Sales by Category"
        )
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        fig2 = px.bar(
            df.groupby("State")["Profit"].sum().reset_index(),
            x="State",
            y="Profit",
            title="Profit by State"
        )
        st.plotly_chart(fig2, use_container_width=True)