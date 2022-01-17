from multiprocessing import connection
import unittest
import pymysql
class Test(unittest.TestCase):
    def tearDown(self) -> None:
        return super().tearDown()
    def test_Q1(self):#sum target
        self.assertTrue(set(Solution().Question1([2,7,11,15],9))==set([0,1]))
        self.assertTrue(set(Solution().Question1([3,2,4],6))==set([1,2]))
        self.assertTrue(set(Solution().Question1([3,3],6))==set([0, 1]))
    def test_Q2(self):#roman numeral
        self.assertEqual(Solution().Question2("III"),3)
        self.assertEqual(Solution().Question2("LIV"),54)
        self.assertEqual(Solution().Question2("IX"),9)
        self.assertEqual(Solution().Question2("LVIII"),58)
        

class Solution(object):
    #program Questions
    def Question1(self, nums, target):#sum target
        origNums=nums
        for i,num in enumerate(nums):
            complement = target-num
            if complement in origNums and origNums.index(complement)!=i:
                return[i,origNums.index(complement)]
    
    def Question2(self, s):#roman numeral
        symbol={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}#1,5,10,50,100,500,1000
        roman = []
        numeral = 0
        for i,e in enumerate(s):
            roman.append(symbol[e])
        p=-1
        for e in reversed(range(len(roman))):
            if roman[e]>roman[e-1] and e-1>-1:
                numeral += (roman[e]-roman[e-1])
                p = e-1
            elif p>-1:
                p=-1
                continue
            else:
                numeral += roman[e]
        return numeral

    #SQL Questions
    """
    connection = pymysql.connect("Driver={};Server=<>;Database=<>;Trusted_Connection=yes;")
    def SQuestion1(self, connection):
        cursor = connection.cursor()
        return cursor.excute("SELECT Person.firstName, Person.lastName, ISNULL(Address.city,'Null') AS city, ISNULL(Address.state) AS state FROM Person LEFT JOIN Address ON Person.personId=Address.personId")

    def SQuestion2(self, connection):
        cursor = connection.cursor()
        return cursor.excute("SELECT DISTINCT Customers.name FROM Customers LEFT OUTER JOIN Orders ON Customers.id=Orders.customerId Where Orders.customerId IS NULL")

    def SQuestion3(self, connection):
        cursor = connection.cursor()
        return cursor.excute("SELECT Email, COUNT(Email) From Person GROUP BY Email HAVING COUNT(Email)>1")        
    """
    #HTML Questions
    """
    <!DOCTYPEhtml>
    <html>
        <head>
            <metacharset="UTF-8">
            <style>
            table, th, td {
            border: 1px solid black;
            border-collapse: collapse;
            padding-bottom: 20px;
            padding-right: 40px;
            }
            </style>
        </head>
        <body>
        <h2>Question1</h2>
        <table style="width:100%">
            <tr>
                <th>Header1</th>
                <th>Header2</th> 
                <th>Header3</th>
                <th>Header4</th>
            </tr>
            <tr>
                <td></td>
                <td style="border: 1px white;"></td>
                <td style="border: 1px white;"></td>
                <td style="border: 1px white;"></td>
            </tr>
            <tr>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
        </table>

        <h2>Question2</h2>
        <h4>Unordered list</h4>
        <ul>
            <li>first item</li>
            <li>second item</li>
            <li>third item</li>
        </ul>
            
        <h4>Ordered lists</h4>
        <ol>
            <li>WIN1</li>
            <li>WIN2</li>
            <li>WIN3</li>
        </ol>

        <h4>Definition lists</h4>
        <dl>
            <dt>WIN1</dt>
            <dd>WIN1-1</dd>
            <dt>WIN2</dt>
            <dt>WIN3</dt>
            <dd>WIN3-1</dd>
        </dl>

        <h4>Nested lists</h4>
        <ol>
            <li>WIN1 item 1</li>
            <li>WIN2 item 2</li>
            <ul style="list-style-type:circle;">
                <li>WIN item 2-1</li>
                <li>WIN item 2-2</li>
            </ul>
            <li>WIN3 item 3</li>
        </ol>
        </body>
    </html>
    """



if __name__=='__main__':
    unittest.main()