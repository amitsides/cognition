class Archivist:
    def __init__(self):
        self.episodic_memory = []
        self.semantic_memory = {}

    def store_experience(self, experience):
        """Store a new experience in episodic memory."""
        self.episodic_memory.append(experience)

    def store_semantic_trace(self, key, value):
        """Store a semantic trace in semantic memory."""
        self.semantic_memory[key] = value

    def retrieve_experience(self, index):
        """Retrieve an experience from episodic memory."""
        if 0 <= index < len(self.episodic_memory):
            return self.episodic_memory[index]
        return None

    def retrieve_semantic_trace(self, key):
        """Retrieve a semantic trace from semantic memory."""
        return self.semantic_memory.get(key, None)

    def clear_memory(self):
        """Clear episodic memory and semantic memory."""
        self.episodic_memory.clear()
        self.semantic_memory.clear()