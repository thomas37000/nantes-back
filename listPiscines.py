import strawberry
from typing import List, Optional, Tuple
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
    position: Optional[Tuple[float, float]]


@strawberry.type
class Query:
    @strawberry.field
    def piscines(self) -> List[Piscine]:
        piscines_data = [
            Piscine(
                id=uuid.uuid4(),
                nom="Piscine des Dervallières",
                adresse="Rue Professeur Dubuisson",
                ville="Nantes",
                departement=44000,
                creation=1969,
                quartier=["Breil", "Barberie"],
                img=[
                    "",
                    "",
                    "",
                ],
                position=(47.2273191, -1.6128337),
            ),
            Piscine(
                id=uuid.uuid4(),
                nom="Piscine du Petit Port",
                adresse="Bd du Petit Port",
                ville="Nantes",
                departement=44300,
                creation=1984,
                quartier=["Nantes Nord"],
                img=[
                    "",
                    "",
                    "",
                ],
                position=(47.2427248, -1.590507),
            ),
            Piscine(
                id=uuid.uuid4(),
                nom="Piscine Ernest Renan",
                adresse="1 Rue de Saint-Servan",
                ville="Saint Herblain",
                departement=44800,
                creation=None,
                quartier=None,
                img=[
                    "",
                    "",
                    "",
                ],
                position=(47.2154985, -1.6495863),
            ),
            Piscine(
                id=uuid.uuid4(),
                nom="Piscine Jules Verne",
                adresse="Rue Jules Grandjouan",
                ville="Nantes",
                departement=44300,
                creation=1995,
                quartier=["Doulon", "Bottière"],
                img=[
                    "",
                    "",
                    "",
                ],
                position=(47.2482135, -1.5897118),
            ),
            Piscine(
                id=uuid.uuid4(),
                nom="Piscine de la Durantière",
                adresse="11 Rue de la Durantière",
                ville="Nantes",
                departement=44100,
                creation=None,
                quartier=None,
                img=[
                    "",
                    "",
                    "",
                ],
                position=(47.2127278, -1.6709106),
            ),
            Piscine(
                id=uuid.uuid4(),
                nom="Piscine de la Cholière",
                adresse="108 Av. Claude Antoine Peccot",
                ville="Orvault",
                departement=44700,
                creation=None,
                quartier=["la Cholière"],
                img=[
                    "",
                    "",
                    "",
                ],
                position=(47.2511443, -1.6821247),
            ),
            Piscine(
                id=uuid.uuid4(),
                nom="Piscine Léo Lagrange",
                adresse="Allée de l'Île Gloriette",
                ville="Nantes",
                departement=44000,
                creation=1951,
                quartier=["Centre-ville"],
                img=[
                    "",
                    "",
                    "",
                ],
                position=(47.2128653, -1.6472413),
            ),
            Piscine(
                id=uuid.uuid4(),
                nom="Piscine de la Bourgonnière",
                adresse="34 Allée de la Bourgonnière",
                ville="Saint-Herblain",
                departement=44800,
                creation=1993,
                quartier=None,
                img=[
                    "",
                    "",
                    "",
                ],
                position=(47.2511443, -1.7542225),
            ),
            Piscine(
                id=uuid.uuid4(),
                nom="So.Pool",
                adresse="2 Rue de Tasmanie",
                ville="Basse-Goulaine",
                departement=44115,
                creation=None,
                quartier=None,
                img=[
                    "",
                    "",
                    "",
                ],
                position=(47.1895785, -1.5556934),
            ),
            Piscine(
                id=uuid.uuid4(),
                nom="Piscine Victor Jara",
                adresse="5 Avenue Léon Blum",
                ville="Rezé",
                departement=44400,
                creation=1973,
                quartier=["Trocardière"],
                img=[
                    "",
                    "",
                    "",
                ],
                position=(47.1782404, -1.6291869),
            ),
            Piscine(
                id=uuid.uuid4(),
                nom="Le jardin d'Ô35 aux nouvelles cliniques nantaise",
                adresse="3 Rue Éric Tabarly",
                ville="Nantes",
                departement=44000,
                creation=None,
                quartier=None,
                img=[
                    "",
                    "",
                    "",
                ],
                position=(47.1830241, -1.7129577),
            ),
            Piscine(
                id=uuid.uuid4(),
                nom="Piscine Municipale de Bouguenais",
                adresse="Chem. Jacques Prévert",
                ville="Bouguenais",
                departement=44340,
                creation=None,
                quartier=None,
                img=[
                    "",
                    "",
                    "",
                ],
                position=(47.1716841, -1.65736929),
            ),
            Piscine(
                id=uuid.uuid4(),
                nom="Piscine de la Petite Amazonie",
                adresse="Bd de Berlin",
                ville="Nantes",
                departement=44000,
                creation=None,
                quartier=["Malakoff", "Saint-Donatien"],
                img=[
                    "",
                    "",
                    "",
                ],
                position=(47.2164682, -1.5677724),
            ),
            Piscine(
                id=uuid.uuid4(),
                nom="Piscine Municipale",
                adresse="35 Bd des Sports",
                ville="Vertou",
                departement=44120,
                creation=None,
                quartier=None,
                img=[
                    "",
                    "",
                    "",
                ],
                position=(47.1780047,-1.5530087),
            ),
        ]
        return piscines_data
