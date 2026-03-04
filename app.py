from pathlib import Path
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assests" / "Kanya_Resume_Final.pdf"
profile_pic = current_dir / "assests" / "kanya_profile_pic.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Kanya V | Business Analyst"
PAGE_ICON = "📊"
NAME = "Kanya V"

DESCRIPTION = """
**Business Analyst** with 2+ years of experience in requirement gathering,
stakeholder communication, KPI tracking, and insight generation.

Skilled in bridging the gap between business teams and developers —
translating client needs into structured requirements and actionable reports.
Hands-on with **SQL, Power BI, Python, Excel, and GA4**.
"""

EMAIL = "kanyavasu7@gmail.com"

SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com/in/kanya-v",
    "GitHub": "https://github.com/kanyavasudev",
    "Portfolio": "https://kanya-v.streamlit.app",
}

# --- PAGE CONFIG ---
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=300)

with col2:
    st.markdown(f"## {NAME}")
    st.markdown("##### Business Analyst | Data Analyst")
    st.write(DESCRIPTION)
    st.download_button(
        label="📄 Download Resume",
        data=PDFbyte,
        file_name="Kanya_V_Resume.pdf",
        mime="application/octet-stream",
        type="primary",
    )
    st.markdown(f"""
    📧 {EMAIL}  
    [![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?logo=linkedin)]({SOCIAL_MEDIA['LinkedIn']}) &nbsp;
    [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)]({SOCIAL_MEDIA['GitHub']})
    """)

# --- WHAT I BRING ---
st.write("---")
st.subheader("🎯 What I Bring")
col1, col2 = st.columns(2)
with col1:
    st.write("""
    ✔ **Requirement Gathering** — worked directly with clients to define business needs and translate them into functional specs for developers  
    ✔ **Stakeholder Communication** — single point of contact between business owners and dev teams  
    ✔ **KPI Reporting** — built dashboards and trackers used by real businesses for decision-making  
    ✔ **Data Analysis** — analyzed 50,000+ records and 3 years of government transport data  
    """)
with col2:
    st.write("""
    ✔ **Process Documentation** — structured execution plans, scope definitions, and handover docs  
    ✔ **Business Insight** — connected data findings to real-world business decisions  
    ✔ **Cross-functional Work** — collaborated with marketing, design, and development teams  
    ✔ **Trend Analysis** — identified patterns in campaign, traffic, and ridership data  
    """)

# --- SKILLS ---
st.write("---")
st.subheader("🛠️ Technical Skills")

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("**Business Analysis**")
    st.write("""
    - Requirement Gathering  
    - Stakeholder Communication  
    - Process Mapping  
    - Scope Definition  
    - Documentation  
    """)
with col2:
    st.markdown("**Data & Reporting**")
    st.write("""
    - SQL & MySQL  
    - Python (Pandas, Matplotlib, Seaborn)  
    - Power BI Dashboards  
    - Excel & Google Sheets  
    - GA4 Analytics  
    """)
with col3:
    st.markdown("**Tools**")
    st.write("""
    - MySQL Workbench  
    - Jupyter Notebook  
    - Git & GitHub  
    - Streamlit  
    - Google Analytics  
    """)

# --- EXPERIENCE ---
st.write("---")
st.subheader("💼 Professional Experience")

# Job 1
st.markdown("**Freelance Business Analyst / Marketing Insights Consultant**")
st.caption("May 2025 – Present | Chennai, India")
st.write("""
- Engaged directly with clients to gather business goals, define scope, and translate requirements into functional specs for developers  
- Acted as single point of contact between business owners and development teams — reducing miscommunication and rework  
- Built Excel-based KPI trackers and dashboards used by clients for weekly performance monitoring  
- Analyzed campaign and engagement data to provide actionable insights on budget and content strategy  
- Structured execution plans and tracked delivery milestones to ensure requirements were met before sign-off  
""")

st.write("")

# Job 2
st.markdown("**Digital Marketing Executive – Reporting & KPI Analysis**")
st.caption("Jan 2024 – Mar 2025 | StrongBox IT, Chennai")
st.write("""
- Maintained GA4 dashboards and analyzed 15+ KPIs across traffic, user behavior, and conversion funnels  
- Prepared monthly performance reports and presented insights to internal stakeholders  
- Improved organic website traffic by **40%** through data-driven SEO analysis  
- Conducted competitor benchmarking in Excel, contributing to a **25% increase** in inbound leads  
""")

