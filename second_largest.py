# Given the participants(' score sheet for your University Sports Day, you are required to find the runner-up score. '
# 'You are given n scores. Store them in a list and find the score of the runner-up.)
#
# Input Format
#
# The first line contains n .
# The second line contains an array A[]  of n integers each separated by a space.
#
# Constraints
#
# 2<=n<=10
# -100<=A[i]<=100
#
# output format
# Print the runner-up score
#
#


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    unique_scores = set(arr)
    runner_up = sorted(unique_scores, reverse=True)[1]
print(runner_up)
