import json
from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.api.schemas import ChatRequest
from app.graph.builder import build_graph

router = APIRouter()

graph = build_graph()
@router.post('/chat')
async def chat(request: ChatRequest):
    async def event_generator():
        
        initial_state = {
            "user_input": request.user_input,
            "mode": request.mode,
            "generation_models": request.generation_models,
            "judge_override": request.judge_model
            }
        
        async for event in graph.astream(initial_state):
            yield f"data:{
                json.dumps(event)}\n\n"
    
    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream"
    )
    