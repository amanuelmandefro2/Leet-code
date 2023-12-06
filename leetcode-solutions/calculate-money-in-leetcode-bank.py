class Solution:
    def totalMoney(self, n: int) -> int:
        save = 0
        other_save = 0
        monday_save = 0

        for i in range(n):
            if i % 7 == 0:
                monday_save += 1
                other_save = monday_save
            else:
                other_save += 1
            save += other_save

        return save        
        