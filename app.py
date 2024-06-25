import streamlit.components.v1 as components
import streamlit as st
from bs4 import BeautifulSoup
import requests

st.set_page_config(page_title='Bypass', layout='wide')

st.markdown("""
    <style>
    .stApp {
        background-color: #0D1016;
        color: white;
    }
    .title {
        font-size: 3em;
        color: white;
        text-align: center;
        margin-top: 20px;
        margin-bottom: 30px;
    }
    .subtitle {
        text-align: center;
        color: white;
        margin-bottom: 20px;
    }
    .input-box {
        display: flex;
        justify-content: center;
        margin-bottom: 10px;
    }
    .button-container {
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }
    .expander {
        background-color: #1E1E1E;
        border: 1px solid #333;
        border-radius: 5px;
        padding: 10px;
        color: white;
    }
    .download-button {
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }
    .expander .streamlit-expanderHeader {
        color: white;
    }
    .stDownloadButton button {
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Page title and subtitle
st.markdown("<div class='title'>Bypass</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Extracting HTML content</div>", unsafe_allow_html=True)

# Input box for URL
st.markdown("<div class='input-box'>", unsafe_allow_html=True)
input_url = st.text_input("Enter URL:", key="input_url")
st.markdown("</div>", unsafe_allow_html=True)

def bypass_paywall(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    script_tag = soup.find("script", text="window.main();")
    if script_tag:
        script_tag.extract()
    html = str(soup)
    html_start = html.find("<html")
    if html_start != -1:
        html = html[html_start:]
    else:
        return "No <html> tag found in the HTML content."
    return html

# Fetch HTML button
st.markdown("<div class='button-container'>", unsafe_allow_html=True)
if st.button("Fetch HTML"):
    if input_url:
        base_url = 'https://webcache.googleusercontent.com/search?q=cache:'
        full_url = base_url + input_url + '&strip=0&vwsrc=0'

        st.write(f"Fetching content from: {full_url}")

        response = requests.get(full_url)

        if response.status_code == 200:
            html_content = response.text
            bypassed_content = bypass_paywall(html_content)

            st.markdown("<div class='expander'>", unsafe_allow_html=True)
            with st.expander("Show Content"):
                components.html(bypassed_content, width=1280, height=700, scrolling=True)
            st.markdown("</div>", unsafe_allow_html=True)

            st.markdown("<div class='download-button'>", unsafe_allow_html=True)
            st.download_button(
                label="Download Content",
                data=bypassed_content,
                key="download",
                file_name="content.html",
            )
            st.markdown("</div>", unsafe_allow_html=True)

        else:
            st.error(f"Failed to retrieve the page. Status code: {response.status_code}")
    else:
        st.warning("Please enter a URL.")
st.markdown("</div>", unsafe_allow_html=True)
