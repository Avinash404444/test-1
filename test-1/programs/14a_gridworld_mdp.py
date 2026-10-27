grid = 4
state = [0, 0]
goal = [3, 3]
path = [state.copy()]
reward = 0
moves = [(1, 0), (1, 0), (1, 0), (0, 1), (0, 1), (0, 1)]
for row_step, col_step in moves:
    state[0] += row_step
    state[1] += col_step
    reward -= 1
    path.append(state.copy())
if state == goal:
    reward += 10
print("Path:", path)
print("Total Reward:", reward)
print("Goal Reached:", state == goal)
