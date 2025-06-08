from typing import TypedDict
from langgraph.graph import StateGraph,END
from langchain_core.runnables import RunnableLambda
from pydantic import BaseModel
from typing import Union, List, Dict
from tools.diagnosis_tool import ai_sci_diagnosis
from tools.summary_checker import check_analysis

class DiagnosisState(TypedDict):
    input : str
    field_area: Union[str, List[Dict[str, str]]]
    summary : str

def build_graph():
    graph = StateGraph(DiagnosisState)    
    
    def sci_step(state):
        return {
                "input" : state["input"],
                "field_area" : check_analysis.invoke(state["input"]),
                "summary" : state.get("summary")
        }


    graph.add_node("sci_step_check",RunnableLambda(sci_step))


    def summary_step(state):
        return {
                "input" : state["input"],
                "field_area" : state['field_area'],
                "summary" : ai_sci_diagnosis.invoke(state['input'])
        }


    graph.add_node("summry_step_check",RunnableLambda(summary_step))

    graph.set_entry_point("sci_step_check")
    graph.add_edge("sci_step_check","summry_step_check")
    graph.add_edge("summry_step_check",END)

    return graph.compile()

    