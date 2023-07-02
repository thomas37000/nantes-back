import strawberry
from typing import List, Optional
import uuid

@strawberry.type
class Piscine:
    id: uuid.UUID
    nom: str
    adresse: str
    ville: str
    departement: int
    creation: Optional[int]
    quartier: Optional[List[str]]
    img: Optional[List[str]]

@strawberry.type
class Query:
    @strawberry.field
    def piscines(self) -> List[Piscine]:
        piscines_data = [
            Piscine(
                id=uuid.uuid4(),
                nom="",
                adresse="",
                ville="Nantes",
                departement=44000,
                creation=None,
                quartier=[],
                img=[
                    "",
                    "",
                    "",
                ],
            ),
        ]
        return piscines_data
