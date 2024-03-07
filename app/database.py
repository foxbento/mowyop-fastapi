from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from models import ArtistCard
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

async def init():
    client = AsyncIOMotorClient(os.getenv("MONGODB_URL"))
    
    await init_beanie(database=client.artistdb, document_models=[ArtistCard])
