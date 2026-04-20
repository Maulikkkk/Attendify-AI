import streamlit as st

def footer_home():
    st.markdown("""
        <div style="
            margin-top: 3rem;
            padding: 1rem 0;
            text-align: center;
            border-top: 1px solid rgba(0,0,0,0.1);
            font-size: 0.9rem;
            color: white;
        ">
            <p style="margin:0;">
                © 2026 <b>Maulik Gupta</b> · Built with Streamlit
            </p>
        </div>
    """, unsafe_allow_html=True)