from pydantic import BaseModel
from typing import Optional, List

class ChatRequest(BaseModel):
    user_input: str
    mode: str #"single" or "multi"
       
    generation_models: Optional[List[str]] = None
    
    judge_model: Optional[str] = None
    