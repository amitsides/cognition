# Configuration settings for the Agentic Cognition MAS application

class Config:
    """Configuration settings for the Agentic Cognition MAS application."""
    
    # General settings
    DEBUG = True
    LOG_LEVEL = 'INFO'
    
    # Agent parameters
    AGENT_TIMEOUT = 5  # seconds
    MAX_RETRIES = 3
    
    # Memory settings
    MEMORY_CAPACITY = {
        'sensory_buffer': 100,
        'working_memory': 50,
        'episodic_memory': 200,
        'semantic_memory': 1000
    }
    
    # Heuristic settings
    HEURISTIC_THRESHOLD = 0.7
    
    # Tree-of-Thoughts settings
    TOT_MAX_DEPTH = 5
    TOT_PRUNING_FACTOR = 0.5
    
    # Other parameters can be added as needed
    # ...