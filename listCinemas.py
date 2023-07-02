import strawberry
from typing import List, Optional
import uuid

@strawberry.type
class Cinema:
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
    def cinemas(self) -> List[Cinema]:
        cinemas_data = [
            Cinema(
                id=uuid.uuid4(),
                nom="",
                adresse="",
                ville="Nantes",
                departement=44000,
                creation= None,
                quartier=[],
                img=[
                    "",
                    "",
                    "",
                ],
            ),
        ]
        return cinemas_data
