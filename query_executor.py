from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain

# Paramètres de génération
params = {
    "max_tokens": 1500,
    "temperature": 0.5,
    "top_p": 1.0
}

def run_query(query, docsearch, file_name):
    llm = OpenAI(openai_api_key='YOUR KEY', **params)
    chain = load_qa_chain(llm, chain_type="stuff")

    print(query)
    docs = docsearch.similarity_search(query)

    print(f"{file_name}: {chain.run(input_documents=docs, question=query)}")
