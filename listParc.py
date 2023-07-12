import strawberry
from typing import List, Optional, Tuple
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
    position: Optional[Tuple[float, float]]
    user_position: Optional[Tuple[float, float]]


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
                    "https://www.jardinspaysdelaloire.fr/media/4417/big/20.04.11-proce-%2852%29.jpg",
                    "https://www.jardinspaysdelaloire.fr/media/4709/big/quartier04-proc-%C2%AE.jpg",
                    "https://api-infonantes.nantesmetropole.fr/banque/public/images/lieux/w/e1019-3-web-nm093419.jpg",
                ],
                position=(47.223889, -1.582222),
                user_position=None,
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
                    "https://www.jardinspaysdelaloire.fr/media/4459/big/19.04.11-la-gaudini-%C2%BFre-%287%29.jpg",
                    "https://www.jardinspaysdelaloire.fr/media/4706/big/quartier07-gaudini-%C2%BFre.jpg",
                    "https://upload.wikimedia.org/wikipedia/commons/7/77/Nantes_-_Ch%C3%A2teau_de_la_Gaudini%C3%A8re_-02.jpg",
                ],
                position=(47.244167, -1.577778),
                user_position=None,
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
                    "https://jardins.nantes.fr/N/Jardin/Parcs-Jardins/Plus/1937/Oblates/Photo/1.jpg",
                    "https://jardins.nantes.fr/N/Jardin/Parcs-Jardins/Plus/1937/Oblates/Photo/6.jpg",
                    "https://jardins.nantes.fr/N/Jardin/Parcs-Jardins/Plus/1937/Oblates/Photo/9.jpg",
                ],
                position=(47.199722, -1.585),
                user_position=None,
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
                img=[
                    "https://www.jardinspaysdelaloire.fr/media/4407/big/44-grandbloterreau_depliant2011_%C2%A9com-externe-ville-de-nantes.jpg",
                    "https://www.jardinspaysdelaloire.fr/media/4705/big/parc-du-grand-blottereau.jpg",
                    "https://jardins.nantes.fr/N/Jardin/Parcs-Jardins/Plus/170/Grand-Blottereau/Photo/Diaporama/7.jpg",
                ],
                position=(47.228056, -1.508611),
                user_position=None,
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
                img=[
                    "https://www.jardinspaysdelaloire.fr/media/4702/big/vdn00107027.jpg",
                    "https://www.jardinspaysdelaloire.fr/media/4402/big/_dsc5858-%C2%A9-j.r.-n-44-jard-des-plantes.jpg",
                    "https://www.jardinspaysdelaloire.fr/media/4400/big/_dsc6895-%C2%A9-j.r.-n-44_jard-des-plantes.jpg",
                ],
                position=(47.219444, -1.542778),
                user_position=None,
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
                img=[
                    "https://www.jardinspaysdelaloire.fr/media/4711/big/quartier09-beaujoire.jpg",
                    "https://www.jardinspaysdelaloire.fr/media/4099/big/560.jpg",
                    "https://www.jardinspaysdelaloire.fr/media/4103/big/568.jpg",
                ],
                position=(47.261944, -1.534167),
                user_position=None,
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
                img=[
                    "https://www.jardinspaysdelaloire.fr/media/5268/big/44_jardin-extraordinaire.jpg",
                    "https://mavieenloireatlantique.fr/wp-content/uploads/2020/05/Jardin-Extraordinaire-9180.jpg",
                    "https://metropole.nantes.fr/files/images/actualites/nature-environnement/jardin%20extraordinaire/jardin-extraordinaire-800jpg.jpg",
                ],
                position=(47.200278, -1.580833),
                user_position=None,
            ),
            Parc(
                id=uuid.uuid4(),
                nom="Île de Versailles",
                adresse="Quai de Versailles",
                ville="Nantes",
                departement=44000,
                hectares=1.7,
                creation=1831,
                quartier=["Hauts-Pavés", "Saint-Félix"],
                img=[
                    "https://www.jardinspaysdelaloire.fr/media/4708/medium/maison-de-l-erdre_ile-de-versailles.jpg",
                    "https://www.jardinspaysdelaloire.fr/media/4411/big/01.06.11-i-de-versailles-%2816%29.jpg",
                    "https://www.jardinspaysdelaloire.fr/media/4408/big/01.06.11-i-de-versailles-%286%29.jpg",
                ],
                position=(47.233333, -1.55),
                user_position=None,
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
                img=[
                    "https://www.sortir-en-ville.com/images/kcfinder/images/beaujoire-jdo-13-754-4.JPG",
                    "https://nanteswithlove.fr/wp-content/uploads/2015/07/Parc-de-la-Roseraie-Nantes-61-1024x678.jpg",
                    "https://nanteswithlove.fr/wp-content/uploads/2015/07/Parc-de-la-Roseraie-Nantes_Cover-832x554_c.jpg",
                ],
                position=(47.2626266, -1.5327121),
                user_position=None,
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
                    "https://jardins.nantes.fr/N/Image/RSoc/Photo/parc-de-beaulieu-nantes.jpg",
                    "https://jardins.nantes.fr/N/Jardin/Parcs-Jardins/Plus/211/Beaulieu/Photo//4.jpg",
                    "https://jardins.nantes.fr/N/Jardin/Parcs-Jardins/Plus/211/Beaulieu/Photo//1.jpg",
                ],
                position=(47.2125, -1.519722),
                user_position=None,
            ),
        ]
        return parcs_data
