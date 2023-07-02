import strawberry
from typing import List, Optional
import uuid

@strawberry.type
class Parc:
    id: uuid.UUID
    nom: str
    adresse: str
    ville: str
    departement: int
    hectares: Optional[float]
    creation: Optional[int]
    quartier: Optional[List[str]]
    img: Optional[List[str]]

@strawberry.type
class Query:
    @strawberry.field
    def parcs(self) -> List[Parc]:
        parcs_data = [
            Parc(
                id=uuid.uuid4(),
                nom="Parc de Procé",
                adresse="4 Rue des Dervallières",
                ville="Nantes",
                departement=44000,
                hectares=11.3,
                creation=1886,
                quartier=["Hauts-Pavés", "Saint Félix", "Dervallières", "Zola"],
                img=[
                    "https://lh3.googleusercontent.com/p/AF1QipPYV41D4CfG3cgK-_1sFoxJmQ3WvO5Rf6FizhEX=s680-w680-h510",
                    "https://lh3.googleusercontent.com/p/AF1QipN3bNYzSqSc5su51GroorKORDD5kVclLudsZDH-=s680-w680-h510",
                    "https://lh3.googleusercontent.com/p/AF1QipPZoenWE7u-50FK06ULnQn1FIkl7so3rZqceK3c=s680-w680-h510",
                ],
            ),
            Parc(
                id=uuid.uuid4(),
                nom="Parc de La Gaudinière",
                adresse="Bd Robert Schuman",
                ville="Nantes",
                departement=44000,
                hectares=12.5,
                creation=1800,
                quartier=["Breil", "Barberie"],
                img=[
                    "https://lh3.googleusercontent.com/p/AF1QipO1N3TY73p5bjAU7lKSSUQVfwzjgI9u95axwwgH=s680-w680-h510",
                    "https://lh3.googleusercontent.com/p/AF1QipObS66q-TqttQkIyjxfhj4uJlOhDFmS3dvnJu8B=s680-w680-h510",
                    "https://lh3.googleusercontent.com/p/AF1QipNO4KSgZW3r692OnV88d1hmjZ7x1KalRTsaewKE=s680-w680-h510",
                ],
            ),
            Parc(
                id=uuid.uuid4(),
                nom="Parc des Oblates",
                adresse="Rue Philippe de Broca",
                ville="Nantes",
                departement=44000,
                hectares=3,
                creation=None,
                quartier=None,
                img=[
                    "https://lh3.googleusercontent.com/p/AF1QipPWI1PR2tiLQB2emVQPwGp9QOYZHHNoMd2rovmp=s680-w680-h510",
                    "https://lh3.googleusercontent.com/p/AF1QipMETUzbxp6UDjuvKXnsawEWjayxW-FfHIqskWwh=s680-w680-h510",
                    "https://lh3.googleusercontent.com/p/AF1QipMGDOMT1jWG0YKsHHXK8pEHGMCTh3MY6gcmqRpi=s680-w680-h510",
                ],
            ),
            Parc(
                id=uuid.uuid4(),
                nom="Parc du Grand Blottereau",
                adresse="16 Bd Auguste Peneau",
                ville="Nantes",
                departement=44000,
                hectares=19,
                creation=None,
                quartier=["Doulon", "Bottière"],
                img=["", "", ""],
            ),
            Parc(
                id=uuid.uuid4(),
                nom="Jardin des Plantes",
                adresse="Rue Stanislas Baudr",
                ville="Nantes",
                departement=44000,
                hectares=7.328,
                creation=1800,
                quartier=None,
                img=["", "", ""],
            ),
            Parc(
                id=uuid.uuid4(),
                nom="Parc Floral de la Beaujoire",
                adresse="344 Rte de Saint-Joseph",
                ville="Nantes",
                departement=44000,
                hectares=14,
                creation=1971,
                quartier=None,
                img=["", "", ""],
            ),
            Parc(
                id=uuid.uuid4(),
                nom="Jardin Extraordinaire",
                adresse="1 Quai Marquis d'Aiguillon",
                ville="Nantes",
                departement=44000,
                hectares=1.2,
                creation=2019,
                quartier=["Quartier Bellevue", "Chantenay", "ainte-Anne"],
                img=["", "", ""],
            ),
            Parc(
                id=uuid.uuid4(),
                nom="L'Île de Versailles",
                adresse="Quai de Versailles",
                ville="Nantes",
                departement=44000,
                hectares=1.7,
                creation=1831,
                quartier=["Hauts-Pavés", "Saint-Félix"],
                img=["", "", ""],
            ),
            Parc(
                id=uuid.uuid4(),
                nom="Parc Floral la Roseraie",
                adresse="Route de Saint-Joseph",
                ville="Nantes",
                departement=44300,
                hectares=None,
                creation=1971,
                quartier=None,
                img=["", "", ""],
            ),
            Parc(
                id=uuid.uuid4(),
                nom="Parc de Beaulieu",
                adresse="Cr de la Prairie d'Amont",
                ville="Nantes",
                departement=44200,
                hectares=13.37,
                creation=None,
                quartier=None,
                img=[
                    "https://lh3.googleusercontent.com/p/AF1QipPnQh25MHY3yHz5Ru9-Kqc-tRCAyArfeP4st-bu=s680-w680-h510",
                    "https://lh3.googleusercontent.com/p/AF1QipOnTz-wv8UqXD8QdcX3zXY7RckRDMyIt6_ga_GY=s680-w680-h510",
                    "https://lh3.googleusercontent.com/p/AF1QipPYqPhKBAFwkB8BxwOyMl4ifjy2541HQ8P4il22=s680-w680-h510",
                ],
            ),
        ]
        return parcs_data
