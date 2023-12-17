from typing import List

class ATM:

    def __init__(self):
        self.notes_order = [20, 50, 100, 200, 500]
        self.notes_amount = [0] * 5

    def deposit(self, banknotesCount: List[int]) -> None:
        for i, amount in enumerate(banknotesCount):
            self.notes_amount[i] += amount

    def withdraw(self, amount: int) -> List[int]:
        note_idx = 4
        ans = [0] * 5

        while amount > 0 and note_idx >= 0:
            ans[note_idx] = min(self.notes_amount[note_idx], amount // self.notes_order[note_idx])
            amount -= ans[note_idx] * self.notes_order[note_idx]
            note_idx -= 1

        if amount > 0:
            return [-1]
        else:
            for i in range(len(self.notes_amount)):
                self.notes_amount[i] -= ans[i]
            return ans

# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)
