from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import GPT4AllEmbeddings
from langchain.schema import Document 
from langchain_community.vectorstores.chroma import Chroma
from dotenv import load_dotenv
import os
import shutil 
from uuid import uuid4


class Document:
    def __init__(self, page_content, metadata):
        self.page_content = page_content
        self.metadata = metadata

class my_vector_store():
    def __init__(self):
            embedder = GPT4AllEmbeddings(model_name="all-MiniLM-L6-v2.gguf2.f16.gguf")
            CHROMA_PATH = "chroma_VDB"
            self.vector_store = Chroma(
                collection_name="generic",
                embedding_function=embedder,
                persist_directory=CHROMA_PATH
            )

    def chunker(self,text):
        documents = [Document(page_content=page, metadata={"page_number": i}) for i, page in enumerate(text)]

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500, # Size of each chunk in characters
            chunk_overlap=100, # Overlap between consecutive chunks
            length_function=len, # Function to compute the length of the text
            add_start_index=True, # Flag to add start index to each chunk
        )

        chunks = text_splitter.split_documents(documents)
        print(f"Split {len(documents)} documents into {len(chunks)} chunks.")

        document = chunks[0]
        # print(document.page_content)
        # print(document.metadata)

        # if os.path.exists(CHROMA_PATH):
        #     shutil.rmtree(CHROMA_PATH)

        self.vector_store.add(
            chunks,
        )

        # Persist the database to disk
        self.vector_store.persist()
        print(f"Saved {len(chunks)} chunks")


    def context_retreiver(self,text):
        retreiver= self.vector_store.as_retriever()      
        return retreiver.invoke(text)

    def add_documents(self, documents):
        uuids = [str(uuid4()) for _ in range(len(documents))]

        self.vector_store.add_documents(documents=documents, ids=uuids)
    
    def v_similarity(self,query,k:None=1):
         return self.vector_store.similarity_search_with_score(
    query=query,
    k=k)