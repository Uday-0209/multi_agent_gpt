from app.core.provider_factory import get_provider

async def single_llm_node(state:dict):
    
    model_name = state["selected_models"][0]
    prompt = state["refined_prompt"]
    
    provider = get_provider(model_name)
    
    output_buffer = ""
    
    async for token in provider.stream_generate(prompt):
        output_buffer += token
        
        yield {
            "type": "model_stream",
            "model": model_name,
            "token": token
        }
        
    yield {
        "type": "model_complete",
        "model":model_name
    }
    
    yield {
        **state,
        "type": "node_complete",
        "outputs":{
            model_name: output_buffer
        }
    }