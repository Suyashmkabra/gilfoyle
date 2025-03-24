from rag import my_vector_store

vcs= my_vector_store()
print(vcs.context_retreiver("Breast Cancer"))