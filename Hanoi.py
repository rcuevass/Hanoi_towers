"""
    This program exemplifies the use of recursion by solving the
    Hanoi towers problem:

    It consists of three rods, and a number of disks of different sizes which can slide onto any rod.
    The puzzle starts with the disks in a neat stack in ascending order of size on one rod,
    the smallest at the top, thus making a conical shape. The objective of the puzzle is to move the
    entire stack to another rod, obeying the following rules:

        1. Only one disk can be moved at a time.
        2. Each move consists of taking the upper disk from one of the stacks and placing it on top
           of another stack i.e. a disk can only be moved if it is the uppermost disk on a stack.
        3. No disk may be placed on top of a smaller disk.

"""

class TowerOfHanoi:
    """
        This class contains the typical initialization function, function
        that moves a disk from one rod to another and a function that moves
        a tower of disks from one rod to another (recursive part)
    """

    def __init__(self, numDisks):
        """
            This function initializes tower with the number of disks given by the user,
            three rods (represented by stacks) and a counter to keep track
            of the number of moves.

            input.- numDisks -- Number of disks set by the user

        """

        self.numDisks = numDisks
        self.towers = ([], [], [])
        self.counter = 0
        for i in range(numDisks, 0, -1):
            self.towers[0].append(i)

    def printStatus(self):
        """
        This function simply prints out to screen the current configuration of the
        three rods
        :return: Prints message to screen
        """
        print self.towers


    def moveDisk(self,src,dest):
        """
        This function moves one disk from one rod (src = source) to another (dest)

        :param src: Index representing the rod where the disk will be moved from
        :param dest: Index representing the rod where the disk will be moved to
        :return: None
        """

        # Remove disk from the source rod...
        disk = self.towers[src].pop()
        # ... add it to the destiny rod...
        self.towers[dest].append(disk)
        # ... and increase counter to account for move just made.
        self.counter += 1
        # Print to screen information regarding the move just made
        print "Step", self.counter, "Move disk", disk, "from tower", src, \
            "to tower", dest, "-->", self.towers

    def moveTower(self, n, src, buffer, dest):
        """
        This function moves a tower of n disks from a rod (src) to another (dest) using a third
        rod (spare) as a buffer. This function is the one that allows recursion.

        :param n: Number of disks in tower to be moved
        :param src: Index representing the source rod
        :param buffer: Index representing the buffer rod
        :param dest: Index representing the final rod
        :return: None
        """

        # If the tower consists of only one disk, then moving the tower
        # is equivalent to moving the only disk available.
        if n == 1:
            self.moveDisk(src, dest)

        # Otherwise...
        else:
            # (recursion!)
            # ...we move the tower that consists of the first n-1 disks from
            # the source rod to the buffer rod using the destiny source as spare.
            self.moveTower(n - 1, src, dest, buffer)
            # Then we move the last disk remaining (n-th disk) in the source rode
            # to the destiny rode (this is the largest disk in the collection and
            # we will pile to rest of the disks on top of it)...
            self.moveDisk(src, dest)
            # (recursion!)
            # ... and finally move the tower of n-1 disks from spare rod to
            # destiny rod using the source rod as a buffer
            self.moveTower(n - 1, buffer, src, dest)


def main(num_Disks):
    """
    This function calls the methods defined in the previous class
    :param num_Disks: Number of disks in the game; user-defined
    :return: Displays progress of game in screen
    """

    # Instantiate the class with the number of disks given
    tH = TowerOfHanoi(num_Disks)
    print "Initial configuration..."
    tH.printStatus()
    print " "
    print "Executing moves..."
    # Here is where the magic actually happens
    tH.moveTower(num_Disks, 0, 1, 2)
    print " "
    print "Final configuration..."
    tH.printStatus()

    # The program is finished
    print "Done!"

if __name__ == '__main__':
    # Execute program with a given number of disks
    main(3)
