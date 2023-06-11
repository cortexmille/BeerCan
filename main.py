# Vector Database for Document Search and Question Answering

# This repository contains Python scripts that enable the creation of a vector database using Pinecone, a vector search service. The code in this repository is heavily inspired by the work in the gkamradt/langchain-tutorials repository. It provides functionality to perform document search and question answering tasks on large PDF files consisting of hundreds of pages.

# Please note that the scripts provided here are inspired by the work in gkamradt/langchain-tutorials and may require further customization or optimization for specific use cases or production environments.
# License
# This project is licensed under the MIT License.


from tkinter import Tk
from tkinter.filedialog import askopenfilename
from data_loader import load_data, initialize_pinecone
from query_executor import run_query

def main():
    # Ouvrir la fenêtre de dialogue pour sélectionner un fichier
    Tk().withdraw()
    file_path = askopenfilename(title="Sélectionner un fichier PDF")

    # Vérifier si un fichier a été sélectionné
    if not file_path:
        print("Aucun fichier sélectionné.")
        return

    # Récupérer le nom du fichier à partir du chemin complet
    file_name = file_path.split("/")[-1]

    # Chargement des données
    texts = load_data(file_path, file_name)
    if texts is None:
        return

    # Initialisation de Pinecone
    docsearch = initialize_pinecone(texts, file_name)
    if docsearch is None:
        return

    while True:
        user_query = input("Entrez votre requête (ou 'exit' pour quitter) : ")
        if user_query == 'exit':
            break
        run_query(user_query, docsearch, file_name)

if __name__ == "__main__":
    main()
