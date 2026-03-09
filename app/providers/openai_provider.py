from openai import AsyncOpenAI
from typing import AsyncGenerator
from app.providers.base import BaseLLMProvider
from app.core.config import get_settings
from app.core.model_registry import MODEL_REGISTRY

class OpenAIProvider(BaseLLMProvider):
    def __init__(self, model_name: str) -> None:
        super().__init__(model_name)
        settings = get_settings()
        self.client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)
        
        meta = MODEL_REGISTRY[model_name]
        self.api_model = meta.get('api_model', model_name)
    
    async def stream_generate(self, prompt: str) -> AsyncGenerator[str, None]:
        
        stream = await self.client.chat.completions.create(
            model = self.api_model,
            messages = [{'role':'user', 'content': prompt}],
            stream = True
        )
        async for chunk in stream:
            if chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content
    
    async def generate(self, prompt: str) -> str:
        response = await self.client.chat.completions.create(
            model = self.model_name,
            messages= [{
                'role':'user',
                'content': prompt
            }],
        )
        return response.choices[0].message.content