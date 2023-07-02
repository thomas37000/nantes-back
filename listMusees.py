import strawberry
from typing import List, Optional
import uuid

@strawberry.type
class Musee:
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
    def musees(self) -> List[Musee]:
        musees_data = [
            Musee(
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
        return musees_data
