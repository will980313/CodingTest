def solution(numbers):
    return sorted(list(set([n_i+n_j for i, n_i in enumerate(numbers) for j, n_j in enumerate(numbers) if i != j ])))