📚 EduBot – Your AI Study Buddy
EduBot is a lightweight, interactive question-answering chatbot built using Streamlit and Hugging Face Transformers. It helps students get answers to questions based on textbook content or custom study material.
🚀 Features
-📖 Paste your context (notes, textbook excerpts, PDFs)
-❓ Ask any question based on that context
-🤖 Get accurate answers using a fine-tuned QA model
-⚡ Simple, fast, and offline-friendly
->🛠️ Tech Stack
1,Python
2,Streamlit (UI)
3,Transformers from Hugging Face
4,Model: distilbert-base-uncased-distilled-squad (lightweight & accurate)
📂 File Structure
bash
Copy
Edit
EduBot_QA/
│
├── EduBot_QA.py
├── requirements.txt
└── README.md
✅ Requirements
-Python 3.8+
-pip
Install dependencies:
bash
Copy
Edit
pip install -r requirements.txt
To Run the app:
streamlit run EduBot_QA.py
🧠 How to Use
Paste your study material in the text area (e.g., a paragraph about Bayes' Theorem)
Ask a question like:
"What is Bayes' Theorem used for?"
Click "Get Answer" to receive an instant, AI-generated response.
📌 Notes
The model only answers based on the context you provide.
It does not fetch from the internet — so keep context relevant.
First run may take a few seconds to load the model.
📜 Example
Context:
Bayes' Theorem is a formula used to calculate conditional probabilities. It is based on prior knowledge of related events.
Question:
What does Bayes' Theorem calculate?
Answer:
Conditional probabilities
🧠 Future Improvements
PDF/Textbook file upload for auto-context
Chat history
OpenAI/GPT-4 fallback for broader knowledge
Speech-to-text questions
🙌 Credits
->Built with ❤️ by Vedha
->Powered by 🤖 Hugging Face Transformers
->UI built using Streamlit
