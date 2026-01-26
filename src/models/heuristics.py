class Heuristic:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def apply(self, context):
        raise NotImplementedError("This method should be overridden by subclasses.")

class SimpleHeuristic(Heuristic):
    def __init__(self):
        super().__init__("Simple Heuristic", "A basic heuristic for demonstration purposes.")

    def apply(self, context):
        # Implement the logic for the simple heuristic
        return context * 2  # Example operation

class ComplexHeuristic(Heuristic):
    def __init__(self):
        super().__init__("Complex Heuristic", "A more complex heuristic that considers multiple factors.")

    def apply(self, context):
        # Implement the logic for the complex heuristic
        return context + 10  # Example operation

def get_available_heuristics():
    return [SimpleHeuristic(), ComplexHeuristic()]