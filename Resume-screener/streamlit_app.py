import streamlit as st

st.title("AI Resume Screening System")

uploaded_files = st.file_uploader(
    "Upload Resume PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:

    st.success(
        f"{len(uploaded_files)} resumes uploaded successfully!"
    )

    for file in uploaded_files:

        st.write("Resume:", file.name)