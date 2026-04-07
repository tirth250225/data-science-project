import streamlit as st
import plotly.express as px
import pandas as pd


def show_chart_section(df):
    df["Date"] = pd.to_datetime(df["Date"])

    # -----------------------------
    # Row 1
    # -----------------------------
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📊 Sales by Category")

        category_sales = (
            df.groupby("Category")["Sales"]
            .sum()
            .reset_index()
        )

        fig1 = px.bar(
            category_sales,
            x="Category",
            y="Sales",
            text="Sales",
            template="plotly_dark"
        )

        fig1.update_traces(textposition="outside")
        fig1.update_layout(height=400)

        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        st.subheader("📈 Profit by State")

        state_profit = (
            df.groupby("State")["Profit"]
            .sum()
            .reset_index()
        )

        fig2 = px.bar(
            state_profit,
            x="State",
            y="Profit",
            text="Profit",
            template="plotly_dark"
        )

        fig2.update_traces(textposition="outside")
        fig2.update_layout(height=400)

        st.plotly_chart(fig2, use_container_width=True)

    st.divider()

    # -----------------------------
    # Row 2
    # -----------------------------
    col3, col4 = st.columns(2)

    with col3:
        st.subheader("📅 Monthly Sales Trend")

        monthly_sales = (
            df.groupby(df["Date"].dt.to_period("M"))["Sales"]
            .sum()
            .reset_index()
        )

        monthly_sales["Date"] = monthly_sales["Date"].astype(str)

        fig3 = px.line(
            monthly_sales,
            x="Date",
            y="Sales",
            markers=True,
            template="plotly_dark"
        )

        fig3.update_layout(height=400)

        st.plotly_chart(fig3, use_container_width=True)

    with col4:
        st.subheader("🥧 Sales Share by Category")

        pie_data = (
            df.groupby("Category")["Sales"]
            .sum()
            .reset_index()
        )

        fig4 = px.pie(
            pie_data,
            names="Category",
            values="Sales",
            hole=0.4,
            template="plotly_dark"
        )

        fig4.update_layout(height=400)

        st.plotly_chart(fig4, use_container_width=True)


def show_india_sales_map(df):
    st.divider()
    st.subheader("🗺️ State & City Sales Analysis")

    col1, col2 = st.columns(2)

    with col1:
        state_sales = (
            df.groupby("State")["Sales"]
            .sum()
            .reset_index()
        )

        fig = px.bar(
            state_sales,
            x="State",
            y="Sales",
            text="Sales",
            template="plotly_dark",
            title="State-wise Sales"
        )

        fig.update_traces(textposition="outside")
        fig.update_layout(height=450)

        st.plotly_chart(fig, use_container_width=True)

    with col2:
        city_sales = (
            df.groupby("City")["Sales"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
            .reset_index()
        )

        fig_city = px.pie(
            city_sales,
            names="City",
            values="Sales",
            hole=0.4,
            template="plotly_dark",
            title="Top Cities by Sales"
        )

        fig_city.update_layout(height=450)

        st.plotly_chart(fig_city, use_container_width=True)


def show_state_insights(df):
    st.divider()
    st.subheader("📍 State Performance Insights")

    state_summary = (
        df.groupby("State")
        .agg({
            "Sales": "sum",
            "Profit": "sum",
            "Quantity": "sum"
        })
        .reset_index()
    )

    st.dataframe(state_summary, use_container_width=True)