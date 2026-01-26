class Metrics:
    def __init__(self):
        self.performance_data = []

    def record_performance(self, agent_id, metric_value):
        self.performance_data.append({'agent_id': agent_id, 'metric_value': metric_value})

    def calculate_average_performance(self):
        if not self.performance_data:
            return 0
        total = sum(entry['metric_value'] for entry in self.performance_data)
        return total / len(self.performance_data)

    def reset_metrics(self):
        self.performance_data = []

    def get_metrics_summary(self):
        return {
            'total_agents': len(set(entry['agent_id'] for entry in self.performance_data)),
            'average_performance': self.calculate_average_performance(),
            'raw_data': self.performance_data
        }