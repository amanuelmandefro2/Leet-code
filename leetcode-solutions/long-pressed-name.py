class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        ptr1 = 0
        ptr2 = 0

        while ptr2 < len(typed):
            if ptr1 < len(name) and name[ptr1] == typed[ptr2]:
                ptr1 += 1
                ptr2 += 1
            elif ptr2 > 0 and typed[ptr2] == typed[ptr2 - 1]:
                ptr2 += 1
            else:
                return False

        return ptr1 == len(name)
