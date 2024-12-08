import streamlit as st
import pandas as pd
from transformers import pipeline
from io import StringIO
import base64

st.set_page_config(
    page_title="Email Classifier",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("Email Content Classifier")

st.markdown("""
This application automatically classifies your email contents into categories such as **Priority**, **Updates**, **Promotions**, and more.
Regardless of the structure of your CSV file, you can select the column you want to use for classification.
""")

@st.cache_resource
def load_classifier():
    classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
    return classifier

classifier = load_classifier()

st.sidebar.header("1. Upload Your CSV File")
uploaded_file = st.sidebar.file_uploader("Select a CSV file containing email contents", type=["csv"])

if uploaded_file is not None:
    try:
        st.sidebar.header("Delimiter Settings")
        delimiter = st.sidebar.selectbox(
            "Select the delimiter used in your CSV file",
            options=[",", ";", "\t", "|", ":"],
            index=0,
            help="Choose the delimiter that separates your CSV file columns."
        )
        
        df = pd.read_csv(uploaded_file, delimiter=delimiter)
        st.sidebar.success("CSV file successfully uploaded and read!")

        st.sidebar.header("2. Configure Settings")
        all_columns = df.columns.tolist()

        email_column = st.sidebar.selectbox(
            "Select the column containing email content",
            options=all_columns,
            index=0
        )

        candidate_labels = st.sidebar.text_input(
            "Candidate Labels (separated by commas)", 
            value="Priority,Updates,Promotions"
        ).split(",")

        candidate_labels = [label.strip() for label in candidate_labels if label.strip()]

        threshold = st.sidebar.slider(
            "Threshold Value",
            min_value=0.0,
            max_value=1.0,
            value=0.5,
            step=0.05
        )

        if st.sidebar.button("Classify"):
            with st.spinner("Classifying emails..."):
                def classify(text):
                    if pd.isna(text):
                        return "Unclassified"
                    result = classifier(text, candidate_labels)
                    top_label, top_score = result['labels'][0], result['scores'][0]
                    return top_label if top_score >= threshold else "Unclassified"

                df['Category'] = df[email_column].apply(classify)

            st.success("Classification completed!")

            st.subheader("Classified Emails")
            st.dataframe(df)

            def convert_df_to_csv(df):
                return df.to_csv(index=False).encode('utf-8')

            csv = convert_df_to_csv(df)
            st.download_button(
                label="Download Results as CSV",
                data=csv,
                file_name='classified_emails.csv',
                mime='text/csv',
            )
    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.info("Please upload a CSV file from the sidebar.")

st.markdown("""
---
**Note:** The classification is performed using the `facebook/bart-large-mnli` model. You can adjust the candidate labels and threshold value according to your needs.
""")
