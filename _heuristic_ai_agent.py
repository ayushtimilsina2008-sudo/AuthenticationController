class HeuristicIntelligentAgent:
    def __init__(self):
        # Conceptual intent matrix routing human expressions to technical zones
        self.semantic_knowledge_base = {
            "mathematics": ["matrix", "calculus", "equation", "algebra", "vectors", "geometry"],
            "computer_science": ["script", "python", "database", "sql", "algorithm", "array", "loop"],
            "chemistry": ["atomic", "molecule", "kinetic", "reaction", "acid", "element"]
        }

    def evaluate_semantic_intent(self, user_expression):
        tokenized_words = user_expression.lower().split()
        intent_intersection_scores = {intent_key: 0 for intent_key in self.semantic_knowledge_base}

        for token in tokenized_words:
            normalized_token = token.strip(".,!?\"';:")
            for intent_key, keyword_array in self.semantic_knowledge_base.items():
                if normalized_token in keyword_array:
                    intent_intersection_scores[intent_key] += 1

        target_classified_intent = max(intent_intersection_scores, key=intent_intersection_scores.get)
        if intent_intersection_scores[target_classified_intent] == 0:
            return "generalized_system_focus"
            
        return target_classified_intent

    def formulate_system_recommendation(self, user_expression):
        detected_domain = self.evaluate_semantic_intent(user_expression)
        
        actionable_insights = {
            "mathematics": "Operational Directive: Prioritize spatial vector matrix transformations. Fundamental for kinematic movement calculations.",
            "computer_science": "Operational Directive: Focus on runtime complexity analysis and database index mapping optimizations.",
            "chemistry": "Operational Directive: Analyze molecular weight calculations and electrochemical equilibrium metrics.",
            "generalized_system_focus": "Operational Directive: Execute standard execution balancing across all technical preparation models."
        }
        
        return detected_domain.upper(), actionable_insights[detected_domain]

# =====================================================================
# RUNTIME INTERACTIVE DRIVER
# =====================================================================
if __name__ == "__main__":
    ai_agent = HeuristicIntelligentAgent()
    print("=" * 65)
    print("            NATURAL LANGUAGE INFERENCE AI STUDY AGENT           ")
    print("=" * 65)
    
    print("\nAsk the AI assistant an educational question or outline a problem:")
    user_input_message = input("User Question > ")
    
    domain, feedback = ai_agent.formulate_system_recommendation(user_input_message)

    print("\n" + "=" * 65)
    print(" DYNAMIC HEURISTIC INTENT CLASSIFICATION LOGS")
    print("=" * 65)
    print(f" [USER STREAM MESSAGE]: '{user_input_message}'")
    print(f" [AI INTENT CATEGORY] : {domain}")
    print(f" [AGENT RECOMMENDATION]: {feedback}")
    print("=" * 65)
