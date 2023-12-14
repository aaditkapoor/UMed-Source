from openai import OpenAI
import streamlit as st
from neighbors import *

# if using openai.api_key = os.environ["OPENAI_API_KEY"]
train_dataset = {
    "inlier": [
        "Stay hydrated; drink at least eight glasses of water daily for optimal health.",
        "Engage in regular exercise to maintain cardiovascular health and boost immunity.",
    "Prioritize sleep; aim for 7-8 hours nightly for mental and physical rejuvenation.",
    "Adopt a balanced diet rich in fruits, vegetables, and lean proteins for overall wellness.",
        "Regular health check-ups are crucial for early detection and management of diseases",
        "Text about medical knowledge",
    ],
    "outlier": [
        "Text about kitchen equipment",
        "This text is about politics",
        "Couches, benches and televisions.",
        "I really need to get a new sofa.",
        "Texts not related to medical knowledge",

    ]
}
# Finds the probability if the response is medical information or not
def find_prob(chat_response):
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=f"Classify any text that talks about medical knowledge or gives medical advice as positive otherwise negative. Positive texts contain something related to medicine or some type of medical terms. The classification should only be negative or positive.\n\nTexts:{chat_response}\nClassification:",
    temperature=1,
        max_tokens=8,
    top_p=1,
         frequency_penalty=0,
    presence_penalty=0,
        stop=["\\n"]
        )
    return response.choices[0].text.strip()


class PromptMaker:
    def __init__(self, medical_practice="General Health"):
        self.medical_practice = medical_practice
    def create_initial_prompt(self):
            return f"""You are an expert in {self.medical_practice} and answer almost any query regarding the same.Introduce yourself as an expert in {self.medical_practice}
            """

st.title("UMed: Personalized Medicine for All")
st.image("background.png", width=300)
st.sidebar.info("""
        Medical Report: Upload personalized medical report (if required)\n
        Medical Practice: Change "medicine practice" to desired consultation
        """)
client = OpenAI(api_key="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")

# Sidebar for file upload
with st.sidebar:
    uploaded_file = st.file_uploader("Upload your medical report", type=["pdf", "jpg", "png", "txt"])
    if uploaded_file is not None:
        # You can use the uploaded file here
        st.write("File uploaded successfully!")

    # Dropdown for selecting medical practice
    medical_practice = st.selectbox(
        "Choose your Medical Practice Area",
        ["General Health", "Heart Health", "Diet Recommendations"]
    )
    # RAG for each medical practice
    st.write(f"Welcome to {medical_practice}")
    promptmaker = PromptMaker(medical_practice=medical_practice)
    initial_prompt = promptmaker.create_initial_prompt()

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])



if prompt := st.chat_input("How is my Health?"):
    # match nearest neighbors with general, cardiac, diet

    if medical_practice == "General Health":
        df = pd.read_csv("embedded_general_medical.csv")
        if medical_practice == "Heart Health":
            df = pd.read_csv("embedded_cardiac_practice.csv")
        if medical_practice == "Diet Recommendations":
            df = pd.read_csv("embedded_diet_practice.csv")
            
    context = find_closest_match(df, prompt, n=1)
    st.session_state.messages.append({"role": "user", "content": f"{initial_prompt} ' ' + {prompt} + Context: {context}"})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        for response in client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        ):
            full_response += (response.choices[0].delta.content or "")
            message_placeholder.markdown(full_response + "▌")
        
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})
