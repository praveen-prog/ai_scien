uvicorn main:app --host 0.0.0.0 --port 8000

streamlit run app.py --server.port=10000 --server.enableCORS=false
