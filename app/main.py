from fastapi import FastAPI, HTTPException, Depends, Header
from fastapi.security import OAuth2PasswordBearer
from typing import List
from models import ArtistCard, ArtistCardCreate
from database import init
from dotenv import load_dotenv
import os

load_dotenv()
SECRET_TOKEN = os.getenv("SECRET_TOKEN")

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    await init()

def validate_token(x_token: str = Header(...)):
    if x_token != SECRET_TOKEN:
        raise HTTPException(status_code=401, detail="Invalid token")

# @app.get("/artistcard/{artist_card_id}", response_model=ArtistCard)
# async def get_artist_card(artist_card_id: str):
#     artist_card = await ArtistCard.get(artist_card_id)
#     if artist_card is None:
#         raise HTTPException(status_code=404, detail="ArtistCard not found")
#     return artist_card


@app.post("/artistcard", response_model=ArtistCard)
async def create_artist_card(artist_card: ArtistCardCreate, _: None = Depends(validate_token)):
    '''
        Only meant for me to add artist cards for now teehee :3
    '''
    new_artist_card = ArtistCard(**artist_card.dict())
    await new_artist_card.create()
    return new_artist_card\

@app.get("/artistcard/random", response_model=ArtistCard)
async def get_random_artist_card():
    pipeline = [{"$sample": {"size": 1}}]
    artist_cards = await ArtistCard.aggregate(pipeline).to_list()
    
    if not artist_cards:
        raise HTTPException(status_code=404, detail="No ArtistCards found")
    
    return artist_cards[0]