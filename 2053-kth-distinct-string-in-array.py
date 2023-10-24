class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        str_dict = {}
        dist_arr = []
        for i in range(len(arr)):
            str_dict[arr[i]] = str_dict.get(arr[i], 0) + 1
        for c in str_dict:
            if str_dict[c] == 1:
                dist_arr.append(c)
        if len(dist_arr ) < k:
            return ""
        return dist_arr[k - 1]
