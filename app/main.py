from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import bittensor as bt
from bittensor import Keypair, metagraph, wallet
from openkaito.openkaito.protocol import SemanticSearchSynapse
from fastapi.middleware.cors import CORSMiddleware

# Configuration and Setup
hotkey = Keypair.create_from_mnemonic("fever unlock seven sphere robot royal feature post tennis ivory black when")
dendrite = bt.dendrite(wallet=hotkey)
bt_network = bt.metagraph(5, network="finney")
bt_network.sync()

app = FastAPI()


origins = [
  # Adjust this to your frontend's URL
    "http://135.181.63.160:8001"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Or ["*"] for open access from any domain
    allow_credentials=True,
    allow_methods=["*"],  # Or specify like ["GET", "POST"]
    allow_headers=["*"],
)


class QueryParams(BaseModel):
    query_string: str
    size: int
    index_name: str

@app.post("/search/")
async def search_synapse(query_params: QueryParams):
    synapse = SemanticSearchSynapse(
        query_string=query_params.query_string,
        size=query_params.size,
        index_name=query_params.index_name
    )
    
    axons = bt_network.axons
    if not axons:
        raise HTTPException(status_code=404, detail="No axons available for querying")

    try:
        response = await dendrite(axons[:min(len(axons), 10)], timeout=300.0, synapse=synapse)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

