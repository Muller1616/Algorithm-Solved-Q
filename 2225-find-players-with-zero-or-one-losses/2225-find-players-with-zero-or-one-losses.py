class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loss_count = {}
        for match in matches:
            winner = match[0]
            loser = match[1]
            if winner not in loss_count:
                loss_count[winner] = 0
            if loser not in loss_count:
                loss_count[loser] = 0
            loss_count[loser] += 1
        no_losses = []
        one_loss = []
        for player in loss_count:
            if loss_count[player] == 0:
                no_losses.append(player)
            elif loss_count[player] == 1:
                one_loss.append(player)
        no_losses.sort()
        one_loss.sort()
        return [no_losses, one_loss]
        