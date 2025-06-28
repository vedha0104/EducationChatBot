from transformers import pipeline
import streamlit as st

#  To Load QA pipeline
qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

st.title("📚 EduBot: Ask Me Anything!")

context = st.text_area("Paste some context (e.g., your textbook content)")
question = st.text_input("Ask a question:")

if st.button("Get Answer") and context and question:
    result = qa_pipeline(question=question, context=context)
    st.markdown("**Answer:**")
    st.write(result["answer"])
