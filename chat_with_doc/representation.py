from typing import List
from langchain.embeddings.openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv('../.env')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')


class Representation(object):
    def __init__(self, engine: str = 'OpenAI'):
        assert engine in ['OpenAI']

        self.engine = engine

        if engine == 'OpenAI':
            self.embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
            # This is default embedding size of the model text-embedding-ada-002
            # TODO: get a `model: dim` mapping
            self.dim = 1536
        else:
            raise NotImplementedError()

    def embed_document(self, document: str) -> List[float]:
        if self.engine == 'OpenAI':
            return self.embeddings.embed_query(document)

        # TODO: support other engine
        raise NotImplementedError()

    def embed_documents(self, documents: List[str], chunk_size: int = 1000) -> List[List[float]]:
        if self.engine == 'OpenAI':
            return self.embeddings.embed_documents(documents, chunk_size)

        # TODO: support other engine
        raise NotImplementedError()


def _test_chinese_document():
    from document_reader import DocumentReader
    reader = DocumentReader(engine='PyPDFParser')
    file_path = '../sample_data/huawei-llm-research.pdf'
    docs = reader.load_pdf_and_split(file_path)
    print(docs[5])

    encoder = Representation()
    embedding = encoder.embed_document(docs[5])
    print(embedding)

    embeddings = encoder.embed_documents(docs[5:10])
    print(embeddings)

    import ipdb
    ipdb.set_trace()


if __name__ == '__main__':
    _test_chinese_document()
