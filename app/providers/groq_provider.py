from groq import AsyncGroq 
from typing import AsyncGenerator
from app.providers.base import BaseLLMProvider
from app.core.config import Settings

class GroqProvider(BaseLLMProvider):
    def __init__(self, model_name:str) -> None:
        super().__init__(model_name)
        self.client = AsyncGroq(api_key=Settings().GROQ_API_KEY)
        
    async def stream_generate(self, prompt:str) -> AsyncGenerator[str, None]:
        stream = await self.client.chat.completions.create(
            model = self.model_name,
            messages = [{
                'role':'user',
                'content': prompt
            }],
            stream = True
        )
        async for chunk in stream:
            if chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content
                
    async def generate(self, prompt:str) -> str:
        response = await self.client.chat.completions.create(
            model = self.model_name,
            messages = [{
                'role':'user',
                'content': prompt
                }])
        return response.choices[0].message.content