from abc import ABC, abstractmethod
from typing import AsyncGenerator

class BaseLLMProvider(ABC):
    def __init__(self, model_name:str) -> None:
        super().__init__()
        self.model_name = model_name
        
    @abstractmethod
    async def stream_generate(self, prompt:str) -> AsyncGenerator[str, None]:
        pass
    
    @abstractmethod
    async def generate(self, prompt:str) -> str:
        pass