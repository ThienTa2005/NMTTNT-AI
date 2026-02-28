import random
import math
N = 8
def conflicts(state):
    c = 0
    for i in range(N):
        for j in range(i + 1, N):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                c += 1
    return c
def random_neighbor(state):
    col = random.randrange(N)
    row = random.randrange(N)
    while row == state[col]:
        row = random.randrange(N)
    nb = state[:]
    nb[col] = row
    return nb
def simulated_annealing(T0=5.0, alpha=0.995, steps=200000):
    state = [random.randrange(N) for _ in range(N)]
    cost = conflicts(state)
    best_state, best_cost = state[:], cost
    T = T0
    for _ in range(steps):
        if cost == 0:
            return state, 0
        nb = random_neighbor(state)
        nb_cost = conflicts(nb)
        d = nb_cost - cost
        if d <= 0 or random.random() < math.exp(-d / max(T, 1e-12)):
            state, cost = nb, nb_cost
            if cost < best_cost:
                best_state, best_cost = state[:], cost
        T *= alpha
        if T < 1e-8:
            break
    return best_state, best_cost
def show(state):
    for r in range(N):
        print(" ".join("Q" if state[c] == r else "." for c in range(N)))
if __name__ == "__main__":
    sol, cost = simulated_annealing(T0=10.0, alpha=0.999, steps=300000)
    print("state:", sol)
    print("conflicts:", cost)
    show(sol)