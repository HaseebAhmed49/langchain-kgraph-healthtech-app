# 🧠 LangChain Knowledge Graph HealthTech Application

A **HealthTech Application** built using **FastAPI**, **LangChain**, **NetworkX**, and **OpenAI GPT-4** to create and interact with a medical knowledge graph. The frontend is built with **Streamlit** for an interactive UI, and the backend uses **FastAPI** to serve the knowledge graph and AI-powered insights.


![Screen Shot 2025-02-12 at 20 57 07 PM](https://github.com/user-attachments/assets/15ec2e6c-8d83-4765-ba17-b215f4fe6894)
![Screen Shot 2025-02-12 at 20 57 13 PM](https://github.com/user-attachments/assets/237a1eba-31fd-478e-9585-0997e70c789d)

---

## 🚀 Features
- 📌 FastAPI-based backend to manage a medical knowledge graph.
- 🤖 OpenAI-powered insights via LangChain for summarizing medical knowledge.
- 📊 Interactive visualization of the knowledge graph using **PyVis**.
- 🎨 Streamlit frontend for querying the knowledge graph and generating AI insights.
- 🔐 Uses `.env` file to store API keys securely.



---

## Project Structure
```sh
langchain-kgraph-healthtech-app/
│── frontend/
│   ├── app.py  # Streamlit UI
│── backend/
│   ├── main.py  # FastAPI
│   ├── .env
│── requirements.txt  # Project dependencies
│── README.md    # Project documentation
```

---

## Technologies Used
* **FastAPI** for backend API
* **Streamlit** for frontend UI
* **LangChain** for AI-based insights
* **OpenAI GPT-4** for summarizing medical knowledge
* **NetworkX** for creating and managing the knowledge graph
* **PyVis** for interactive graph visualization

---

## 📌 Prerequisites
Ensure you have the following installed on your system:
- **Python 3.13+**
- **pip** (Python package manager)

---

## 🛠 Installation & Setup

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/HaseebAhmed49/langchain-kgraph-healthtech-app.git
cd langchain-kgraph-healthtech-app
```

### 2️⃣ Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables
Create a `.env` file in the root directory and add your OpenAI API key:
```sh
echo "OPENAI_API_KEY=your_openai_api_key_here" > .env
```

---

## 🖥 Backend (FastAPI)

### 📌 Start the FastAPI Server
Run the backend using:
```sh
uvicorn backend.main:app --reload
```
The API will be available at `http://127.0.0.1:8000`.

### 📌 API Endpoints
- **`GET /query/{entity}`** → Fetches medical knowledge related to an entity (e.g., "Diabetes").
- **`GET /llm_query/{entity}`** → Generates AI-powered insights for a medical entity.
- **`GET /visualize_graph`** → Generates an interactive HTML visualization of the knowledge graph.

---

## 🎨 Frontend (Streamlit)

### 📌 Run the Streamlit App
```sh
streamlit run frontend/app.py
```

---

## 🔄 How It Works
1. **Query the Knowledge Graph**: Users can input a medical entity (e.g., "Diabetes") in the Streamlit app. The app sends a request to the FastAPI backend (`/query/{entity}`) to fetch related medical knowledge.
2. **Generate AI Insights**: Users can request AI-generated insights for a medical entity. The app sends a request to the FastAPI backend (`/llm_query/{entity}`), which uses LangChain and OpenAI GPT-4 to summarize the knowledge.
3. **Visualize the Graph**: Users can trigger the backend to generate an interactive visualization of the knowledge graph. The app sends a request to the FastAPI backend (`/visualize_graph`), which creates an HTML file using PyVis.

---

## 📜 License
This project is licensed under the MIT License.

---

## 📩 Contact
For issues or suggestions, feel free to open an [issue](https://github.com/HaseebAhmed49/langchain-kgraph-healthtech-app/issues) or reach out!
* Email: haseebahmed02@gmail.com
* LinkedIn/GitHub: /HaseebAhmed49

💡 **Happy Coding!** 🚀
