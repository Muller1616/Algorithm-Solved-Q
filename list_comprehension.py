# Question: List Comprehensions in Python
# You are given three integers x, y, and z representing the dimensions of a cuboid, along with an integer n.
# You need to generate a list of all possible coordinates [i,j,k]
#
# where:  0≤i≤x
#         0≤j≤y
#         0≤k≤z
# The sum 𝑖+𝑗+𝑘≠𝑛
#
# Input Format
# Four integers: x, y, z, and n (each on a separate line).
#
#
# Output Format
# Print a list of lists containing valid coordinates, sorted in lexicographic order.

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    result = [[i, j, k] for i in range(x + 1)
                  for j in range(y + 1)
                  for k in range(z + 1)
                  if i + j + k != n]

print(result)
