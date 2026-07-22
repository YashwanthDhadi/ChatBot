# 🤖 Groq AI Chatbot

A modern AI chatbot built with **Streamlit** and powered by **Groq's ultra-fast Llama models**. This application provides a clean conversational interface with customizable model settings, real-time responses, and persistent chat history during each session.

---

## 🚀 Features

* ⚡ Powered by Groq's high-speed inference engine
* 🤖 Supports multiple Llama models
* 💬 Interactive chat interface using Streamlit
* 🌡 Adjustable temperature for response creativity
* 📏 Configurable maximum response length
* 🗑 One-click chat history reset
* 🔐 Secure API key management using environment variables
* 🎨 Simple, responsive, and user-friendly UI

---

## 🛠 Tech Stack

* **Python 3.11+**
* **Streamlit**
* **Groq Python SDK**
* **python-dotenv**

---

## 📂 Project Structure

```text
Groq-AI-Chatbot/
│
├── app.py              # Main Streamlit application
├── .env                # Stores Groq API Key (not committed)
├── requirements.txt    # Project dependencies
├── README.md           # Project documentation
└── .gitignore          # Files ignored by Git
```

---

## ⚙ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Groq-AI-Chatbot.git

cd Groq-AI-Chatbot
```

---

### 2. Create a Virtual Environment (Recommended)

**Windows**

```bash
python -m venv venv

venv\Scripts\activate
```

**macOS/Linux**

```bash
python3 -m venv venv

source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_groq_api_key_here
```

---

### 5. Run the Application

```bash
streamlit run app.py
```

The application will launch automatically in your default web browser.

---

## 📦 Requirements

Example `requirements.txt`

```text
streamlit
groq
python-dotenv
```

---

## 🖥 Supported Models

The chatbot currently supports:

* Llama 3.1 8B Instant
* Llama 3.1 70B Versatile

Additional Groq-supported models can be added easily by updating the model selection list.



## 🔒 Security

* API keys are stored securely using a `.env` file.
* Never commit your `.env` file to GitHub.
* Ensure `.env` is included in your `.gitignore`.

Example:

```text
.env
venv/
__pycache__/
```

---

## 📈 Future Improvements

* Conversation export (PDF / TXT)
* Streaming responses
* Dark mode support
* File upload and document Q&A
* Voice input and speech synthesis
* Conversation memory
* Multiple AI model support
* Chat history persistence
* Authentication and user accounts


## 👨‍💻 Author

**Yashwanth Dhadi**

* AI & Machine Learning Enthusiast
* Python Developer
* Generative AI Explorer

GitHub: https://github.com/YashwanthDhadi

