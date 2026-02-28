import random
N = 8
def conflicts(state):
    c = 0
    for i in range(N):
        for j in range(i + 1, N):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                c += 1
    return c
def best_neighbor(state):
    best = state[:]
    best_cost = conflicts(best)
    for col in range(N):
        old_row = state[col]
        for row in range(N):
            if row == old_row:
                continue
            cand = state[:]
            cand[col] = row
            cost = conflicts(cand)
            if cost < best_cost:
                best, best_cost = cand, cost
    return best, best_cost
def hill_climbing(restarts=200):
    best_overall = None
    best_cost = 10**9
    for _ in range(restarts):
        state = [random.randrange(N) for _ in range(N)]
        cost = conflicts(state)
        while True:
            nb, nb_cost = best_neighbor(state)
            if nb_cost >= cost:
                break
            state, cost = nb, nb_cost
            if cost == 0:
                return state, 0
        if cost < best_cost:
            best_overall, best_cost = state, cost
            if best_cost == 0:
                break
    return best_overall, best_cost
def show(state):
    for r in range(N):
        print(" ".join("Q" if state[c] == r else "." for c in range(N)))
if __name__ == "__main__":
    sol, cost = hill_climbing(restarts=500)
    print("state:", sol)
    print("conflicts:", cost)
    show(sol)