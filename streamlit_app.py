import streamlit as st
import requests

# Function to call the Flask API
def classify_text(text):
    url = 'http://localhost:5000/api/text'  # Change the URL if your Flask app is hosted elsewhere
    payload = {'text': text}
    response = requests.post(url, json=payload)
    
    if response.status_code == 200:
        result = response.json()
        return result
    else:
        return {'status': -1, 'message': 'Error: Failed to connect to the API'}

# Streamlit app code
def main():
    st.title("Toxic Comment Classification")

    # Input text area
    text = st.text_area("Enter your comment here:")
    if st.button("Classify"):
        if text:
            # Call API and display result
            result = classify_text(text)
            if result['status'] == 1:
                toxicity_info = result['response']
                labels = []
                for label, value in toxicity_info.items():
                    if value:
                        labels.append(label)
                st.success("Toxicity labels: {}".format(', '.join(labels)))
            else:
                st.error(result['message'])
        else:
            st.warning("Please enter some text.")

if __name__ == "__main__":
    main()
