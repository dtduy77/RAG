import time
from typing import AnyStr, Dict
from ..configs.firebase_config import db

class FirebaseProvider:
    def __init__(self, collection_name: AnyStr):
        self.collection_name = collection_name
        self.db = db

    def upload_doc(self, data: Dict):
        """
        Uploads a document to Firestore.

        :param collection_name: Name of the Firestore collection
        :param data: Dictionary containing the document data
        :return: document id for successfully uploaded, error otherwise
        """
        try:
            print("Uploading document to Firestore...")
            _s = time.perf_counter()
            doc_ref = self.db.collection(self.collection_name).add(data)
            _e = time.perf_counter()
            print(f"Document uploaded successfully to document id' {doc_ref[1].id}. Time taken: {_e - _s} seconds.")
            return doc_ref[1].id
        except Exception as e:
            return (f"An error occurred: {e}")

    def get_doc(self, document_id):
        """
        Retrieves a document from Firestore by collection name and document ID.

        :param collection_name: Name of the Firestore collection
        :param document_id: ID of the Firestore document
        :return: Dictionary containing the document data or None if document is not found
        """
        try:
            doc_ref = self.db.collection(self.collection_name).document(document_id)
            doc = doc_ref.get()
            if doc.exists:
                print(f"Document with ID {document_id} retrieved successfully from collection {self.collection_name}.")
                return doc.to_dict()
            else:
                print(f"No document found with ID {document_id} in collection {self.collection_name}.")
                return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
        
    def delete_doc(self, document_id):
        """
        Deletes a document from Firestore by collection name and document ID.

        :param collection_name: Name of the Firestore collection
        :param document_id: ID of the Firestore document
        :return: document is successfully deleted, False otherwise
        """
        try:
            doc_ref = self.db.collection(self.collection_name).document(document_id)
            doc = doc_ref.get()
            if doc.exists:
                doc_ref.delete()
                return f"Document with ID {document_id} deleted successfully from collection {self.collection_name}."
            else:
                print(f"No document found with ID {document_id} in collection {self.collection_name}.")
                return False
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
        
    def update_doc(self, document_id: AnyStr, data: Dict):
        """
        Updates a document in Firestore by collection name and document ID.

        :param collection_name: Name of the Firestore collection
        :param document_id: ID of the Firestore document
        :param data: Dictionary containing the updated document data
        :return: document is successfully updated, error otherwise
        """

        try:
            doc_ref = self.db.collection(self.collection_name).document(document_id)
            doc = doc_ref.get()
            if doc.exists:
                doc_ref.set(data, merge=True)
                return f"Document with ID {document_id} updated successfully in collection {self.collection_name}."
            else:
                print(f"No document found with ID {document_id} in collection {self.collection_name}.")
                return False
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
        

