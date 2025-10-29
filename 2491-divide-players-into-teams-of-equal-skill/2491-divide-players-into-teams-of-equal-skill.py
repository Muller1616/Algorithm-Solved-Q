class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        total_skill = skill[0] + skill[-1]
        i, j = 0, n - 1
        result = 0

        while i < j:
            if skill[i] + skill[j] != total_skill:
                return -1
            result += skill[i] * skill[j]
            i += 1
            j -= 1

        return result
