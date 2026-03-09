from app.core.provider_factory import get_provider

SLM_MODEL = "groq_llama_8b"


async def slm_model(state: dict) -> dict:
    
    user_input = state['user_input']
    
    provider = get_provider(SLM_MODEL)
    
    slm_prompt = f"""
        You are a prompt-refinement engine inside an AI orchestration system.

        Your job is to rewrite the user's query into a clear, concise instruction.

        Rules:
        - Do NOT explain anything.
        - Do NOT give examples.
        - Do NOT generate code.
        - Do NOT add extra sections.
        - Return ONLY the refined prompt.

        User Query:
        {user_input}

        Output format:
        REFINED_PROMPT: <one improved sentence>
    
    """
    try:
        refined_prompt = await provider.generate(slm_prompt)
        refined_prompt = refined_prompt.strip()
        
        if not refined_prompt:
            refined_prompt = user_input
            
    except Exception as e:
        refined_prompt = user_input
        
       
    return {
        **state,
        'refined_prompt': refined_prompt
    }