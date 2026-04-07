import streamlit as st

def show_kpi_cards(df):
    total_sales = df["Sales"].sum()
    total_profit = df["Profit"].sum()
    avg_sales = df["Sales"].mean()
    quantity = df["Quantity"].sum()
    margin = (total_profit / total_sales) * 100 if total_sales else 0

    cards = [
        ("💰", "Total Sales", f"{total_sales:,.0f}"),
        ("📈", "Total Profit", f"{total_profit:,.0f}"),
        ("📊", "Avg Sales", f"{avg_sales:,.0f}"),
        ("📦", "Quantity", f"{quantity:,}"),
        ("🎯", "Margin", f"{margin:.2f}%")
    ]

    cols = st.columns(5)

    for col, (icon, title, value) in zip(cols, cards):
        with col:
            st.markdown(f"""
            <div style="
                background-color:#1E1E1E;
                padding:20px;
                border-radius:18px;
                height:170px;
                display:flex;
                flex-direction:column;
                justify-content:space-between;
                box-shadow: 0 4px 10px rgba(0,0,0,0.25);
            ">
                <div style="font-size:20px; color:#B0B0B0;">
                    {icon} <b>{title}</b>
                </div>
                <div style="
                    font-size:42px;
                    font-weight:700;
                    color:white;
                    text-align:center;
                    margin-top:20px;
                ">
                    {value}
                </div>
            </div>
            """, unsafe_allow_html=True)