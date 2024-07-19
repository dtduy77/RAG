from .vectorstore_provider import VectorStoreProvider
from .firebase_provider import FirebaseProvider
from ..utils.constants import DOC_COLLECTION_NAME

vectorstore_db = VectorStoreProvider()
firebase_db = FirebaseProvider(DOC_COLLECTION_NAME)