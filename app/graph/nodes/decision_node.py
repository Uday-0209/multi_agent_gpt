from app.core.model_registry import MODEL_REGISTRY

async def decision_node(state: dict) -> dict:
    
    mode = state.get('mode')
    override = state.get('generation_models')
    judge_override = state.get("judge_override")
    
    models = list(MODEL_REGISTRY.keys())
    
    models = [m for m in models if MODEL_REGISTRY[m].get('roles') != 'slm']
    
    models.sort(
        key = lambda x: MODEL_REGISTRY[x]['strength'],
        reverse = True
    )
    if not mode:
        raise ValueError("mode is required in the state.")
    
    if mode == 'single':    
        if override:
            selected = override[:1]
        else:
            selected = [models[0]]
    
    elif mode == 'multi':
        if override:
            selected = override[:3]
            if len(selected) < 2:
                for m in models:
                    if m not in selected:
                        selected.append(m)
                    if len(selected) == 2:
                        break
        else:
            selected = models[:2]
    
    if judge_override:
        judge = judge_override
    else:
        judge = models[0]
        
           
    return {
        **state,
        "selected_models": selected,
        "judge_model": judge
    }

        