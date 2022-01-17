from multiprocessing import connection
import unittest
import pyodbc
class Test(unittest.TestCase):
    def test_Q1(self):#sum target
        self.assertListEqual(Solution().Question1([3,2,4],6),[1,2])
    # def test_Q2(self):#roman numeral
        # ff



class Solution(object):
    #program Q
    def Question1(self, nums, target):#sum target
        origNums=nums
        for i,num in enumerate(nums):
            complement = target-num
            if complement in origNums and origNums.index(complement)!=i:
                return[i,origNums.index(complement)]
    
    # def Question2():#roman numeral
        # symbol=["I","V","X","L","C","D","M"]#1,5,10,50,100,500,1000
        #I->V,X; X->L,C; C->D,M
        #1. check M->D->C,...->I, if 
    
    #SQL Q
    connection = pyodbc.connect("Driver={};Server=<>;Database=<>;Trusted_Connection=yes;")
    def SQuestion1(self, connection):
        cursor = connection.cursor()
        cursor.excute("")



if __name__=='__main__':
    unittest.main()