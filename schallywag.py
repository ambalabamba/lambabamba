import random
import requests
import threading
from xml.dom import minidom

class AFunStickArenaExperience:
    def __init__(self, Password, Amount):
        self.Password = Password
        self.MaxAmount = Amount
        self.generateAccounts()
 
    def generateAccounts(self):
        try:
            threading.Timer(0.1, self.generateAccounts).start()
            Start = 0
            Accounts = []
            LowerList = ['a', 'b', 'c', 'c', 'e', 'f', 'h', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            additional = ['a', 'y', 'x', '4', 'p', '3', 'q', 'l', 'k', 'o', 'v']

            while Start < self.MaxAmount:
                Username = ''.join(random.choice(LowerList) for NameLen in range(10)) + ''.join(random.choice(additional) for NameLen in range(3))
                PostData = {"username": Username, "userpass": self.Password, "usercol": "248000000", "action": "create"}
                URLData = requests.post("http://www.xgenstudios.com/stickarena/stick_arena.php", data=PostData).text
 
                if "success" in URLData:
                    Start += 1
                else:
                    print("Couldn't create: '" + Username + "'")
                if Start == self.MaxAmount:
                    print('Successfully made ' + str(self.MaxAmount) + ' accounts.')
                break
 
            return True
        except Exception:
            pass
 
    def startGenerator(self):
        Generated = 0
 
        while Generated < self.MaxAmount:
            print("Generating accounts...")
            Generated += 1
 
            self.generateAccounts()
            if Generated == self.MaxAmount:
                print("Successfully created " + self.MaxAmount + " accounts.")
            break
 
if __name__ == "__main__":
    Password = 'okniggaboy'
    Amount = 1000000000000000
    
    print("started!")
    AFunStickArenaExperience(Password, Amount)
