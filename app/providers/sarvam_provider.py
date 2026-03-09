from openai import AsyncOpenAI
from typing import AsyncGenerator

from app.providers.base import BaseLLMProvider
from app.core.config import get_settings
from app.core.model_registry import MODEL_REGISTRY

class SarvamProvider(BaseLLMProvider):
    def __init__(self, model_name:str) -> None:
        super().__init__(model_name)
        
        settings = get_settings()
        
        self.client = AsyncOpenAI(
            api_key = settings.SARVAM_API_KEY,
            base_url = settings.SARVAM_BASE_URL
        )
        
        meta = MODEL_REGISTRY[model_name]
        self.api_model = meta.get('api_model', model_name)
    
    async def stream_generate(self, prompt: str) -> AsyncGenerator[str, None]:

        stream = await self.client.chat.completions.create(
            model=self.api_model,
            messages=[
                {"role": "user", "content": prompt}
            ],
            stream=True
        )

        async for chunk in stream:
            token = chunk.choices[0].delta.content
            if token:
                yield token

    async def generate(self, prompt: str) -> str:

        response = await self.client.chat.completions.create(
            model=self.api_model,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content