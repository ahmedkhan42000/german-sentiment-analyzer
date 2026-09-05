import streamlit as st
from transformers import pipeline


# Load model locally
@st.cache_resource
def load_model():
    return pipeline(
        model="oliverguhr/german-sentiment-bert", task="text-classification"
    )


# Page config
st.set_page_config(page_title="German Sentiment Analyzer", page_icon="🇩🇪")

# UI
st.title("🇩🇪 German Sentiment Analyzer")
st.write("Type any German text and see if it is positive, negative, or neutral.")

# Load model
model = load_model()

text = st.text_area("Enter German text here:", height=150)

if st.button("Analyze"):
    if text:
        with st.spinner("Analyzing..."):
            result = model(text)
            label = result[0]["label"]
            score = round(result[0]["score"] * 100, 2)

            if label == "positive":
                st.success(f"✅ Sentiment: {label.upper()} — Confidence: {score}%")
            elif label == "negative":
                st.error(f"❌ Sentiment: {label.upper()} — Confidence: {score}%")
            else:
                st.warning(f"⚠️ Sentiment: {label.upper()} — Confidence: {score}%")
    else:
        st.warning("Please enter some text first.")
