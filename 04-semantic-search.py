# 语义检索（查询）

from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

# 嵌入模型
embedding = OllamaEmbeddings(model="nomic-embed-text")

# 向量知识库
vector_store = Chroma(
    collection_name="example_collection",
    embedding_function=embedding,
    persist_directory="./chroma_langchain_db",
)

# 相似度查询
# results = vector_store.similarity_search(
#     "介绍一下医疗行业轮班考勤管理系统"
# )

# for index, result in enumerate(results):
#     print(index)
#     print(result.page_content[:100])

# 带分数的相似度查询
# results = vector_store.similarity_search_with_score(
#     "介绍一下医疗行业轮班考勤管理系统"
# )

# for doc, score in results:
#     print(score)
#     print(doc.page_content[:100])

# 用向量进行相似度查询
# vector = embedding.embed_query("介绍一下医疗行业轮班考勤管理系统")

# results = vector_store.similarity_search_by_vector(vector)

# for index, result in enumerate(results):
#     print(index)
#     print(result.page_content[:100])

# 创建向量检索链
# from typing import List
# from langchain_core.documents import Document
# from langchain_core.runnables import chain

# @chain
# def retriever(query: str) -> List[Document]:
#     return vector_store.similarity_search(query, k=1)

# results = retriever.invoke("介绍一下医疗行业轮班考勤管理系统")

# for index, result in enumerate(results):
#     print(index)
#     print(result.page_content[:100])