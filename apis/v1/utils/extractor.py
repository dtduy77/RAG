import os
from fastapi import HTTPException, status
from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader


def _load_pdf_docx(filepath: str):
    '''
    Load the PDF or DOCX file and split the content into the list of documents.
    '''
    if os.path.basename(filepath).endswith(".pdf") or os.path.basename(filepath).endswith(".PDF"):
        loader = PyPDFLoader(filepath)

    elif os.path.basename(filepath).endswith(".docx") or os.path.basename(filepath).endswith(".DOCX"):
        loader = Docx2txtLoader(filepath)

    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="File type not supported."
        )

    # Load and split the content
    return loader.load_and_split()

def get_content(file_path: str) -> str:
    '''
    Get the content of the file.
    '''
    try:
        data = _load_pdf_docx(file_path)
        content = ""
        
        for _data in data:

            _content = [line.strip()
                        for line in _data.page_content.splitlines() if line.strip() != ""]
            content += "\n".join(_content) + "\n"
        
        return content
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
       )

