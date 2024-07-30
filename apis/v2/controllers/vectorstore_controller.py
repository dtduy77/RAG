from ..controllers.document_controller import split_chunk, split_to_df
from ..configs.word_embedding_config import get_embedding
import pymongo

def embedding_chunk(pdf_path):
    splits_chunk_list = split_chunk(pdf_path)
    dataset_df = split_to_df(splits_chunk_list)
    dataset_df["embedding"] = dataset_df["text"].apply(get_embedding)
    return dataset_df

def get_mongo_client(mongo_uri):
    """Establish connection to the MongoDB."""
    try:
        client = pymongo.MongoClient(mongo_uri, appname="devrel.content.python")
        print("Connection to MongoDB successful")
        return client
    except pymongo.errors.ConnectionFailure as e:
        print(f"Connection failed: {e}")
        return None
pdf_path = 'dataset_fpt_rag.pdf'

dataset_df = embedding_chunk(pdf_path)

mongo_uri = "mongodb+srv://nstung463:uXDMuD9MBPbYHMCF@exe.vsuk2vq.mongodb.net/?retryWrites=true&w=majority&appName=exe    "
if not mongo_uri:
    print("MONGO_URI not set in environment variables")
mongo_client = get_mongo_client(mongo_uri)
# Ingest data into MongoDB
db = mongo_client['sample_mflix']
collection = db['movie_collection_2']
mongo_client['sample_mflix']['movie_collection_2'].count_documents({})
collection.delete_many({})
documents = dataset_df.to_dict("records")
collection.insert_many(documents)
