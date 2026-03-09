from langgraph.graph import StateGraph, END
from app.graph.nodes.slm_node import slm_model
from app.graph.nodes.single_llm_node import single_llm_node
from app.graph.state import GraphState
from app.graph.nodes.decision_node import decision_node
from app.graph.nodes.multi_llm_node import multi_llm_node
from app.graph.nodes.judge_node import judge_node

def route_mode(state):
    if state['mode'] == 'single':
        return "single_llm"
    return "multi_llm"

def build_graph():
    workflow = StateGraph(GraphState)
    
    workflow.add_node("slm", slm_model)
    workflow.add_node("decision", decision_node)
    workflow.add_node("single_llm", single_llm_node)
    workflow.add_node("multi_llm", multi_llm_node)
    workflow.add_node('judge_llm', judge_node)
    
    workflow.set_entry_point("slm")
    
    workflow.add_edge("slm", "decision")
    workflow.add_conditional_edges("decision", 
                      route_mode,
                      {
                          "single_llm": "single_llm",
                          "multi_llm": "multi_llm"
                          
                      })
    workflow.add_edge("single_llm", END)
    workflow.add_edge("multi_llm", "judge_llm")
    workflow.add_edge("judge_llm", END)
    
    return workflow.compile()
    
    
    
