# BeerCan
Somes python scripts to use openAI and other LLM and other stuff

Vector Database for Document Search and Question Answering

This repository contains Python scripts that enable the creation of a vector database using Pinecone, a vector search service. The code in this repository is heavily inspired by the work in the gkamradt/langchain-tutorials repository. It provides functionality to perform document search and question answering tasks on large PDF files consisting of hundreds of pages.
Installation

To use the scripts, please follow these steps:

    Clone this repository to your local machine.
    Install the necessary packages by running the command:

    pip install -r requirements.txt

    Ensure that you have Python 3.7 or above installed on your system.

Usage

The provided scripts are based on the work in gkamradt/langchain-tutorials and allow you to create a vector database for document search and question answering:

    Run the main.py script using Python.
    A file dialog will appear, allowing you to select a PDF file.
    After selecting a file, the script will load the data, initialize the Pinecone vector search, and prepare the document for querying.
    Enter your query when prompted, and the script will return relevant answers from the document.

The code leverages Pinecone's similarity search capabilities and utilizes OpenAI's language model for question answering tasks. It efficiently handles large PDF files by converting them into a vector representation.

The database created through this process empowers you to search and retrieve information from multi-page PDF documents using natural language queries.

Please note that the scripts provided here are inspired by the work in gkamradt/langchain-tutorials and may require further customization or optimization for specific use cases or production environments.
License

This project is licensed under the MIT License.

Feel free to explore, modify, and enhance the scripts according to your specific requirements and use cases.
