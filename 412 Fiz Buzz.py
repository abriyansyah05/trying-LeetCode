class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        value = n
        answer = []
        for x in range (1, value+1):
            if x % 3 == 0:
                if x % 5 == 0 :
                    answer.append("FizzBuzz")
                    
                else:
                    answer.append("Fizz")
                
                
            elif x % 5 == 0:
                answer.append("Buzz")
                
            else:
                answer.append(str(x))
                
        return answer