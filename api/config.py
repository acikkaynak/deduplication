from environs import Env

env = Env()
env.read_env()

DEDUPLICATION_API_KEY = env.str("DEDUPLICATION_API_KEY")

MILVUS_DB_ALIAS = env.str("MILVUS_DB_ALIAS", "default")
MILVUS_DB_URI = env.str("MILVUS_DB_URI")  # host
MILVUS_DB_PORT = env.str("MILVUS_DB_PORT", "19530")
MILVUS_DB_COLLECTION_NAME = env.str("MILVUS_DB_COLLECTION_NAME", "address")
MILVUS_DB_SEARCH_FIELD = env.str("MILVUS_DB_SEARCH_FIELD", "vector")
MILVUS_DB_SEARCH_LIMIT = env.int("MILVUS_DB_SEARCH_LIMIT", 200)
MILVUS_DB_CONNECTION_TIMEOUT = env.int("MILVUS_DB_CONNECTION_TIMEOUT", 60)

MODEL_NAME = env.str("MODEL_NAME", "loodos/bert-base-turkish-uncased")
