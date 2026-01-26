class Planner:
    def __init__(self):
        self.hierarchical_plans = []
        self.tot_seeds = []

    def generate_plan(self, goal):
        # Logic to generate a hierarchical plan based on the given goal
        pass

    def create_tot_seed(self, context):
        # Logic to create a Tree-of-Thoughts seed based on the current context
        pass

    def refine_plan(self, plan):
        # Logic to refine an existing plan
        pass

    def evaluate_plan(self, plan):
        # Logic to evaluate the effectiveness of a plan
        pass

    def get_hierarchical_plans(self):
        return self.hierarchical_plans

    def get_tot_seeds(self):
        return self.tot_seeds