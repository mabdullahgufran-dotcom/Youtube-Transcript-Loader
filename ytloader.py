# Importing the libraries
import streamlit as st
from langchain_community.document_loaders import YoutubeLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

# Adding the title and input field for the YouTube video link
st.title("YouTube Video Loader")
youtube_link = st.text_input("Enter YouTube Video Link")

# Creating an "Extract Text" button to extract the text from the YouTube video
if st.button("Extract Text"):

# Checks whether the YouTube link box is empty
    if youtube_link == "":
        st.warning("Please enter a YouTube video link.")

# If the code is NOT empty, it will try to extract the text from the YouTube video
    else:
        st.write("YouTube Link:")
        st.write(youtube_link)

# Tries to run the code instead of crashing the app if an error occurs
        try:
            loader = YoutubeLoader.from_youtube_url(
                youtube_link,
                add_video_info=False
            )

# Loads the document
            documents = loader.load()

# Gets the transcript text.
            text = documents[0].page_content

# Shows a smaller heading and Displays the extracted text
            st.subheader("Extracted Text")
            st.write(text)

# Saves the extracted text and shows a success message
            st.session_state["text"] = text
            st.success("Text extracted successfully!")

# Catches any error, shows an error message and error details
        except Exception as e:
            st.error("Could not extract the YouTube transcript.")
            st.write(e)

# Checks if text is saved, creates summary button
if "text" in st.session_state:
    if st.button("Generate Summary"):

# Gets saved transcript
        text = st.session_state["text"]
        api_key = "Your API Key" # Input your API key here

# LLM model
        llm = ChatOpenAI(
            model = "gpt-4o-mini",
            api_key = api_key
        )

        prompt = PromptTemplate.from_template("Summarize the following text. Keep the important points and use simple language. Text: {text} Summary:")

        chain = prompt | llm

        response = chain.invoke({"text": text})

# Summary subheader
        st.subheader("Summary")
        st.write(response.content)

