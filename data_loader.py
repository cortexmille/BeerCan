# PDF Loaders. If unstructured gives you a hard time, try PyPDFLoader
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_data(file_path, file_name):
    if file_path.endswith(".pdf"):
        loader = PyPDFLoader(file_path)
    else:
        print("Format de fichier non pris en charge. Veuillez fournir un fichier PDF.")
        return None

    data = loader.load()

    print(f'Vous avez {len(data)} document(s) dans vos données')
    print(f'Il y a {len(data[0].page_content)} caractères dans votre document')

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=0)
    texts = text_splitter.split_documents(data)

    print(f'Maintenant vous avez {len(texts)} documents')
    return texts

def initialize_pinecone(texts, file_name):
    from langchain.vectorstores import Pinecone
    from langchain.embeddings.openai import OpenAIEmbeddings
    import pinecone

    embeddings = OpenAIEmbeddings(openai_api_key='YOUR KEY')

    pinecone.init(
        api_key='YOUR KEY',  # find at app.pinecone.io
        environment='YOUR ENV'  # next to api key in console 
    )
    active_indexes = pinecone.list_indexes()
    print("Active indexes:", active_indexes)
    
    index_name = input("Veuillez entrer le nom de l'index Pinecone existant : ")  # ask user for index name

    # ask user if they want to add new data to existing index or delete and create new index
    reset_index = input("Voulez-vous ajouter les nouvelles données à l'index existant ou le supprimer et en créer un nouveau ? (add/supprimer) : ")

    if reset_index.lower() == 'supprimer':
        print("Suppression de l'index existant et création d'un nouvel index...")
        pinecone.delete_index(index_name)  # delete existing index
        # add code to create new index with same name here. Make sure to add the correct dimension.
        pinecone.create_index(index_name, dimension=1536)  # replace 1024 with correct dimension

    docsearch = Pinecone.from_texts([f"{file_name} - {t.page_content}" for t in texts], embeddings, index_name=index_name)
    return docsearch

