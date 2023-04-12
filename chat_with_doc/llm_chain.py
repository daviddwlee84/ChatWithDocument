from typing import List
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.schema import Document
import tiktoken
import os
from dotenv import load_dotenv
from vector_store import AnnRecall

load_dotenv('../.env')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')


class LLMChain:
    def __init__(self, doc_embedding_path: str, ann_output_path: str, engine: str = 'OpenAI', temperature: int = 0, debug: bool = False) -> None:
        assert engine in ['OpenAI']
        self.engine = engine

        self.debug = debug

        self.llm = OpenAI(temperature=0, openai_api_key=OPENAI_API_KEY)
        # https://python.langchain.com/en/latest/modules/chains/index_examples/question_answering.html
        self.chain = load_qa_chain(self.llm, chain_type='stuff')
        self.ann_recall = AnnRecall()
        self.ann_recall.load_index(doc_embedding_path, ann_output_path)

        # self.bpe = tiktoken.get_encoding('cl100k_base')
        self.bpe = tiktoken.encoding_for_model('text-embedding-ada-002')

    def _context_length_stripper(self, query: str, docs: List[Document], max_context_length: int = 4097):
        """
        https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them
        https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb
        gpt-3.5-turbo, text-embedding-ada-002 use cl100k_base
        https://github.com/hwchase17/langchain/blob/b92a89e29f85d6b90796c24cdd952be76fb64a23/langchain/chains/question_answering/stuff_prompt.py#L4
        raise self.handle_error_response(openai.error.InvalidRequestError: This model's maximum context length is 4097 tokens, however you requested 4170 tokens (3914 in your prompt; 256 for the completion). Please reduce your prompt; or completion length.
        """

        # TODO: use customized prompt for each language
        curr_length = 4170 - 2173  # Estimated prompt token length
        query_length = len(self.bpe.encode(query))
        curr_length += query_length

        new_docs = []
        for doc in docs:
            doc_length = len(self.bpe.encode(doc.page_content))
            if curr_length + doc_length > max_context_length:
                break
            new_docs.append(doc)
            curr_length += doc_length

        if self.debug:
            print(curr_length)

        return new_docs

    def qa_chain(self, query: str) -> str:
        docs = self.ann_recall.similarity_search(query)
        if self.debug:
            print('Recalled doc length:', len(docs))
        docs = self._context_length_stripper(query, docs)

        if self.debug:
            print('Final doc length:', len(docs))
            print('Recalled content:')
            print(docs)

        return self.chain.run(input_documents=docs, question=query)


if __name__ == '__main__':
    from document_encoder import DocumentEncoder
    from vector_store import ANNIndexBuilder
    file_path = '../sample_data/huawei-llm-research.pdf'
    embed_path = DocumentEncoder._get_default_output_file_path(file_path)
    ann_path = ANNIndexBuilder._get_default_output_file_path(embed_path)

    llm = LLMChain(embed_path, ann_path, debug=True)
    # print(llm.qa_chain('华为净利率成长多少?'))  # I don't know
    # print(llm.qa_chain('2021年华为毛利率是多少?'))  # I don't know (this is weird, the document with the answer should be recalled)
    print(llm.qa_chain('请给出本研报的总结'))  # 麒麟信安携手华为欧拉共筑国产操作系统新生态 (not good)
