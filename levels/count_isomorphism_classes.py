from itertools import permutations, combinations

def generate_adjacency_matrices(n):
  """
  Generates all possible adjacency matrices for a graph with n nodes.
  """
  matrix = [[0 for _ in range(n)] for _ in range(n)]
  for edges in combinations(range(n * n), n * (n - 1) // 2):
    for edge in edges:
      i, j = edge // n, edge % n
      matrix[i][j] = matrix[j][i] = 1
    yield matrix

def is_isomorphic(m1, m2):
  """
  Checks if two adjacency matrices represent isomorphic graphs.
  """
  for i in range(len(m1)):
    for j in range(i + 1, len(m1)):
      if m1[i][j] != m2[i][j]:
        return False
  return True

def count_isomorphism_classes(n):
  """
  Counts the number of isomorphism classes for graphs with n nodes.
  """
  matrices = list(generate_adjacency_matrices(n))
  classes = set()
  for m1 in matrices:
    isomorphic = False
    for m2 in matrices:
      if is_isomorphic(m1, m2):
        isomorphic = True
        break
    if not isomorphic:
      classes.add(tuple(tuple(row) for row in m1))
  return len(classes)

# Plot node count vs isomorphism classes count
nodes = range(1, 4)
classes = [count_isomorphism_classes(n) for n in nodes]
import matplotlib.pyplot as plt
plt.plot(nodes, classes)
plt.xlabel("Number of Nodes")
plt.ylabel("Number of Isomorphism Classes")
plt.title("Isomorphism Classes vs. Number of Nodes")
plt.show()

