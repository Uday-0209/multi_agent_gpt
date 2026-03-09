from app.core.model_registry import MODEL_REGISTRY
from app.providers.openai_provider import OpenAIProvider
from app.providers.groq_provider import GroqProvider
# from app.providers.anthropic_provider import AnthropicProvider
# from app.providers.grok_provider import GrokProvider
from app.providers.sarvam_provider import SarvamProvider
# from app.providers.oss_provider import OSSProvider

def get_provider(model_name: str):
    meta = MODEL_REGISTRY.get(model_name)
    
    if not meta:
        raise ValueError(f"Model {model_name} not found in registry.")
    
    provider_name = meta["provider"]
    
    if provider_name == 'openai':
        return OpenAIProvider(model_name)
    if provider_name == 'groq':
        return GroqProvider(model_name)
    if provider_name == 'sarvam':
        return SarvamProvider(model_name)
    raise ValueError(f"Provider {provider_name} not implimented yet.")
    