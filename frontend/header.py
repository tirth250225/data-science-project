import streamlit as st

def show_header():
    left_col, center_col, right_col = st.columns([6, 3, 1])

    with left_col:
        st.markdown("""
        <div style="
            background-color:#1E1E1E;
            padding:20px;
            border-radius:18px;
            margin-bottom:20px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.25);
        ">
            <h1 style="
                margin:0;
                color:white;
                font-size:32px;
            ">
                📊 Sales Analytics Dashboard
            </h1>
            <p style="
                margin-top:8px;
                color:white;
                font-size:14px;
            ">
                Real-time business insights & performance tracking
            </p>
        </div>
        """, unsafe_allow_html=True)

    with center_col:
        st.markdown("""
        <div style="
            background-color:#1E1E1E;
            padding:20px;
            border-radius:18px;
            margin-bottom:20px;
            text-align:center;
        ">
            <h3 style="margin:0; color:white;">
                👤 tirth
            </h3>
            <p style="margin-top:6px; color:#A0A0A0;">
                Logged In
            </p>
        </div>
        """, unsafe_allow_html=True)

    with right_col:
        st.write("")
        st.write("")
        logout_clicked = st.button("Logout")

    return logout_clicked