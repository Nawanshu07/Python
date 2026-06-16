import random

class Train:
    def book(self , start , stop):
        self.start = start
        self.stop = stop
        PNR = random.randint(100000000, 999999999) 
        self.pnr = PNR
        
        return PNR

    def check(self , pnr):
        if (pnr == self.pnr):
            print(f"Start:{self.start} \nStop:{self.stop} \nTiming status: On time")
        else:
            print("Enter a valid PNR number")

    def fare(self , pnr):
        if (pnr == self.pnr):
            print("The fare of this train is", random.randint(20,50))
        else:
            print("Enter a valid PNR number")        

tkt = Train()
PNR = tkt.book("Alwar" , "delhi")
tkt.check(PNR)
tkt.fare(PNR)