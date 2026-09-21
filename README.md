# 🎥 YouTube Video Loader

> 🚀 A simple AI-powered application that extracts text from YouTube videos and generates a concise summary using an LLM.

## ✨ Features

* 🔗 Enter any YouTube video link
* 📝 Extract the available video transcript
* 👀 View the extracted text directly in the app
* 🤖 Generate an AI-powered summary
* ⚡ Simple and easy-to-use Streamlit interface
* 🛡️ Basic error handling for transcript extraction

## 🛠️ Technologies Used

* 🐍 **Python**
* 🎨 **Streamlit**
* 🔗 **LangChain**
* 📚 **LangChain Community**
* 🧠 **LangChain OpenAI**
* ▶️ **YouTube Transcript API**
* 🤖 **OpenAI LLM**

## ⚙️ How It Works

1. 🔗 Enter a YouTube video URL.
2. 📥 Click **Extract Text**.
3. 🧩 LangChain's `YoutubeLoader` loads the video's transcript.
4. 📄 The extracted transcript is displayed in the application.
5. 💾 The transcript is temporarily stored using Streamlit session state.
6. 🤖 Click **Generate Summary**.
7. 🧠 The transcript is sent to the LLM.
8. ✨ The generated summary is displayed on the screen.

## 📦 Installation

Install the required packages using the VS Code terminal:

```bash
py -m pip install streamlit langchain-core==0.3.79 langchain-community==0.3.31 langchain-openai==0.3.35 youtube-transcript-api==1.2.2
```

## ▶️ Running the Project

Run:

```bash
py -m streamlit run ytloader.py
```

🌐 The Streamlit application will open in your web browser.

## 🔑 API Key

The summarization feature requires an OpenAI API key.

Add your API key in the Python file:

```python
api_key = "YOUR_API_KEY"
```

⚠️ **Important:** Never upload your real API key to GitHub. Keep it private.

## 🎯 Project Purpose

This project was created as a learning task to understand how **YouTube transcript extraction, Streamlit, LangChain, and Large Language Models (LLMs)** can work together to create a useful AI-powered application.

## 👨‍💻 Author

**Abdullah Gufran**

⭐ If you found this project interesting, feel free to explore the code and learn from it!
# Youtube-Transcript-Loader
A simple Streamlit-based YouTube Video Loader that extracts transcript text from YouTube videos and uses an LLM to generate a concise summary.

---

# 📸 Media & Files
[ytloader.py](https://github.com/user-attachments/files/32480549/ytloader.py)

## 📁 Project Files

Additional project files and resources will be added here.

> 📂 **Files:**
> Add your files below.

---

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
        api_key = "You API Key" # Input your API key here

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


## 📌 Project Preview

This section contains the visual materials and additional files related to the project, kept separate from the main project documentation.

