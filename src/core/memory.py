class HierarchicalMemory:
    def __init__(self):
        self.sensory_buffer = []
        self.working_memory = {}
        self.episodic_memory = []
        self.long_term_memory = {}
        self.meta_memory = {}

    def add_to_sensory_buffer(self, event):
        self.sensory_buffer.append(event)

    def clear_sensory_buffer(self):
        self.sensory_buffer.clear()

    def set_working_memory(self, context):
        self.working_memory = context

    def add_to_episodic_memory(self, experience):
        self.episodic_memory.append(experience)

    def add_to_long_term_memory(self, key, value):
        self.long_term_memory[key] = value

    def update_meta_memory(self, agent_id, reliability):
        self.meta_memory[agent_id] = reliability

    def get_memory_snapshot(self):
        return {
            "sensory_buffer": self.sensory_buffer,
            "working_memory": self.working_memory,
            "episodic_memory": self.episodic_memory,
            "long_term_memory": self.long_term_memory,
            "meta_memory": self.meta_memory,
        }