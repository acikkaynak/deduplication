from environs import Env

env = Env()
env.read_env()

APP_HOST = env.str("APP_HOST", "0.0.0.0")
APP_PORT = env.int("APP_PORT", 8000)

MILVUS_DB_ALIAS = env.str("MILVUS_DB_ALIAS")
MILVUS_DB_URI = env.str("MILVUS_DB_URI")
MILVUS_DB_USERNAME = env.str("MILVUS_DB_USERNAME")
MILVUS_DB_PASSWORD = env.str("MILVUS_DB_PASSWORD")
MILVUS_DB_SECURE = env.str("MILVUS_DB_SECURE").lower() == "true"

MILVUS_SEARCH_THRESHOLD = env.float("MILVUS_SEARCH_THRESHOLD")
