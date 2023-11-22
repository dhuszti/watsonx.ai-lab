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
import streamlit as st

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
    "apikey": "_to_be_replaced_"
}

project_id = "_to_be_replaced_"


model = Model(
    model_id=model_id,
    params=parameters,
    credentials=credentials,
    project_id=project_id
)

@st.cache_resource
def load_data():
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
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50, separators=["\n"])
    texts = text_splitter.split_documents(documents)

    # Create embeddings
    embeddings = HuggingFaceEmbeddings()
    docsearch = Chroma.from_documents(texts, embeddings)

    qa = RetrievalQA.from_chain_type(llm=model.to_langchain(), chain_type="stuff", retriever=docsearch.as_retriever())

    return qa


# Main Streamlit app
if __name__ == "__main__":
    # Execute the main function at the start of the app
    qa = load_data()

    # Title for the app
    st.title('🤖 Első Watsonx.ai alkalmazásom')
    # Prompt box
    prompt = st.text_input('Add meg a kérdésed')
    prompt = prompt + " Válaszolj magyarul."

    # If a user hits enter
    if prompt:
        # Pass the prompt to the llm
        response = qa.run(prompt)
        # Write the output to the screen
        st.write(response)
