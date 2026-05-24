# 索引（建库）

## 1.读取PDF：按照页（Document）来管理, 最终形成List[Document]
## 2.分割文本：分割成文本段（chunk）,按照页Document来分割，最终形成List[Document]
## 3.向量化：文本段 <=> 向量，需要嵌入模型来进行转换
## 4.向量库：把多个文本段和向量存到向量库里

# pip install pypdf

# 1.读取PDF
from langchain_community.document_loaders import PyPDFLoader

# 文件路径
file_path = "./pdf.pdf"

loader = PyPDFLoader(file_path)

docs = loader.load()

# 2.分割问本
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 创建文本分割器
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, 
    chunk_overlap=200,
    add_start_index=True,
)

# 切分文本
all_splits = text_splitter.split_documents(docs)

print(len(all_splits))

# 3.向量化
# 这是本地的嵌入模型，需要当前本地安装了ollama，且下载了嵌入模型
from langchain_ollama import OllamaEmbeddings

# 初始话embedding模型
embedding = OllamaEmbeddings(model="nomic-embed-text")

# 将第一个chunk转为向量
# 转换后vector_0的值将是一个存储一堆浮点数的列表
# 这里只是教学，因此只转换第一个chunk，在后续也不会使用
vector_0 = embedding.embed_query(all_splits[0].page_content)

# 4.向量库存储
from langchain_chroma import Chroma

# 创建向量数据库
vector_store = Chroma(
    collection_name="example_collection",
    embedding_function=embedding,
    persist_directory="./chroma_langchain_db",
)

# 将全部all_splits转换成向量存入向量数据库中
ids = vector_store.add_documents(documents=all_splits)

print(ids)