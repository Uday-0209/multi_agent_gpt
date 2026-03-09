from typing import TypedDict, Optional, List, Dict, Any
class GraphState(TypedDict, total=False):
    user_input: str
    refined_prompt: str
    mode: str #"single" or "multiple"
    generation_models: Optional[List[str]]
    
    judge_override: Optional[str]
    judge_model: Optional[str]
    
    complexity:Optional[int]
    selected_models: List[str]
    
    outputs: Dict[str, str]
    
    winner: Optional[str]
    judge_reason: Optional[str]
    
    token_usage: Dict[str, str]
    total_cost: float
    
    final_answer: str
    
    regen_count: int
    regen_feedback: str
    max_regens: int
    