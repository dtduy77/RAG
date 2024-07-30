import torch
from time import perf_counter as timer
from ..configs.word_embedding_config import embedding_model, SentenceTransformer,util

def retrieve_relevant_resources(query: str,
                                embeddings: torch.tensor,
                                model: SentenceTransformer=embedding_model,
                                n_resources_to_return: int=2,
                                print_time: bool=True):
    query_embedding = model.encode(query, 
                                    convert_to_tensor=True) 
    start_time = timer()
    dot_scores = util.dot_score(query_embedding, embeddings)[0]
    end_time = timer()
    if print_time:
        print(f"[INFO] Time taken to get scores on {len(embeddings)} embeddings: {end_time-start_time:.5f} seconds.")
    scores, indices = torch.topk(input=dot_scores, 
                                    k=n_resources_to_return)
    return scores, indices
def get_data_source(df,indices):
    data = ''
    for i in indices:
        text = df["text"][indices[0].detach().cpu().numpy()]
        data += text + '\n'
    return data