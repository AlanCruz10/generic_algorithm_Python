from pydantic import BaseModel


class Individual(BaseModel):
    id: int
    individual_bits: str
    individual_num: int
    x: float | int
    fx: float | int
    generation: int
