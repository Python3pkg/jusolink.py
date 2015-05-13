# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it 
import sys
import imp
import random
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

try:
    import unittest2 as unittest
except ImportError:
    import unittest
from jusolink import *

class JusolinkTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.jusolinkService =  Jusolink('TESTER_JUSO','FjaRgAfVUPvSDHTrdd/uw/dt/Cdo3GgSFKyE1+NQ+bc=')
        
    def test_getBalance(self):
        balance = self.jusolinkService.getBalance()
        print(balance)
        self.assertGreaterEqual(balance,0,'잔액 0 이상.')

    def test_getUnitCost(self):
        unitCost = self.jusolinkService.getUnitCost()
        print(unitCost)
        self.assertGreaterEqual(unitCost,0,"단가는 0 이상.")

    def test_search(self):
        result = self.jusolinkService.search("광주광역시 북그 용봉동 1", 1, 20)
        
        tmp = "검색문자열 : " + str(result.searches) + "\n"
        
        if result.deletedWord != None :
            tmp += "[제외단어 목록] \n"
            i = 0
            for i in range(0, len(result.deletedWord)):
                tmp += str(result.deletedWord[i]) + " "

        tmp += "\n"
        tmp += "수정제시어 : " + str(result.suggest) + "\n"
        tmp += "총 검색 결과 수 : " + str(result.numFound) + "\n"
        tmp += "페이지 목록 주소 개수 : " + str(result.listSize) + "\n"
        tmp += "검색된 페이지 번호 : " + str(result.page) + "\n"
        tmp += "과금 여부 : " + str(result.chargeYN) + "\n\n"
        
        if result.juso != None :
            tmp += "[주소정보 리스트] \n"
            i = 0 
            for i in range(0, len(result.juso)):
                tmp += str(result.juso[i].roadAddr1)+ " "
                tmp += str(result.juso[i].roadAddr2)+ " "
                tmp += str(result.juso[i].jibunAddr)+ " "
                tmp += str(result.juso[i].zipcode)+ " "
                tmp += str(result.juso[i].sectionNum)+ " "
                tmp += str(result.juso[i].dongCode)+ " "
                tmp += str(result.juso[i].streetCode)+ " "

                if result.juso[i].detailBuildingName != None:
                    tmp += "\n[상세건물명] "
                    j = 0 
                    for j in range(0, len(result.juso[i].detailBuildingName)):
                        tmp += str(result.juso[i].detailBuildingName[j])+ " "

                if result.juso[i].relatedJibun != None:
                    tmp += "\n[관련지번목록] "
                    j = 0 
                    for j in range(0, len(result.juso[i].relatedJibun)):
                        tmp += str(result.juso[i].relatedJibun[j])+ " "
                

                tmp += "\n\n"
        print(tmp)
if __name__ == '__main__':
    unittest.main()