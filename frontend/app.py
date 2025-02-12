import streamlit as st
import requests
import networkx as nx
import matplotlib.pyplot as plt
from io import BytesIO

st.set_page_config(page_title="Medical Knowledge Graph", page_icon="🩺", layout="wide")
st.title("🩺 AI-Powered Medical Knowledge Graph")

# API Endpoint
BASE_URL = "http://127.0.0.1:8000"

def query_knowledge_graph(entity):
    """Fetch medical knowledge related to an entity."""
    response = requests.get(f"{BASE_URL}/query/{entity}")
    if response.status_code == 200:
        return response.json()
    return {"error": "Failed to fetch data"}

def query_llm(entity):
    """Fetch AI-generated insights for a medical entity."""
    response = requests.get(f"{BASE_URL}/llm_query/{entity}")
    if response.status_code == 200:
        return response.json()
    return {"error": "Failed to fetch AI response"}


def visualize_graph():
    """Trigger the backend graph visualization."""
    print("visualizing graph")
    response = requests.get(f"{BASE_URL}/visualize_graph")
    print(response.status_code)
    print(response.text)
    if response.status_code == 200:
        data = response.json()
        st.success(data["message"])
        st.markdown("[📊 Click here to open the graph](http://127.0.0.1:8000/static/graph.html)", unsafe_allow_html=True)
    else:
        st.error("Visualization failed")

# Sidebar Input
st.sidebar.header("🔎 Medical AI Assistant")
entity = st.sidebar.text_input("Enter a medical entity (e.g., Diabetes, Hypertension, Insulin Therapy):")

if st.sidebar.button("Search Knowledge Graph"):
    with st.spinner("Fetching data..."):
        result = query_knowledge_graph(entity)
        if "error" in result:
            st.error(result["error"])
        else:
            st.subheader(f"📌 Medical Insights for: {entity}")
            for item in result.get("related_info", []):
                st.write(f"🔗 **{entity}** {item['relation']} **{item['name']}**")

if st.sidebar.button("Ask AI for Insights"):
    with st.spinner("Fetching AI-generated response..."):
        response = query_llm(entity)
        if "error" in response:
            st.error(response["error"])
        else:
            st.subheader("🧠 AI-Generated Insights:")
            st.write(response.get("llm_response", "No response received."))
            visualize_graph()
