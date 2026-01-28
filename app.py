import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# ----------------------------------------
# App Config
# ----------------------------------------
st.set_page_config(
    page_title="Medication Adherence AI",
    page_icon="💊",
    layout="centered"
)

st.title("💊 AI-Assisted Medication Adherence Monitoring")

st.write(
    "Describe your recent medication intake behavior. "
    "This system will analyze adherence risk and provide supportive guidance."
)

# ----------------------------------------
# User Input
# ----------------------------------------
user_input = st.text_area(
    "Medication Adherence Input",
    placeholder=(
        "Example:\n"
        "I take my medication twice a day. "
        "I missed two evening doses last week because I forgot."
    ),
    height=150
)

# ----------------------------------------
# Langflow Configuration
# ----------------------------------------
LANGFLOW_URL = (
    "https://api.langflow.astra.datastax.com/"
    "lf/<YOUR_FLOW_ID>/api/v1/run/<YOUR_ENDPOINT_ID>"
)

LANGFLOW_TOKEN = os.getenv("LANGFLOW_API_TOKEN")

if not LANGFLOW_TOKEN:
    st.error("❌ LANGFLOW_API_TOKEN is not set as an environment variable.")
    st.stop()

headers = {
    "Authorization": f"Bearer {LANGFLOW_TOKEN}",
    "Content-Type": "application/json"
}

# ----------------------------------------
# Submit
# ----------------------------------------
if st.button("Analyze Adherence"):
    if not user_input.strip():
        st.warning("⚠️ Please enter medication adherence information.")
        st.stop()

    payload = {
        "input_value": user_input,
        "input_type": "chat",
        "output_type": "chat"
    }

    with st.spinner("Analyzing adherence behavior..."):
        try:
            response = requests.post(
                LANGFLOW_URL,
                headers=headers,
                json=payload,
                timeout=60
            )
            response.raise_for_status()
            data = response.json()

            # ----------------------------------------
            # Extract final agent output text
            # ----------------------------------------
            try:
                final_text = (
                    data["outputs"][0]
                    ["outputs"][0]
                    ["results"]["message"]
                    ["data"]["text"]
                )

                st.success("✅ Analysis Complete")
                st.markdown(final_text)

            except (KeyError, IndexError):
                st.error("❌ Could not parse agent response.")
                st.json(data)

        except requests.exceptions.RequestException as e:
            st.error(f"❌ API Error: {e}")
