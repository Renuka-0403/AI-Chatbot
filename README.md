# Lumora AI

### AI-Powered Chatbot using Python, Streamlit and Hugging Face

Lumora AI is a simple AI chatbot built using **Python, Streamlit, and Hugging Face**. It provides an easy-to-use chat interface where users can ask questions and receive AI-generated responses.

---

## Features

- Simple and clean chatbot UI
- AI-powered responses
- Conversation history during the session
- New Chat option
- Clear Chat option
- Hugging Face API integration
- Secure API token handling
- Easy deployment with Streamlit Community Cloud

---

## Technologies Used

- Python
- Streamlit
- Hugging Face
- Hugging Face Inference API

---

## How It Works

Lumora AI follows a simple chatbot workflow:

```text
User
  ↓
Chat Interface
  ↓
Hugging Face Inference API
  ↓
AI Language Model
  ↓
Generated Response
  ↓
User
```

The chatbot connects the Streamlit interface with a Hugging Face hosted language model to generate responses to user queries.

---

## Chatbot Workflow

1. The user enters a question in the Lumora AI chat interface.
2. The user query is sent to the Hugging Face Inference API.
3. The hosted AI language model processes the query.
4. The model generates an AI-powered response.
5. The generated response is displayed in the chatbot interface.
6. Conversation history is maintained during the current session.

---

## AI Capabilities

Lumora AI can be used for:

- Answering general questions
- Generating natural-language responses
- Interactive conversations
- Maintaining conversation context during a session
- Exploring information through an AI-powered chat interface

---

## Hugging Face Integration

Lumora AI uses the **Hugging Face Inference API** to access a hosted language model.

The API connects the Streamlit chatbot interface with the AI model and enables users to receive generated responses without running the model locally.

---

## Security

The Hugging Face API token is handled securely and is not included directly in the application source code.

For local usage, the token is stored using environment variables.

For Streamlit Community Cloud deployment, the token is stored using **Streamlit Secrets**.

Do not upload your `.env` file or Hugging Face token to GitHub.

---

## Deployment

Lumora AI can be deployed using **Streamlit Community Cloud**.

The deployed application provides an interactive web-based chatbot where users can communicate with the AI model through the Streamlit interface.

---

## Chatbot Link

**Live Chatbot:**

https://ai-chatbot-2xmnyxzuntouh7l7xujqbu.streamlit.app/

---

## Future Enhancements

- Multiple chat sessions
- Persistent chat history
- File upload support
- Voice input and output
- Improved response formatting
- Multiple AI model options

---

## About the Project

Lumora AI is a simple Generative AI chatbot project developed using **Python, Streamlit, and Hugging Face**.

The project demonstrates how a web-based interface can be connected to a hosted AI language model to create an interactive conversational application.

---

