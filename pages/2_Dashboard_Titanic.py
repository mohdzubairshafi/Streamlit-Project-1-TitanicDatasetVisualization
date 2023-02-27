import streamlit as st
from matplotlib import image
import os
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")
IMAGE_PATH = os.path.join(dir_of_interest, "images", "titanic.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "titanic.csv")

img = image.imread(IMAGE_PATH)


df = pd.read_csv(DATA_PATH)

header = st.container()
datasets = st.container()
features = st.container()
overallVisuals = st.container()

with header:
    st.title("Dashboard - Titanic Data")
    st.image(img)

with datasets:
    st.title("Titanic- DataSets")
    df.fillna(method="ffill", inplace=True)
    st.dataframe(df)

with features:
    st.title("Town Specific Data Visualization")
    embark_town = st.selectbox("Select the Location:", df["embark_town"].unique())
    col1, col2, col3, col4 = st.columns(4)

    # Gender
    col1.subheader("Gender")
    fig_1 = px.histogram(df[df["embark_town"] == embark_town], x="sex")
    col1.plotly_chart(fig_1, use_container_width=True)
    # Survived
    col2.subheader("Survived")
    fig_2 = px.histogram(df[df["embark_town"] == embark_town], x="survived")
    col2.plotly_chart(fig_2, use_container_width=True)
    # Who
    col3.subheader("Who")
    fig_3 = px.histogram(df[df["embark_town"] == embark_town], x="who")
    col3.plotly_chart(fig_3, use_container_width=True)
    # Class
    col4.subheader("Class")
    fig_4 = px.histogram(df[df["embark_town"] == embark_town], x="class")
    col4.plotly_chart(fig_4, use_container_width=True)

    st.title("Comparison")
    st.subheader("who Survived from given Town!!")

    fig_5 = px.histogram(df[df["embark_town"] == embark_town], x="who", y="survived")
    st.plotly_chart(fig_5, use_container_width=True)


with overallVisuals:
    st.title("Overall - Visualization")
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)
    col5, col6 = st.columns(2)

    # Gender
    col1.subheader("Gender")
    col1.bar_chart(df["sex"].value_counts())

    # Class
    col2.subheader("Class")
    col2.bar_chart(df["class"].value_counts())

    # Survived
    col3.subheader("Survived")
    col3.bar_chart(df["survived"].value_counts())

    # Embark_town
    col4.subheader("Embark town")
    col4.bar_chart(df["embark_town"].value_counts())

    # Who
    col5.subheader("Who")
    col5.bar_chart(df["who"].value_counts())

    # age
    col6.subheader("Age")
    col6.bar_chart(df["age"].sample(20))
