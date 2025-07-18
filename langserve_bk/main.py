from fastapi import FastAPI
from langserve import add_routes

from diagnostics_graph import build_graph

app = FastAPI()
graph = build_graph()

add_routes(app,graph,path="/diagnose")
