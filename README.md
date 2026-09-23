# 🎥 YouTube Video Loader

> 🚀 A simple AI-powered application that extracts text from YouTube videos and generates a concise summary using an LLM.

##  Features

* 🔗 Enter any YouTube video link
* 📝 Extract the available video transcript
* 👀 View the extracted text directly in the app
* 🤖 Generate an AI-powered summary
* ⚡ Simple and easy-to-use Streamlit interface
* 🛡️ Basic error handling for transcript extraction

##  Technologies Used

* 🐍 **Python**
* 🎨 **Streamlit**
* 🔗 **LangChain**
* 📚 **LangChain Community**
* 🧠 **LangChain OpenAI**
* ▶️ **YouTube Transcript API**
* 🤖 **OpenAI LLM**

##  How It Works

1. 🔗 Enter a YouTube video URL.
2. 📥 Click **Extract Text**.
3. 🧩 LangChain's `YoutubeLoader` loads the video's transcript.
4. 📄 The extracted transcript is displayed in the application.
5. 💾 The transcript is temporarily stored using Streamlit session state.
6. 🤖 Click **Generate Summary**.
7. 🧠 The transcript is sent to the LLM.
8. ✨ The generated summary is displayed on the screen.

##  Installation

Install the required packages using the VS Code terminal:

```bash
py -m pip install streamlit langchain-core==0.3.79 langchain-community==0.3.31 langchain-openai==0.3.35 youtube-transcript-api==1.2.2
```

##  Running the Project

Run:

```bash
py -m streamlit run ytloader.py
```

 The Streamlit application will open in your web browser.

##  API Key

The summarization feature requires an OpenAI API key.

Add your API key in the Python file:

```python
api_key = "YOUR_API_KEY"
```

 **Important:** Never upload your real API key to GitHub. Keep it private.

##  Author
**Abdullah Gufran**

---

