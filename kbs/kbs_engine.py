import json

class KBSEngine:
    def __init__(self, rules_file="kbs/expert_rules.json"):
        with open(rules_file, "r") as f:
            self.rules = json.load(f)

    def check_hints(self, player_state):
        """
        Return number of hints to give based on player mistakes
        player_state: {'mistakes':int, 'time':float}
        """
        hints = 0
        if player_state.get("mistakes",0) >= self.rules["give_hint_if_stuck"]:
            hints +=1
        return hints

    def adjust_difficulty(self, player_state, current_level):
        """
        Reduce difficulty if player fails too much
        """
        if player_state.get("mistakes",0) >= self.rules["reduce_difficulty_after_failures"]:
            return max(1, current_level-1)
        return current_level
