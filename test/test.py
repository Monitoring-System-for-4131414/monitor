import time

class TestMe:
    def __init__(self):
        self.swi = False
    def Te(self):
        while(self.swi == True):
            print(time.asctime( time.localtime(time.time()) )+'\n')
    def On(self):
        self.swi=True
    def Off(self):
        self.swi=False

te = TestMe()