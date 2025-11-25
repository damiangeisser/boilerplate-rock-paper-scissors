def player(prev_play, opponent_history=[], pattern_counts={}):
    
    if not prev_play:
        prev_play = "R"

    opponent_history.append(prev_play)

    prediction = "P"

    if len(opponent_history) > 4:
 
        last_five = "".join(opponent_history[-5:])
        pattern_counts[last_five] = pattern_counts.get(last_five, 0) + 1

        last_four = opponent_history[-4:]
        potential_sequences = [
            "".join(last_four + [m]) for m in ["R", "P", "S"]
        ]

        sub_counts = {
            seq: pattern_counts[seq]
            for seq in potential_sequences
            if seq in pattern_counts
        }

        if sub_counts:
            best_seq = max(sub_counts, key=sub_counts.get)
            prediction = best_seq[-1]

    beats = {"R": "P", "P": "S", "S": "R"}
    return beats[prediction]
