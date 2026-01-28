# 💊 AI-Assisted Medication Adherence Monitoring System

An intelligent AI-powered system that helps monitor and improve medication adherence for patients with chronic diseases.

## 🎯 Overview

This application leverages **IBM Granite Model** through **LangFlow** to analyze medication adherence patterns and provide supportive guidance to patients and healthcare providers.

### Key Features

- **Adherence Analysis** – Analyze medication intake behavior and identify risk patterns
- **Risk Detection** – Identify declining adherence trends using AI-powered analysis
- **Educational Support** – Provide helpful reminders and lifestyle guidance (non-diagnostic)

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **Streamlit** | Interactive web interface |
| **LangFlow** | AI workflow orchestration |
| **IBM Granite Model** | Large Language Model for analysis |
| **RAG** | Retrieval-Augmented Generation for best practices |

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- LangFlow API Token

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/NitinHarsur/Medication_Adherence.git
   cd Medication_Adherence
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install streamlit python-dotenv requests
   ```

5. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```
   LANGFLOW_API_TOKEN=your_langflow_api_token_here
   ```

6. **Run the application**
   ```bash
   streamlit run app.py
   ```

7. **Open your browser** and navigate to `http://localhost:8501`

## 📖 Usage

1. Enter your medication adherence information in the text area
2. Click "Analyze Adherence" button
3. Receive AI-powered analysis and supportive guidance

## ⚠️ Disclaimer

This system is **assistive only** and is **not intended for diagnostic purposes**. Always consult healthcare professionals for medical advice.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👥 Team

Built for the IBM Hackathon 2026
