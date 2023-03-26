class Solution(object):
    def sortSentence(self, s):
        lst_str = s.split(" ")
        new_lst = [' ']*len(lst_str)
        for word in lst_str:
            index = int(word[-1])-1
            new_lst[index] = word[:-1]
        return " ".join(new_lst)
    
        
        