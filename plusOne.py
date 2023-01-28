from typing import List

class Solution:
    def plusOne(digits: List[int]) -> List[int]:

        new = str(digits)
        new2 = new.replace(',','')
        new3 = new2.replace(' ','')
        new4 = new3.replace(']','')
        new5 = new4.replace('[','')
        new6 = int(new5)
        new7 = new6+1
        new8 = str(new7)
        new9 = [int(i) for i in new8]

        return(new9)

digits = [1,2,3,8]
Solution.plusOne(digits)