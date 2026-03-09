MODEL_REGISTRY = {

    "gpt4o_mini": {
        "provider": "openai",
        "api_model": "gpt-4o-mini",
        "strength": 7,
        "latency": "fast",
        "context_window": 128000,
        "cost_input": 0.00015,
        "cost_output": 0.0006,
        "roles": ["generator"]
    },

    "gpt4o": {
        "provider": "openai",
        "api_model": "gpt-4o",
        "strength": 9,
        "latency": "medium",
        "context_window": 128000,
        "cost_input": 0.005,
        "cost_output": 0.015,
        "roles": ["generator", "judge"]
    },

    "claude_opus": {
        "provider": "anthropic",
        "api_model": "claude-3-opus-20240229",
        "strength": 9,
        "latency": "medium",
        "context_window": 200000,
        "cost_input": 0.015,
        "cost_output": 0.075,
        "roles": ["generator", "judge"]
    },

    "claude_sonnet": {
        "provider": "anthropic",
        "api_model": "claude-3-5-sonnet-20241022",
        "strength": 8,
        "latency": "fast",
        "context_window": 200000,
        "cost_input": 0.003,
        "cost_output": 0.015,
        "roles": ["generator"]
    },

    "grok_beta": {
        "provider": "grok",
        "api_model": "grok-beta",
        "strength": 8,
        "latency": "fast",
        "context_window": 128000,
        "cost_input": 0.003,
        "cost_output": 0.009,
        "roles": ["generator"]
    },

    "sarvam_m": {
        "provider": "sarvam",
        "api_model": "sarvam-m",
        "strength": 7,
        "latency": "fast",
        "context_window": 32000,
        "cost_input": 0.002,
        "cost_output": 0.006,
        "roles": ["generator"]
    },

    "sarvam_large": {
        "provider": "sarvam",
        "api_model": "sarvam-large",
        "strength": 8,
        "latency": "medium",
        "context_window": 64000,
        "cost_input": 0.004,
        "cost_output": 0.008,
        "roles": ["generator"]
    },

    "llama3_70b": {
        "provider": "oss",
        "api_model": "meta-llama/Meta-Llama-3-70B-Instruct",
        "strength": 8,
        "latency": "slow",
        "context_window": 8000,
        "cost_input": 0.0005,
        "cost_output": 0.0005,
        "roles": ["generator"]
    },

    "mixtral_8x7b": {
        "provider": "oss",
        "api_model": "mistralai/Mixtral-8x7B-Instruct",
        "strength": 7,
        "latency": "fast",
        "context_window": 32000,
        "cost_input": 0.0004,
        "cost_output": 0.0004,
        "roles": ["generator"]
    },

    "groq_llama_8b": {
        "provider": "groq",
        "api_model": "llama-3.1-8b-instant",
        "strength": 4,
        "latency": "ultra_fast",
        "context_window": 8000,
        "cost_input": 0.0002,
        "cost_output": 0.0002,
        "roles": ["slm"]
    },

    "groq_llama_70b": {
        "provider": "groq",
        "api_model": "llama-3.1-70b-versatile",
        "strength": 7,
        "latency": "ultra_fast",
        "context_window": 8000,
        "cost_input": 0.0004,
        "cost_output": 0.0004,
        "roles": ["generator"]
    }
}