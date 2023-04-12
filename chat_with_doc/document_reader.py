from typing import List
from langchain.document_loaders import UnstructuredPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from py_pdf_parser.loaders import load_file
from py_pdf_parser.visualise import visualise
from dotenv import load_dotenv

load_dotenv('../.env')


# TODO: do document clean up to reduce noise
class DocumentReader(object):
    def __init__(self, engine: str = 'UnstructuredPDFLoader', chunk_size: int = 1000, debug: bool = False) -> None:
        assert engine in ['UnstructuredPDFLoader', 'PyPDFParser']
        self.engine = engine
        self.debug = debug

        self.chunk_size = chunk_size
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size, chunk_overlap=0)

    def load_pdf(self, file_path: str) -> str:
        if self.engine == 'UnstructuredPDFLoader':
            # TODO: try `element` mode
            pdf_loader = UnstructuredPDFLoader(file_path, mode='single')
            list_of_doc = pdf_loader.load()
            if self.debug:
                print('Number of documents:', len(list_of_doc))
            return '\n'.join(doc.page_content for doc in list_of_doc)
        elif self.engine == 'PyPDFParser':
            # TODO: we need to select element case by case to avoid noise content,
            # now we ignore it for the generalize ability

            # https://py-pdf-parser.readthedocs.io/en/latest/reference/filtering.html#filtering-reference
            entire_document = load_file(file_path)
            if self.debug:
                print('Number of pages:', entire_document.number_of_pages)
                print('Number of elements:', len(entire_document.elements))
                # visualise(entire_document)

            return '\n'.join(element.text() for element in entire_document.elements)

        raise NotImplementedError()

    def load_pdf_and_split(self, file_path: str) -> List[str]:
        if self.engine == 'UnstructuredPDFLoader':
            pdf_loader = UnstructuredPDFLoader(file_path)

            # splitted_list_of_doc = pdf_loader.load_and_split(
            #     self.text_splitter)

            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=self.chunk_size, chunk_overlap=0)
            splitted_list_of_doc = pdf_loader.load_and_split(
                text_splitter)

            if self.debug:
                print('Number of pages:', len(splitted_list_of_doc))

            return [doc.page_content for doc in splitted_list_of_doc]

        elif self.engine == 'PyPDFParser':
            # TODO: chunk each page
            entire_document = load_file(file_path)
            if self.debug:
                print('Number of pages:', entire_document.number_of_pages)
                print('Number of elements:', len(entire_document.elements))
                # visualise(entire_document)

            return ['\n'.join(element.text() for element in page.elements) for page in entire_document.pages]

        raise NotImplementedError()


def _debug_UnstructuredPDFLoader(file_path: str) -> None:
    """
    This is super slow on a regular computer (Probably due to requiring running the OCR model)
    """
    reader = DocumentReader(engine='UnstructuredPDFLoader', debug=True)

    document = reader.load_pdf(file_path)
    print(document)

    splitted_list_of_doc = reader.load_pdf_and_split(file_path)
    print(splitted_list_of_doc[:3])

    # pdf_loader = UnstructuredPDFLoader(file_path)
    # list_of_doc = pdf_loader.load()  # len(list_of_doc) == 1
    # splitted_list_of_doc2 = reader.text_splitter.split_documents(
    #     list_of_doc)  # len(splitted_list_of_doc2) == 229
    #
    # print(splitted_list_of_doc2[:3])

    import ipdb
    ipdb.set_trace()


def _debug_PyPDFParser(file_path: str) -> None:
    """
    (Can't detect elements from the field-guide-to-data-science.pdf)
    """
    reader = DocumentReader(engine='PyPDFParser', debug=True)

    document = reader.load_pdf(file_path)
    print(document)

    splitted_list_of_doc = reader.load_pdf_and_split(file_path)
    print(splitted_list_of_doc[:3])
    import ipdb
    ipdb.set_trace()


if __name__ == '__main__':
    file_path = '../sample_data/field-guide-to-data-science.pdf'
    _debug_UnstructuredPDFLoader(file_path)

    file_path = '../sample_data/huawei-llm-research.pdf'
    _debug_PyPDFParser(file_path)
