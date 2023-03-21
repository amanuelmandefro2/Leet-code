class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        lst = []
        for num in range(1, n+1):
            if num % 3 == 0 and num % 5 == 0:
                lst.append("FizzBuzz")
            elif num % 3 == 0:
                lst.append("Fizz")
            elif num % 5 == 0:
                lst.append("Buzz")
            else:
                lst.append("{:d}".format(num))
        return lst