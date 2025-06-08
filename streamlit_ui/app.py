import streamlit as st
import requests

st.title("AI Science Papers Assitant for arxiv.org")

symptom_input = st.text_area("Share your Science Topic")

if st.button("Get Analysis"):
    state_input = {
                "input" : symptom_input,
                "field_area" : "",
                "summary" : ""
    }

    try:
        response = requests.post(
            #"http://localhost:8000/diagnose/invoke",
            "https://ai-scien.onrender.com/diagnose/invoke",
            headers={"Content-Type": "application/json"},
            json={"input": state_input}  # ✅ wrap state in "input"
        )

        data = response.json()
        st.write("DEBUG Raw JSON:", data)  # Optional debug

        #st.subheader("Science Topic Found:")
        #st.write(data.get("field_area", "N/A"))

        #st.subheader("AI Summary on Research papers from arix")
        #st.write(data.get("summary", "N/A"))

    except Exception as e:
        st.error(f"Failed to get diagnosis: {e}")
