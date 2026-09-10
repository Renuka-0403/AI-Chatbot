import streamlit as st
from huggingface_hub import InferenceClient

HF_TOKEN = st.secrets["HF_TOKEN"]

client = InferenceClient(
    api_key=HF_TOKEN
)

st.set_page_config(
    page_title="Lumora AI",
    page_icon="✨",
    layout="wide"
)

st.markdown("""
<style>

.stApp {
    background: #f6f7fb;
}

.block-container {
    max-width: 1050px;
    padding-top: 2rem;
    padding-bottom: 6rem;
}

.header {
    background: linear-gradient(135deg, #6c63ff, #857cff);
    padding: 28px 32px;
    border-radius: 20px;
    color: white;
    margin-bottom: 28px;
    box-shadow: 0 8px 25px rgba(108, 99, 255, 0.18);
}

.header h1 {
    margin: 0;
    font-size: 34px;
    font-weight: 700;
}

.header p {
    margin: 8px 0 0 0;
    font-size: 15px;
    opacity: 0.9;
}

.welcome {
    background: white;
    padding: 38px 30px;
    border-radius: 20px;
    text-align: center;
    border: 1px solid #e9e9ee;
    margin-bottom: 25px;
}

.welcome-icon {
    font-size: 42px;
    margin-bottom: 8px;
}

.welcome h2 {
    margin: 0;
    color: #292b38;
    font-size: 25px;
}

.welcome p {
    color: #777;
    margin-top: 8px;
}

.suggestion {
    background: white;
    padding: 20px;
    border-radius: 16px;
    border: 1px solid #e9e9ee;
    min-height: 90px;
    color: #444;
}

.suggestion-title {
    font-weight: 600;
    color: #292b38;
    margin-bottom: 6px;
}

.suggestion-text {
    font-size: 14px;
    color: #777;
}

.user-message {
    background: #6c63ff;
    color: white;
    padding: 13px 17px;
    border-radius: 18px 18px 4px 18px;
    margin: 10px 0 10px auto;
    max-width: 72%;
    width: fit-content;
    font-size: 15px;
    line-height: 1.5;
}

.ai-message {
    background: white;
    color: #333;
    padding: 13px 17px;
    border-radius: 18px 18px 18px 4px;
    border: 1px solid #e9e9ee;
    margin: 10px auto 10px 0;
    max-width: 72%;
    width: fit-content;
    font-size: 15px;
    line-height: 1.5;
}

[data-testid="stSidebar"] {
    background: white;
    border-right: 1px solid #eeeeee;
}

.sidebar-title {
    font-size: 24px;
    font-weight: 700;
    color: #292b38;
}

.sidebar-subtitle {
    color: #777;
    font-size: 14px;
}

.info-box {
    background: #f6f7fb;
    padding: 16px;
    border-radius: 12px;
    font-size: 14px;
    color: #555;
}

.stButton button {
    border-radius: 10px;
    height: 40px;
    font-weight: 500;
}

</style>
""", unsafe_allow_html=True)

client = InferenceClient(
    api_key=HF_TOKEN,
    provider="auto"
)

MODEL = "openai/gpt-oss-120b"

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:

    st.markdown(
        '<div class="sidebar-title">Lumora AI</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-subtitle">Your AI conversation assistant</div>',
        unsafe_allow_html=True
    )

    st.divider()

    if st.button("➕ New Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    if st.button("Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.divider()

    st.markdown("### About Lumora")

    st.markdown(
        """
        <div class="info-box">
        Lumora AI is a simple conversational application
        built with Streamlit and Hugging Face.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown("### Technology")

    st.write("Streamlit")
    st.write("Hugging Face")
    st.write("Inference Providers")
    st.write("Python")

    st.divider()

    st.caption("Powered by Hugging Face")

st.markdown(
    """
    <div class="header">
        <h1>Lumora AI</h1>
        <p>Ask questions, explore ideas and have a conversation with your AI assistant.</p>
    </div>
    """,
    unsafe_allow_html=True
)

if len(st.session_state.messages) == 0:

    st.markdown(
        """
        <div class="welcome">
            <div class="welcome-icon">✨</div>
            <h2>Welcome to Lumora AI</h2>
            <p>How can I help you today?</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div class="suggestion">
                <div class="suggestion-title">Learn Something</div>
                <div class="suggestion-text">
                    Ask questions about a topic you want to understand.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="suggestion">
                <div class="suggestion-title">Get Ideas</div>
                <div class="suggestion-text">
                    Explore creative ideas and possible solutions.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """
            <div class="suggestion">
                <div class="suggestion-title">Programming</div>
                <div class="suggestion-text">
                    Ask questions about programming and technology.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

for message in st.session_state.messages:

    if message["role"] == "user":

        st.markdown(
            f"""
            <div class="user-message">
                👤 {message["content"]}
            </div>
            """,
            unsafe_allow_html=True  
        )

    else:

        st.markdown(
            f"""
            <div class="ai-message">
                🤖 {message["content"]}
            </div>
            """,
            unsafe_allow_html=True
        )

user_input = st.chat_input("Message Lumora AI...")

if user_input:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    st.markdown(
        f"""
        <div class="user-message">
            👤 {user_input}
        </div>
        """,
        unsafe_allow_html=True
    )

    messages = [
        {
            "role": "system",
            "content": "You are Lumora AI, a helpful, friendly and knowledgeable assistant. Give clear and accurate answers. Keep answers easy to understand."
        }
    ]

    messages.extend(st.session_state.messages)

    with st.spinner("Lumora AI is thinking..."):

        try:

            response = client.chat.completions.create(
                model=MODEL,
                messages=messages,
                max_tokens=500,
                temperature=0.7
            )

            answer = response.choices[0].message.content

        except Exception as e:

            answer = f"Sorry, I couldn't generate a response. Error: {e}"
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )
    st.markdown(
        f"""
        <div class="ai-message">
            🤖 {answer}
        </div>
        """,
        unsafe_allow_html=True
    )
