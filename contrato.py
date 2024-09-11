from datetime import datetime
from typing import Tuple

from pydantic import BaseModel, EmailStr
from enum import Enum

class ProdutoEnum(str, Enum):
    produto1 = "ZapFlow com Gemini"
    produto2 = "ZapFlow com chatGPT"
    produto3 = "ZapFlow com Llama3.0"
        
class Vendas(BaseModel):
    email: EmailStr
    data: datetime
    valor: float
    quantidade: int
    produto: ProdutoEnum