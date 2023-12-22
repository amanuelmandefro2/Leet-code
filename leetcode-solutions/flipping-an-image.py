class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for img in image:
            l, r = 0, len(img) - 1
            while l < r:
                img[l], img[r] = img[r], img[l]
                l+= 1
                r -= 1
       
        for img in image:
            for i in range(len(img)):
                if img[i] == 1:
                    img[i] = 0
                else:
                    img[i]=1        
        return image        
        