class Reflector:
    def __init__(self):
        self.training_signals = []

    def analyze_results(self, results):
        # Analyze the results and extract training signals
        training_signal = self.extract_training_signal(results)
        self.training_signals.append(training_signal)

    def extract_training_signal(self, results):
        # Placeholder for logic to extract training signals from results
        return {"signal": "example_signal", "data": results}

    def get_training_signals(self):
        return self.training_signals

    def reset(self):
        self.training_signals.clear()