st.write("")

# Job 3
st.markdown("**Digital Marketing Intern – Data Tracking & Reporting**")
st.caption("Jul 2023 – Dec 2023 | StrongBox IT, Chennai")
st.write("""
- Cleaned and validated datasets with 10,000+ records to improve reporting accuracy  
- Supported weekly reporting by summarizing social media performance trends across 4 platforms  
""")

# --- PROJECTS ---
st.write("---")
st.subheader("🚀 Projects")

# Project 1 - CMRL
with st.container():
    st.markdown("### 🚇 Chennai Metro Ridership Analysis")
    st.caption("Python | MySQL | Power BI | 2025")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("""
        Analyzed **3 years of official CMRL ridership data** (Apr 2023 – Feb 2026) sourced directly 
        from the Chennai Metro Rail open data portal.
        
        **Key Findings:**
        - 📉 Closed Loop tokens collapsed from **65% → 0.40%** in 3 years — complete digital shift  
        - 🚀 Singara Chennai Card launch (Feb 2025) caused a **17% surge** in NCMC adoption in one month  
        - 📅 April consistently lowest ridership — summer holidays effect  
        - 🌧️ August dips every year — Chennai monsoon season  
        - 🏆 NCMC crossed **50% of total ridership** for first time in Oct 2025  
        
        **Tools:** Python (EDA), MySQL Workbench (5 SQL queries), Power BI (2-page dashboard)
        """)
    with col2:
        st.markdown("**What This Shows:**")
        st.info("""
        ✅ Real government data  
        ✅ Business questions defined  
        ✅ SQL querying  
        ✅ Stakeholder dashboard  
        ✅ Insight documentation  
        """)
        st.markdown("[🔗 View on GitHub](https://github.com/kanyavasudev/cmrl-analysis)")

st.write("")

# Project 2 - Library
with st.container():
    st.markdown("### 📚 Library Management System")
    st.caption("Python | Streamlit | MySQL | 2025")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("""
        End-to-end business process and database design project simulating 
        a real library management system.
        
        **What Was Built:**
        - Gathered and structured core business requirements for library operations  
        - Translated functional requirements into a **relational MySQL database** with 6 tables  
        - Designed interactive Streamlit interface for non-technical users (CRUD operations)  
        - Deployed on **Railway (cloud DB) + Streamlit Cloud** — live and accessible  
        
        **Tools:** Python, MySQL, Streamlit, Railway Cloud
        """)
    with col2:
        st.markdown("**What This Shows:**")
        st.info("""
        ✅ Requirement gathering  
        ✅ Database design  
        ✅ End-to-end delivery  
        ✅ Live deployment  
        ✅ User-focused design  
        """)
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("[🔗 Live App](https://library-management-kanya.streamlit.app)")
        with col_b:
            st.markdown("[💻 GitHub](https://github.com/kanyavasudev/Library_Management_System)")

st.write("")

# Project 3 - Ride Booking
with st.container():
    st.markdown("### 🚗 Ride Booking Analysis")
    st.caption("Python | EDA | Jan 2025")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("""
        Exploratory data analysis on **50,000+ ride booking records** to identify 
        demand trends and cancellation patterns.
        
        - Cleaned and structured raw data for analysis  
        - Identified booking trends, peak demand periods, and cancellation drivers  
        - Created visualizations using Pandas and Matplotlib  
        
        **Tools:** Python, Pandas, Matplotlib
        """)
    with col2:
        st.markdown("**What This Shows:**")
        st.info("""
        ✅ Large dataset handling  
        ✅ Data cleaning  
        ✅ Pattern recognition  
        ✅ Visual storytelling  
        """)
        st.markdown("[🔗 View on GitHub](https://github.com/kanyavasudev/Ride-Booking-Analysis-Python-EDA)")

# --- EDUCATION ---
st.write("---")
st.subheader("🎓 Education")
st.markdown("**B.E. Computer Science Engineering** — Saveetha Engineering College")
st.caption("2018 – 2022 | CGPA: 8.15 / 10")

# --- CONTACT ---
st.write("---")
st.subheader("📬 Get In Touch")
st.write(f"📧 {EMAIL}")
st.write(f"[LinkedIn]({SOCIAL_MEDIA['LinkedIn']}) | [GitHub]({SOCIAL_MEDIA['GitHub']})")
st.caption("Open to Business Analyst, Data Analyst, and Analytics roles in Chennai.")
