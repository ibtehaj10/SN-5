# Bittensor Semantic Search API | Subnet 5 | OpenKaito

This FastAPI application utilizes the Bittensor network to provide a decentralized semantic search API. The API allows querying against various Bittensor subnetworks using semantic and structured search protocols. Users can interact with the API to perform searches based on specific queries, sort results, and filter based on various parameters.

## Features

- **Semantic Search**: Search by meaning rather than exact keyword matches.


## Installation

Ensure you have Python 3.8+ installed on your system. To install the required dependencies, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/neuralinternet/subnet-endpoints.git
   cd subnet-endpoints.git/SN-5
   ```
   Install the required Python packages:
```
pip install -r requirements.txt
```

Configuration
Before running the application, you need to set up the necessary environment variables:

mnemonic: Your Bittensor wallet mnemonic for authentication.
This can be set in your shell or included in an environment file.

Running the API
To run the FastAPI server, use the following command from the root of your project directory:
```
uvicorn main:app --reload --host 0.0.0.0 --port 8001

```
