def predict_player_skill(features):
    mistakes=features.get("mistakes",0)
    time_taken=features.get("time_taken",0)
    if mistakes>5 or time_taken>60:
        return "easy"
    elif mistakes<=2 and time_taken<30:
        return "hard"
    else:
        return "medium"
