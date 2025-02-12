from fastapi import FastAPI
import networkx as nx
from langchain.chat_models import ChatOpenAI
from pyvis.network import Network
from dotenv import load_dotenv
import os
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
app = FastAPI()

# Initialize OpenAI LLM (Replace "your-api-key" with actual API key)
llm = ChatOpenAI(openai_api_key=openai_api_key, model_name="gpt-4", temperature = 0)

# Create the medical knowledge graph
G = nx.Graph()

# Add diseases
G.add_node("Diabetes", type="Disease")
G.add_node("Hypertension", type="Disease")

# Add symptoms
G.add_node("Frequent Urination", type="Symptom")
G.add_node("Blurred Vision", type="Symptom")
G.add_node("Headache", type="Symptom")

# Add treatments
G.add_node("Insulin Therapy", type="Treatment")
G.add_node("Blood Pressure Medication", type="Treatment")

# Add risk factors
G.add_node("Obesity", type="Risk Factor")
G.add_node("Smoking", type="Risk Factor")

# Add diagnosis methods
G.add_node("Blood Sugar Test", type="Diagnosis")
G.add_node("Blood Pressure Check", type="Diagnosis")

# Add prevention methods
G.add_node("Exercise", type="Prevention")
G.add_node("Healthy Diet", type="Prevention")

# Define relationships
G.add_edge("Diabetes", "Frequent Urination", relation="Causes")
G.add_edge("Diabetes", "Blurred Vision", relation="Causes")
G.add_edge("Diabetes", "Insulin Therapy", relation="Treated by")
G.add_edge("Diabetes", "Kidneys", relation="Affects")
G.add_edge("Diabetes", "Blood Sugar Test", relation="Diagnosed by")
G.add_edge("Diabetes", "Obesity", relation="Risk Factor")
G.add_edge("Diabetes", "Exercise", relation="Prevented by")

G.add_edge("Hypertension", "Headache", relation="Causes")
G.add_edge("Hypertension", "Blood Pressure Medication", relation="Treated by")
G.add_edge("Hypertension", "Kidneys", relation="Affects")
G.add_edge("Hypertension", "Blood Pressure Check", relation="Diagnosed by")
G.add_edge("Hypertension", "Smoking", relation="Risk Factor")
G.add_edge("Hypertension", "Healthy Diet", relation="Prevented by")

@app.get("/query/{entity}")
def query_knowledge_graph(entity: str):
    """ Fetch medical knowledge related to an entity """
    if entity in G:
        results = []
        for neighbor in G.neighbors(entity):
            relation = G[entity][neighbor]['relation']
            results.append({"name": neighbor, "relation": relation})
        return {"entity": entity, "related_info": results}
    return {"error": "No data found"}


@app.get("/llm_query/{entity}")
def query_with_llm(entity: str):
    """ Generate LLM response based on entity knowledge """
    if entity in G:
        context = "\n".join(
            [f"{entity} {G[entity][neighbor]['relation']} {neighbor}" for neighbor in G.neighbors(entity)]
        )
        prompt = f"Based on the following medical knowledge, summarize insights about {entity}: {context}"
        response = llm.predict(prompt)
        return {"entity": entity, "llm_response": response}
    return {"error": "No data found"}

@app.get("/visualize_graph")
def visualize_graph():
    """ Generate an interactive HTML visualization of the knowledge graph """
    net = Network(notebook=False, height="600px", width="100%")
    # Add nodes and edges safely
    for node in G.nodes():
        node_type = G.nodes[node].get("type", "Unknown")  # <-- Fix: Use .get() to avoid KeyError
        color = {
            "Disease": "red", "Symptom": "orange", "Treatment": "green",
            "Risk Factor": "blue", "Diagnosis": "purple", "Prevention": "cyan"
        }.get(node_type, "gray")  # Default color if type is missing

        net.add_node(node, label=node, color=color)

    for edge in G.edges():
        relation = G[edge[0]][edge[1]].get("relation", "Unknown")  # <-- Fix: Use .get() for safety
        net.add_edge(edge[0], edge[1], title=relation)

    # Save graph.html
    output_path = "static/graph.html"
    net.show(output_path, notebook=False)
    return {"message": f"Graph visualization generated. Open {output_path} in a browser."}