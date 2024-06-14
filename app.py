import streamlit as st
from search.chain import chains  # Import the combined chain from chain.py

# # Accessing the environment variables
# LANGCHAIN_API_KEY = st.secrets["LANGCHAIN_API_KEY"]
# GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
# TAVILY_API_KEY = st.secrets["TAVILY_API_KEY"]
# LANGCHAIN_PROJECT = st.secrets["LANGCHAIN_PROJECT"]

# Page configuration
st.set_page_config(page_title="Research Assistant", page_icon=":mag:", layout="wide")

# Custom CSS for additional styling
st.markdown(
    """
    <style>
    .reportview-container {
        background: #ffffff;
        color: #333333;
    }
    .sidebar .sidebar-content {
        background: #f9f9f9;
        color: #333333;
    }
    .sidebar .sidebar-title {
        color: #003366;
        font-weight: bold;
        font-size: 24px;
    }
    .sidebar .sidebar-markdown {
        color: #336699;
        font-size: 16px;
    }
    .title {
        text-align: center;
        color: #003366;
        font-weight: bold;
        font-family: 'Arial', sans-serif;
    }
    .input-field {
        margin-bottom: 20px;
    }
    .illustration {
        text-align: center;
        margin-bottom: 20px;
    }
    .result-container {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin-top: 20px;
    }
    .about-content {
        margin: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Navigation options
page = st.sidebar.selectbox("Navigate", ["Home", "About"])

if page == "Home":
    # Main content
    st.markdown('<h1 class="title">Research Assistant</h1>', unsafe_allow_html=True)
    # st.markdown("This tool helps you find answers to your research questions. Simply enter your question below and click 'Submit'.")

    # Input section
    question = st.text_input(" ", placeholder="Enter your doubt/Query:", key="question_input",
                             help="Enter your doubt/Query", type="default")

    # Submit button
    if st.button("Submit", key="submit_button"):
        if question:
            with st.spinner("Processing your question..."):
                input_data = {"question": question}
                result = chains.invoke(input_data)  # Use the combined chain
                st.success("Here's the answer to your question:")
                st.write(result)
        else:
            st.warning("Please enter a question.")

elif page == "About":
    st.markdown('<h1 class="title">About Research Assistant</h1>', unsafe_allow_html=True)
    st.markdown("""
    ### What is this tool?
    The Research Assistant is a powerful tool designed to help you with your research by providing accurate and relevant answers to your questions. It leverages state-of-the-art machine learning and natural language processing technologies.

    ### How does it work?
    This tool is powered by a large language model (LLM) Agent developed using LLAMA-3 with GROQ's LPU and servers. 

    ### Benefits for Researchers
    - **Quick Answers:** Get immediate answers to your research questions. As by using GROQ's LPU ( language processing unit ) , LLM responses are super fast , fastest in market
    - **Accurate Information:** Leverage the power of advanced AI to get reliable information.
    - **Ease of Use:** Simple interface that allows you to input your questions and get answers with ease.
    """)

# Create an expander for the "Research Assistant" section in the sidebar
with st.sidebar.expander("How to Use"):
    st.markdown("""
    Use this tool to get answers to your research questions. Enter your question in the text box below and click "Submit" to get started.
    """)

    # Add the science flask illustration beside the text
    st.markdown('<div style="display: flex; align-items: center;">'
                '<span>Use this tool to get answers to your research questions. Enter your question in the text box below and click "Submit" to get started.</span>'
                '<img src="https://th.bing.com/th/id/OIP.vFkTHeEKCojrk3gbVeyZ-wAAAA?rs=1&pid=ImgDetMain" alt="Science Flask" width="50">'
                '</div>',
                unsafe_allow_html=True)

# # Adding the illustration to the sidebar
# st.sidebar.markdown("""
# <div class="illustration">
#     <img src="https://th.bing.com/th/id/OIP.vFkTHeEKCojrk3gbVeyZ-wAAAA?rs=1&pid=ImgDetMain" alt="Science Flask" width="50">
#     <img src="https://clipground.com/images/atom-clipart-6.jpg" alt="Atom" width="50">
#     <img src="https://static.vecteezy.com/system/resources/previews/000/139/901/original/geometry-and-mathematics-tool-set-vector.jpg" alt="Mathematics" width="50">
# </div>
# """, unsafe_allow_html=True)


# Footer in the sidebar
st.sidebar.markdown("---")

# Create an expander for the "Developed by" section in the sidebar
with st.sidebar.expander("Developed by"):
    st.markdown("**Abhishek Vidhate**")
    st.markdown(
        "[LinkedIn](https://www.linkedin.com/in/abhishek-vidhate-21smdb/) | [GitHub](https://github.com/Abhishekvidhate)")

    # Include the atom image inside the expander
    st.markdown('<div class="illustration" style="text-align: center;">'
                '<img src="https://clipground.com/images/atom-clipart-6.jpg" alt="Atom" width="50"></div>',
                unsafe_allow_html=True)
