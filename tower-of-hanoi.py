class Rod:
    
    def __init__(self, n_disks=0):
        if n_disks > 0:
            self.disks = [t for t in range(1, n_disks+1)]            
        else:
            self.disks = []
        self.disks.reverse()
        #disks = ex:[6,5,4,3,2,1] 

    def getSmallestDisk(self):
        return self.disks[-1] if len(self.disks) > 0 else None 

    def appendDisk(self, disk):
        self.disks.append(disk)

    def popDisk(self):
        return self.disks.pop()

    def canReceiveDisk(self, disk):
        smallest = self.getSmallestDisk()
        if smallest is None or disk < smallest:
            return True
        return False


class Game:

    def __init__(self, n_disks):
        self.n_disks = n_disks
        self.minimum = 2**n_disks - 1
        self.rods = [Rod(n_disks), Rod(), Rod()]

    def printTab(self):
        print()
        for d in reversed(range(self.n_disks)):
            print("\t{0}\t{1}\t{2}".format(
                "-" if len(self.rods[0].disks)-1 < d else self.rods[0].disks[d],
                "-" if len(self.rods[1].disks)-1 < d else self.rods[1].disks[d],
                "-" if len(self.rods[2].disks)-1 < d else self.rods[2].disks[d]
                ))
        print("\t" + "*"*17 + "\nRods \t1\t2\t3\n")

    def move(self, rod1, rod2):  
        self.rods[rod2].appendDisk(self.rods[rod1].popDisk())

    def hadVictory(self):
        if len(self.rods[1].disks) == self.n_disks or\
           len(self.rods[2].disks) == self.n_disks:
            return True
        return False

def play():
    while True:
        n_disks = input("\nNumber of disks(3 - 8): ")
        if n_disks.isdigit() and 3 <= int(n_disks) <= 8:
            n_disks = int(n_disks)
            break
        print("\nInvalid number of disks.\n")

    game = Game(n_disks)

    moves = 0
        
    while True: 
  
        game.printTab()
        
        while True:
            rod1 = input("Move from rod number: ")
            rod2 = input("To rod number: ")
            if rod1.isdigit() and rod2.isdigit() \
               and 1 <= int(rod1) <= 3 and 1 <= int(rod2) <= 3 \
               and int(rod1) != int(rod2):
                rod1, rod2 = int(rod1), int(rod2)
                rod1 -= 1
                rod2 -= 1
                smallest_disk = game.rods[rod1].getSmallestDisk()
                if smallest_disk:
                    can_receive = game.rods[rod2].canReceiveDisk(smallest_disk)
                    if can_receive:
                        game.move(rod1, rod2)
                        break
            print("\nInvalid move.\n")

        moves += 1

        if game.hadVictory():
            game.printTab()
            if moves == game.minimum:
                print("Congratulations, you win with the "
                      "least possible moves!\n")
            else:
                print("You win with {} moves.\n"
                      "Minimum number of moves possible: {}.\n"
                      "".format(moves, game.minimum))
            break

print("\nWelcome to Tower of Hanoi!")

play()
        
while True:
    again = input("Type anything to play again or type Enter to exit: ")
    if again == "": break
    play()
    
print("\nThank you for playing Tower of Hanoi!\n\t\t\tby Paulo Comasetto")
