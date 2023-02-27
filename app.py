import streamlit as st
from pathlib import Path


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "resources" / "styles" / "main.css"

# --- SETTING VARIABLES ---
PAGE_TITLE = "Streamlit Portfolio"
PAGE_ICON = ":wave:"
NAME = "Mohd Zubair"
DESCRIPTION = """
            junior Data Scientist , Full-Stack Developer 
            experience working with Python ,C++,Java , JavaScript, HTML/CSS, ReactJS

"""

SOCIAL_MEDIA = {
    "GitHub": "https://github.com/mohdzubairshafi",
    "Linkedin": "https://www.linkedin.com/in/mohdzubairansari",
    "Portfolio": "https://github.com/mohdzubairshafi",
}
PROJECTS = {
    "Weather-app": "http://weather-app-rust-eta.vercel.app/",
    "Github-Profile-Finder": "http://github-finder-app-seven-sigma.vercel.app/",
    "Flower-Image-Classifier": "https://github.com/mohdzubairshafi",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# ---- LOADING CSS ,PDF & PROFILE PIC----

with open(css_file) as f:
    st.markdown("<style>{}<style>".format(f.read()), unsafe_allow_html=True)


# ---- HERO SECTION ----

st.title(NAME)
st.write(DESCRIPTION)

# ---- SOCIAL LINKS -----

st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# ---- EXPERIENCE & QUALIFICATIONS ----
st.write("#")
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ 1 year experience in Full-Stack Development 
- ✔️ Strong hand on experience and knowledge in Js , Python And C++  
- ✔️ Good UnderStanding of DSA 
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)

# ---- SKILLS ----
st.write("#")
st.subheader("Hard Skills")
st.write(
    """
    - 👨‍💻️ Programming: C++ ,JS, Python  
    - 📊 Data Visualization: Matplotlib
    - 📚 Modeling: Logistic regression, linear regression ,decision trees
    - 📄 Database: MongoDB  
    """
)

# ---- INTERNSHIP ----
st.write("#")
st.subheader("Internships")
st.write("----")

# --- Internship 1
st.write("🏢 Innomatics Research Labs")
st.write("Data Science & Full-Stack Development")
st.write("Feb 2023 - Present")

# --- Internship 2
st.write("🏢 GGSIP University USS ACM Student Chapter")
st.write("Full-Stack Development")
st.write("Dec 2022 - Present")


# --- Projects & Accomplishments ----
st.write("#")
st.subheader("Projects & Accomplishments")
st.write("---")

for projects, link in PROJECTS.items():
    st.write(f"[{projects}]({link})")
