import os
import sys
from abc import ABC, abstractmethod

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class CognitiveKernel(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def evaluate_scenario(self, variables: dict) -> dict:
        pass

    @abstractmethod
    def generate_alignment_prompt(self, base_info: str) -> str:
        pass

class WesternLogosKernel(CognitiveKernel):
    def __init__(self):
        super().__init__("Western Analytical (Logos)")

    def evaluate_scenario(self, variables: dict) -> dict:
        individual_rights_protected = variables.get("individual_rights", True)
        rule_compliance = variables.get("formal_contract_compliance", 1.0)
        
        decision = "Rule-Driven Action: "
        if individual_rights_protected and rule_compliance >= 0.8:
            decision += "Protect individual autonomy and enforce contractual obligations strictly."
            metric_score = 0.95
        else:
            decision += "Invoke universal legal/procedural remediation."
            metric_score = 0.40
            
        return {
            "kernel": self.name,
            "decision": decision,
            "metric_type": "Categorical Imperative / Deontological Score",
            "score": metric_score
        }

    def generate_alignment_prompt(self, base_info: str) -> str:
        return f"[System Paradigm: Western Analytical]\nInstruction: Present the following information using rigorous, logical, and modular arguments.\n\nContent:\n{base_info}"

class EasternTaoKernel(CognitiveKernel):
    def __init__(self):
        super().__init__("Eastern Relational (Tao)")

    def evaluate_scenario(self, variables: dict) -> dict:
        context_weight = variables.get("contextual_nuance", 0.9)
        relational_harmony = variables.get("interpersonal_harmony", 0.8)
        
        decision = "Harmony-Driven Action: "
        if context_weight > 0.5 and relational_harmony > 0.6:
            decision += "Dynamically adjust enforcement to preserve systemic cohesion and consensus."
            metric_score = 0.88
        else:
            decision += "Seek intermediate mediation to avoid binary polarization."
            metric_score = 0.50
            
        return {
            "kernel": self.name,
            "decision": decision,
            "metric_type": "Relational Homeostasis / Yin-Yang Balance Score",
            "score": metric_score
        }

    def generate_alignment_prompt(self, base_info: str) -> str:
        return f"[System Paradigm: Eastern Holistic]\nInstruction: Present the following information focusing on the systemic context and interconnected relationships.\n\nContent:\n{base_info}"

class CrossCulturalEvaluator:
    def __init__(self):
        self.western_kernel = WesternLogosKernel()
        self.eastern_kernel = EasternTaoKernel()

    def execute_evaluation(self):
        print("=" * 65)
        print(" LOGOS-TAO ENGINE: CROSS-CULTURAL COGNITION SANDBOX v1.0 ")
        print("=" * 65)
        print("Scenario: A highly talented individual team member insists on pursuing an unauthorized path.")
        print("1: Enforce standard protocols. Rules exist for structural stability.")
        print("2: Convene the team, assess the relational impact, and flexibly adjust constraints.")
        
        choice = input("\nSelect your cognitive path (1 or 2): ").strip()
        raw_info = "The project timeline requires a shift towards a decentralized execution plan."
        
        if choice == "1":
            res = self.western_kernel.evaluate_scenario({"individual_rights": True, "formal_contract_compliance": 0.9})
            print(f"\nDecision: {res['decision']}")
            print(self.western_kernel.generate_alignment_prompt(raw_info))
        elif choice == "2":
            res = self.eastern_kernel.evaluate_scenario({"contextual_nuance": 0.85, "interpersonal_harmony": 0.75})
            print(f"\nDecision: {res['decision']}")
            print(self.eastern_kernel.generate_alignment_prompt(raw_info))

if __name__ == "__main__":
    evaluator = CrossCulturalEvaluator()
    evaluator.execute_evaluation()
