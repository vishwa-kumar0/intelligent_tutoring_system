class BayesianKnowledgeTracing:
    def __init__(self, p_init=0.3, p_trans=0.2, p_slip=0.1, p_guess=0.2):
        self.p_init = p_init
        self.p_trans = p_trans
        self.p_slip = p_slip
        self.p_guess = p_guess
        self.students = {}

    def get_student_mastery(self, student_id):
        if student_id not in self.students:
            self.students[student_id] = {
                "for_loop": self.p_init,
                "while_loop": self.p_init,
                "function_definition": self.p_init,
                "nested_loops": self.p_init
            }
        return self.students[student_id]

    def update_concept(self, student_id, concept, success):
        mastery = self.get_student_mastery(student_id)
        if concept not in mastery:
            mastery[concept] = self.p_init
        p_prev = mastery[concept]
        
        if success:
            p_obs = p_prev * (1 - self.p_slip) / (p_prev * (1 - self.p_slip) + (1 - p_prev) * self.p_guess)
        else:
            p_obs = p_prev * self.p_slip / (p_prev * self.p_slip + (1 - p_prev) * (1 - self.p_guess))
            
        p_new = p_obs + (1 - p_obs) * self.p_trans
        mastery[concept] = round(p_new, 4)

    def update_session(self, student_id, concepts, issues):
        failed_concepts = set()
        for issue in issues:
            if issue['type'] == 'infinite_while_loop': failed_concepts.add('while_loop')
            if issue['type'] == 'nested_loop': failed_concepts.add('nested_loops')
            
        for concept in concepts:
            success = concept not in failed_concepts
            self.update_concept(student_id, concept, success)
