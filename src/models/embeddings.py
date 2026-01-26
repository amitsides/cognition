class EmbeddingModel:
    def __init__(self, embedding_size):
        self.embedding_size = embedding_size
        self.embeddings = {}

    def add_embedding(self, key, vector):
        if len(vector) != self.embedding_size:
            raise ValueError("Vector size must match the embedding size.")
        self.embeddings[key] = vector

    def get_embedding(self, key):
        return self.embeddings.get(key, None)

    def similarity(self, key1, key2):
        vec1 = self.get_embedding(key1)
        vec2 = self.get_embedding(key2)
        if vec1 is None or vec2 is None:
            return None
        return self.cosine_similarity(vec1, vec2)

    @staticmethod
    def cosine_similarity(vec1, vec2):
        dot_product = sum(a * b for a, b in zip(vec1, vec2))
        norm_a = sum(a ** 2 for a in vec1) ** 0.5
        norm_b = sum(b ** 2 for b in vec2) ** 0.5
        if norm_a == 0 or norm_b == 0:
            return 0.0
        return dot_product / (norm_a * norm_b)

class SemanticMemory:
    def __init__(self):
        self.memory = {}

    def store(self, key, value):
        self.memory[key] = value

    def retrieve(self, key):
        return self.memory.get(key, None)

    def clear(self):
        self.memory.clear()