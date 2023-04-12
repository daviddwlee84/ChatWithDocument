from typing import Dict, List, Tuple
from annoy import AnnoyIndex
from document_encoder import DocumentEncoder
from representation import Representation
import os


class ANNIndexBuilder(object):
    """
    Build ANN index for documents
    """

    def __init__(self, engine: str = 'annoy', annoy_metric: str = 'angular', annoy_tree_num: int = 10):
        assert engine in ['annoy']
        assert annoy_metric in ['angular', 'euclidean',
                                'manhattan', 'hamming', 'dot']
        self.engine = engine
        self.annoy_metric = annoy_metric
        self.annoy_tree_num = annoy_tree_num

    @staticmethod
    def _get_default_output_file_path(doc_embedding_path: str):
        return os.path.join(os.path.dirname(
            doc_embedding_path), os.path.basename(doc_embedding_path) + '.annoy.ann')

    def build_index_from_document_embedding(self, doc_embedding_path: str, ann_output_path: str = None, override: bool = False) -> None:
        if not ann_output_path:
            ann_output_path = self._get_default_output_file_path(
                doc_embedding_path)

        if not override and os.path.exists(ann_output_path):
            print(
                f'ANN index of the {doc_embedding_path} already exist, skipped!')
            return

        data = DocumentEncoder.load(doc_embedding_path)
        assert len(data) > 0 and '0' in data

        if self.engine == 'annoy':
            emb_dim = len(data['0']['Embedding'])
            ann_index = AnnoyIndex(emb_dim, self.annoy_metric)

            # Add index
            for doc_id, item in data.items():
                ann_index.add_item(int(doc_id), item['Embedding'])

            # Build index
            ann_index.build(self.annoy_tree_num)

            # Save index
            ann_index.save(ann_output_path)

            return

        raise NotImplementedError()


class AnnRecall(object):
    def __init__(self, engine: str = 'annoy', annoy_metric: str = 'angular', encoder_engine: str = 'OpenAI', chunk_size: int = 1000):
        assert engine in ['annoy']
        assert annoy_metric in ['angular', 'euclidean',
                                'manhattan', 'hamming', 'dot']
        self.ann_engine = engine
        self.annoy_metric = annoy_metric
        self.encoder_engine = encoder_engine
        self.chunk_size = chunk_size
        self.encoder = Representation(engine=encoder_engine)

    def load_index(self, doc_embedding_path: str, ann_path: str):
        """
        To continuous build index from last checkpoint use this function
        (not sure if it's possible...)
        """
        self.data = DocumentEncoder.load(doc_embedding_path)
        if self.ann_engine == 'annoy':
            emb_dim = len(self.data['0']['Embedding'])
            self.ann_index = AnnoyIndex(emb_dim, self.annoy_metric)
            self.ann_index.load(ann_path)
            return

        raise NotImplementedError()

    def _retrieve_topk_ids(self, query: str, topk: int = 10) -> List[Tuple[int, float]]:
        query_embedding = self.encoder.embed_document(query)
        matches, distances = self.ann_index.get_nns_by_vector(
            query_embedding, topk, include_distances=True)
        match_result = [(match, distance)
                        for match, distance in zip(matches, distances)]
        match_result.sort(key=lambda x: x[1], reverse=True)
        return match_result

    def recall_topk_document(self, query: str, topk: int = 10) -> List[Tuple[Dict[str, str], float]]:
        """
        TODO: maybe add ANN threshold & minimum recall number
        """
        match_result = self._retrieve_topk_ids(query, topk)
        doc_result = []
        for doc_id, score in match_result:
            original_doc = self.data[str(doc_id)]['Document']
            doc_result.append((original_doc, score))
        return doc_result


if __name__ == "__main__":
    file_path = '../sample_data/huawei-llm-research.pdf'
    embed_path = DocumentEncoder._get_default_output_file_path(file_path)
    ann_path = ANNIndexBuilder._get_default_output_file_path(embed_path)

    encoder = DocumentEncoder(document_engine='PyPDFParser')
    encoder.encode(file_path)

    ann_index = ANNIndexBuilder()
    ann_index.build_index_from_document_embedding(embed_path)

    ann_recall = AnnRecall()
    ann_recall.load_index(embed_path, ann_path)

    # NOTE: this will call embedding API
    results = ann_recall.recall_topk_document('LLM大模型')
    print(results)
    results2 = ann_recall.recall_topk_document('华为的毛利率与净利率')
    print(results2)
    import ipdb
    ipdb.set_trace()
