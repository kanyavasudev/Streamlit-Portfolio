from pathlib import Path
import streamlit as st

from PIL import Image 

#---Path Settings---
current_dir=Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir/"styles"/"main.css"
resume_file=current_dir/"assests"/"Kanya_Resume_Final.pdf"
profile_pic=current_dir/"assests"/"kanya_profile_pic.png"


# --- GENERAL SETTINGS ---

PAGE_TITLE = "Portfolio | Kanya V"
PAGE_ICON = "👋"

NAME = "Kanya V"

DESCRIPTION = """
Junior Data Analyst with 2+ years of experience in reporting, KPI tracking,
and performance analysis, supported by a background in digital marketing.

Experienced in gathering business requirements, preparing reports,
analyzing performance data, and supporting data-driven decision-making.
Currently upskilling in SQL, Power BI, and Python through hands-on projects.
"""

EMAIL = "kanyavasu7@gmail.com"

SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com/in/kanya-v",
    "GitHub": "https://github.com/kanyavasudev",
}

PROJECTS = {
    """
    🏆 Ride Booking Analysis (Python EDA)-Exploratory data analysis 
    on 50,000+ ride booking records to identify booking trends and cancellation patterns. 
    Used data cleaning, handling missing values, and visualizations.""": "https://github.com/kanyavasudev/Ride-Booking-Analysis-Python-EDA"
} 

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)



#---Load CSS, PDF & PROFILE PIC---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte=pdf_file.read()
profile_pic=Image.open(profile_pic)


#---HERO SECTION---
col1,col2=st.columns(2, gap="small")
with col1:
    st.image(profile_pic,width=350)

with col2:
    st.markdown(f"## {NAME}")
    st.write(DESCRIPTION)
    st.download_button(
        label="Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
         type="primary",
    )
    st.markdown(f"""
    📧 {EMAIL}  
    [LinkedIn]({SOCIAL_MEDIA['LinkedIn']}) &nbsp; | &nbsp;
    [GitHub]({SOCIAL_MEDIA['GitHub']})
    """)

#---Experience & Qualifictaion---
st.write("#")
st.subheader("Experience & Qualifications")
st.write(
"""
✔ Experience in reporting, KPI tracking, and performance analysis using Excel and Google Sheets  
✔ Hands-on experience gathering business requirements and converting them into reports  
✔ Worked with real business and marketing data to support decision-making  
✔ Experience analyzing paid ads and campaign performance metrics  
✔ Practical exposure to Python for data cleaning and exploratory data analysis  
✔ Basic working knowledge of SQL and Power BI through hands-on projects  
✔ Strong communication skills from client and stakeholder interactions  
"""
)
#--Skills--
st.write("\n")
st.subheader("Technical Skills")
st.write(
"""
✔ Excel & Google Sheets (Pivot Tables, VLOOKUP, Data Cleaning)   
✔ SQL
✔ Python (Pandas, NumPy, Matplotlib – EDA)  
✔ Power BI (Basic dashboard creation)  
✔ GA4 & Marketing Analytics  
✔ Requirement Gathering & Stakeholder Communication  
"""
)

#---Work history
st.write('#')
st.subheader("Professional Experience")
st.write("---")
#---Job1---
st.write("**Freelance Data Analyst & Marketing Consultant**")
st.write("*May 2025 – Present | Chennai, India*")
st.write("""
- Worked with multiple clients to gather business requirements and define reporting needs  
- Analyzed paid ads and campaign performance to track leads, reach, and ROI  
- Built Excel trackers and weekly KPI dashboards for monitoring performance  
- Presented insights and recommendations to business owners to support decision-making  
""")

#---JOB2---
st.write("**Digital Marketing Executive – Reporting & KPI Analysis**")
st.write("*Jan 2024 – Mar 2025 | StrongBox IT, Chennai*" )
st.write("""
- Maintained GA4 reports and tracked 15+ KPIs across traffic, engagement, and conversions  
- Prepared monthly performance reports and shared insights with internal teams  
- Improved organic website traffic through data-driven SEO analysis  
- Conducted competitor benchmarking using Excel to support lead generation  
""")

#---JOB3--
st.write("**Digital Marketing Intern – Data Tracking & Reporting**")
st.write("*Jul 2023 – Dec 2023 | StrongBox IT, Chennai*")
st.write("""
- Cleaned and validated large datasets to improve reporting accuracy  
- Supported weekly reporting by summarizing social media performance trends 
""")
#---Projects & Accomplishments---
st.write("#")
st.subheader("Projects")
st.write("---")
for project,link in PROJECTS.items():
    st.write(f"[{project}]({link})")

st.write("Hello")
