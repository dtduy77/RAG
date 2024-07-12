# RAG

This project provides a web interface to upload PDF documents and ask questions about their content. It uses a FastAPI backend to process the documents and provide summarized responses, and a Streamlit frontend to create an interactive user interface.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites

- Python 3.7+
- `pip` (Python package installer)

### Steps

1. Clone the repository:

```bash
git clone https://github.com/dtduy77/RAG.git
cd RAG
```

2. Create and activate a virtual environment:

```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Run the FastAPI server:

```bash
uvicorn main:app --reload
```

5. Run the Streamlit app in another terminal:

```bash
streamlit run app.py
```

## Usage

1. Open your web browser and go to http://localhost:8501.

2. Use the file uploader to select a PDF document.

3. Enter a question related to the content of the document.

4. Click on "Get Summary" to receive a summarized response.

## Contributing

1. Fork the repository.

2. Create a new branch (git checkout -b feature/your-feature).

3. Make your changes.

4. Commit your changes (git commit -m 'Add your message').

5. Push to the branch (git push origin feature/your-feature).

6. Open a Pull Request.

## License

This project is open-source.

Feel free to contribute and enhance the functionality!
