from pydantic import BaseModel

class Observation(BaseModel):
    money: float
    savings: float
    investments: float
    income: float
    expenses: float
    happiness: float
    month: int

class Action(BaseModel):
    action: str

class Reward(BaseModel):
    value: float