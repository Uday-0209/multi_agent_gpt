import asyncio
from app.core.provider_factory import get_provider

async def multi_llm_node(state: dict):
    
    models = state["selected_models"]
    print("Selected models:", models)
    prompt = state["refined_prompt"]
    
    queue = asyncio.Queue()
    
    outputs = {}
    
    async def run_model(model_name):
        provider = get_provider(model_name)
        
        buffer = ""
    
        async for token in provider.stream_generate(prompt):
            buffer += token
            
            await queue.put({
                "type": "model_stream",
                "model": model_name,
                "token": token
            })
        outputs[model_name] = buffer
        
        await queue.put(
            {
                'type': "model_complete",
                'model': model_name
            }
        )
        
    tasks = [
        asyncio.create_task(run_model(model)) for model in models
    ]
    
    async def monitor():
        
        await asyncio.gather(*tasks)
        
        await queue.put({
            "type":"multi_complete"
        })
        
    asyncio.create_task(monitor())
    
    completed = False
    
    while not completed:
        event = await queue.get()
        
        yield event
        
        if event['type'] == 'multi_complete':
            completed = True
            
    yield {
        'outputs': outputs
    }
    