def player(prev_play, opponent_history=[], sequences={}):
  stride = 3

  if prev_play != '':
    opponent_history.append(prev_play)

  if len(opponent_history) <= stride:
    return "R"

  if len(opponent_history) > stride + 1:
    opponent_history.pop(0)

  seq = "".join(opponent_history)
  sequences[seq] = sequences.get(seq, 0) + 1

  seq     = "".join(opponent_history[-stride:])
  predict = max([seq+"R", seq+"P", seq+"S"],
                  key=lambda key: sequences.get(key,0))[-1]

  if predict == "R": return "P"
  if predict == "P": return "S"
  return "R"
