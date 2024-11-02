import streamlit as st
import requests

st.title("Keyword Summary Tool using Wikipedia API")
keyword = st.text_input("Enter a keyword to search:")

if st.button("Search") and keyword:
    # Wikipedia API URL for fetching summaries
    url = "https://en.wikipedia.org/api/rest_v1/page/summary/" + keyword
    
    # Fetching the summary
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Display the title and summary
        st.write(f"**{data['title']}**")
        st.write(data['extract'])  # Display the summary text
    else:
        st.write("No information found.")
