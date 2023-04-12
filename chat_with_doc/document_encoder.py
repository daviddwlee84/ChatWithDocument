from typing import Dict
import os
import json
from document_reader import DocumentReader
from representation import Representation


class DocumentEncoder(object):
    def __init__(self, document_engine: str = 'PyPDFParser', encoder_engine: str = 'OpenAI', chunk_size: int = 1000) -> None:
        self.doc_reader = DocumentReader(
            engine=document_engine, chunk_size=chunk_size)
        self.chunk_size = chunk_size
        self.encoder = Representation(engine=encoder_engine)

    def encode(self, input_file_path: str, output_file_path: str = None, override: bool = False) -> Dict[str, dict]:
        assert input_file_path.endswith(
            '.pdf'), 'Currently, self.doc_reader only support pdf file'

        if not output_file_path:
            output_file_path = os.path.join(os.path.dirname(
                input_file_path), os.path.basename(input_file_path) + '.embed.json')

        if not override and os.path.exists(output_file_path):
            print(
                f'Embedding of the {input_file_path} already exist, skipped! (saved quota)')
            return self.load(output_file_path)

        # NOTE: currently, self.doc_reader only support pdf file
        docs = self.doc_reader.load_pdf_and_split(input_file_path)
        embeddings = self.encoder.embed_documents(docs, self.chunk_size)

        data = {}

        for doc_id, (doc, emb) in enumerate(zip(docs, embeddings)):
            data[doc_id] = {
                'Document': doc,
                'Embedding': emb
            }

        with open(output_file_path, 'w', encoding='utf-8') as fp:
            json.dump(data, fp, ensure_ascii=False)

        return data

    def load(self, file_path: str) -> Dict[str, dict]:
        with open(file_path, 'r', encoding='utf-8') as fp:
            return json.load(fp)


if __name__ == '__main__':
    file_path = '../sample_data/huawei-llm-research.pdf'
    encoder = DocumentEncoder(document_engine='PyPDFParser')
    data = encoder.encode(file_path)

    embed_file_path = os.path.join(os.path.dirname(
        file_path), os.path.basename(file_path) + '.embed.json')
    data2 = encoder.load(embed_file_path)

    import ipdb
    ipdb.set_trace()
