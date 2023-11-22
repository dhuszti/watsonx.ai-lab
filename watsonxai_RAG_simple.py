import os, ssl, wget
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams
from ibm_watson_machine_learning.foundation_models.utils.enums import DecodingMethods
from ibm_watson_machine_learning.foundation_models import Model
from langchain.chains import RetrievalQA

ssl._create_default_https_context = ssl._create_unverified_context

model_id = "meta-llama/llama-2-70b-chat"

parameters = {
    GenParams.DECODING_METHOD: DecodingMethods.GREEDY,
    GenParams.MIN_NEW_TOKENS: 1,
    GenParams.MAX_NEW_TOKENS: 100,
    GenParams.STOP_SEQUENCES: ["\n\n"]
}

credentials = {
    "url": "https://us-south.ml.cloud.ibm.com",
    "apikey": "3ECK93_KGTnhh95d51Eb-3bdM-FtLYo9lzontmTTNl5i"
}

project_id = "18265bd9-4b55-4658-8c6b-2d785f2f9d16"


model = Model(
    model_id=model_id,
    params=parameters,
    credentials=credentials,
    project_id=project_id
)

# Download document
url = 'https://raw.githubusercontent.com/dhuszti/watsonx.ai-lab/main/output.txt'
filename = 'output.txt'

if not os.path.isfile(filename):
    wget.download(url, out=filename)

documents = []

# Load document
loader = TextLoader(filename)
documents.extend(loader.load())

# Build up knowledge base¶
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
texts = text_splitter.split_documents(documents)

# Create embeddings
embeddings = HuggingFaceEmbeddings()
docsearch = Chroma.from_documents(texts, embeddings)

qa = RetrievalQA.from_chain_type(llm=model.to_langchain(), chain_type="stuff", retriever=docsearch.as_retriever())

# Sample python input
while True:
    # Ask a question
    query = input("Kérem adja meg a kérdését: ")
    query = query + " Válaszolj magyarul."
    answer = qa.run(query)
    print('Válasz: ' + answer)
    # Docsearch similarity
    #print(docsearch.similarity_search(query))
