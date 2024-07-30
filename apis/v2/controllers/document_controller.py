import fitz # (pymupdf, found this is better than pypdf for our use case, note: licence is AGPL-3.0, keep that in mind if you want to use any code commercially)
from tqdm.auto import tqdm # for progress bars, requires !pip install tqdm 
from langchain_text_splitters import RecursiveCharacterTextSplitter
import pandas as pd
class Document:
    def __init__(self, metadata, page_content):
        self.metadata = metadata
        self.page_content = page_content

    def __repr__(self):
        return f"Document(metadata={self.metadata}, page_content=\"{self.page_content}\")"  # Hiển thị chỉ 30 ký tự đầu tiên của nội dung
doc = Document(
    metadata={'source': 'dataset_fpt_rag.pdf', 'page': 0},
    page_content="Tôi tên Tùng"
)
def split_chunk(pdf_path,chunk_size=1000, chunk_overlap=200):
    doc = fitz.open(pdf_path)  # open a document
    pages_and_texts = []
    for page_number, page in tqdm(enumerate(doc)):  # iterate the document pages
        text = page.get_text()  # get plain text encoded as UTF-8
        doc = Document(
        metadata={'source': 'dataset_fpt_rag.pdf', 'page': page_number+1},
        page_content=text
        )
        pages_and_texts.append(doc)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    splits = text_splitter.split_documents(pages_and_texts)
    return splits
def split_to_df(splits_chunk):
    split_contents = [split.page_content for split in splits_chunk]
    # Tạo DataFrame từ các nội dung văn bản
    dataset_df = pd.DataFrame({
        'chunk_id': range(len(split_contents)),  # ID hoặc chỉ số cho mỗi đoạn văn bản
        'text': split_contents                   # Nội dung của từng đoạn
    })
    return dataset_df
if __name__ == "__main__":
    pdf_path = 'dataset_fpt_rag.pdf'
    splits_chunk_list = split_chunk(pdf_path)
    dataset_df = split_to_df(splits_chunk_list)
