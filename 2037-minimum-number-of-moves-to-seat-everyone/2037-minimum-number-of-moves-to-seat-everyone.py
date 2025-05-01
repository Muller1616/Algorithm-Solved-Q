class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        new = []
        summ = 0
        for  i in range(len(students)):
            d = abs(students[i] - seats[i])
            new.append(d)
        for  i in range(len(new)):
            summ += new[i]
        return summ
        