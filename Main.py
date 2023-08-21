import streamlit as st
from meta_data_init import define_meta_data
from family_to_charttype import get_chart_types
from front import space

st.markdown("## Meta Data")

file = st.file_uploader("Upload file", type=["ipynb"])
space(2)

if file is not None:

    # define family
    families = ['evolution', 'ranking', 'distribution', 'general', 'correlation', 'partOfAWhole', 'flow']
    family = st.selectbox("family", families)

    # define chartType
    chart_types = get_chart_types(family)
    chartType = st.selectbox("chartType", chart_types)

    # define title
    title = st.text_input("title", "Title")

    # define description
    description = st.text_input("description", "Description")

    # define keywords
    keywords = st.text_input("keywords", "Keywords")

    # define seoDescription
    seoDescription = st.text_input("seoDescription", "SEO Description")

    # define slug using file name
    slug = file.name.split(".")[0]

    # output meta data
    space(2)
    meta_data = define_meta_data(chartType, description, family, keywords, seoDescription, slug, title)
    st.code(meta_data)

