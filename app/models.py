from typing import Dict, List
from beanie import Document
from pydantic import AnyUrl, BaseModel

class ArtistCard(Document):
    profile_image: AnyUrl
    artist_name: str
    description: str
    socials: Dict[str, AnyUrl]
    popular_images: List[AnyUrl]

    class Settings:
        name = "artistcard"

class ArtistCardCreate(BaseModel):
    profile_image: str
    artist_name: str
    description: str
    socials: Dict[str, str]
    popular_images: List[str]