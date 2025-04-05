# models.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Abordagem(BaseModel):
    evento_id: Optional[str] = None
    cliente_id: str
    data_hora_abordagem: datetime
    nome_lead: str
    telefone: str
    canal: Optional[str] = None
