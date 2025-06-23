import itertools
import random


class Minesweeper():
    """
    Minesweeper game representation
    """

    def __init__(self, height=8, width=8, mines=8):

        # Set initial width, height, and number of mines
        self.height = height
        self.width = width
        self.mines = set()

        # Initialize an empty field with no mines
        self.board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(False)
            self.board.append(row)

        # Add mines randomly
        while len(self.mines) != mines:
            i = random.randrange(height)
            j = random.randrange(width)
            if not self.board[i][j]:
                self.mines.add((i, j))
                self.board[i][j] = True

        # At first, player has found no mines
        self.mines_found = set()

    def print(self):
        """
        Prints a text-based representation
        of where mines are located.
        """
        for i in range(self.height):
            print("--" * self.width + "-")
            for j in range(self.width):
                if self.board[i][j]:
                    print("|X", end="")
                else:
                    print("| ", end="")
            print("|")
        print("--" * self.width + "-")

    def is_mine(self, cell):
        i, j = cell
        return self.board[i][j]

    def nearby_mines(self, cell):
        """
        Returns the number of mines that are
        within one row and column of a given cell,
        not including the cell itself.
        """

        # Keep count of nearby mines
        count = 0

        # Loop over all cells within one row and column
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself
                if (i, j) == cell:
                    continue

                # Update count if cell in bounds and is mine
                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.board[i][j]:
                        count += 1

        return count

    def won(self):
        """
        Checks if all mines have been flagged.
        """
        return self.mines_found == self.mines


class Sentence():
    """
    Logical statement about a Minesweeper game
    A sentence consists of a set of board cells,
    and a count of the number of those cells which are mines.
    """

    def __init__(self, cells, count):
        self.cells = set(cells)
        self.count = count

    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count

    def __str__(self):
        return f"{self.cells} = {self.count}"

    def known_mines(self)->set:
        """
        Returns the set of all cells in self.cells known to be mines.
        """
        if len(self.cells) == self.count:
            return self.cells
        else:
            return set()
        
    def known_safes(self):
        """
        Returns the set of all cells in self.cells known to be safe.
        """
        if self.count == 0:
            return self.cells
        else:
            return set()

    def mark_mine(self, cell):
        """
        Updates internal KB representation given the fact that
        a cell is known to be a mine.
        """
        self.cells.remove(cell)
        self.count -= 1

    def mark_safe(self, cell):
        """
        Updates internal KB representation given the fact that
        a cell is known to be safe.
        """
        self.cells.remove(cell)


class MinesweeperAI():
    """
    Minesweeper game player
    """

    def __init__(self, height=8, width=8):

        # Set initial height and width
        self.height = height
        self.width = width

        # Keep track of which cells have been clicked on
        self.moves_made = set()

        # Keep track of cells known to be safe or mines
        self.mines = set()
        self.safes = set()

        # List of sentences about the game known to be true
        self.KB = []

    def mark_mine(self, cell):
        """
        Marks a cell as a mine, and updates all KB
        to mark that cell as a mine as well.
        """
        self.mines.add(cell)
        for sentence in self.KB:
            if cell in sentence.cells:
                print("A mine was found in a sntnc")
                sentence.mark_mine(cell)

    def mark_safe(self, cell):
        """
        Marks a cell as safe, and updates all KB
        to mark that cell as safe as well.
        """
        self.safes.add(cell)
        for sentence in self.KB:
            if cell in sentence.cells:
                print("A safe was found in a sntnc")
                sentence.mark_safe(cell)

    def add_knowledge(self, cell, count):
        """
        Called when the Minesweeper board tells us, for a given
        safe cell, how many neighboring cells have mines in them.

        This function should:
            1) mark the cell as a move that has been made
            2) mark the cell as safe
            3) add a new sentence to the AI's KB base
               based on the value of `cell` and `count`
            4) mark any additional cells as safe or as mines
               if it can be concluded based on the AI's KB base
            5) add any new sentences to the AI's KB base
               if they can be inferred from existing KB
        """
        self.moves_made.add(cell)
        self.mark_safe(cell)
        
        NeighbouringCells = []
        #Assuming cords(0,0) are top left
        # Adding coords while ensuring they are not outside the board

        if cell[0]+1 < self.width:
            NeighbouringCells.append((cell[0]+1,cell[1]))
            if cell[1]+1 < self.height:
                NeighbouringCells.append((cell[0]+1,cell[1]+1))
            if cell[1]-1 > -1:
                NeighbouringCells.append((cell[0]+1,cell[1]-1))
        if cell[1]+1 < self.height:
            NeighbouringCells.append((cell[0],cell[1]+1))
        if cell[0]-1 > -1:
            NeighbouringCells.append((cell[0]-1,cell[1]))
            if cell[1]-1 > -1:
                NeighbouringCells.append((cell[0]-1,cell[1]-1))
            if cell[1]+1 < self.height:
                NeighbouringCells.append((cell[0]-1,cell[1]+1))
        if cell[1]-1 > -1:
            NeighbouringCells.append((cell[0],cell[1]-1))

        CellsToRemove = []
        for i in NeighbouringCells:
            if i in self.safes or i in self.mines:
                CellsToRemove.append(i)
        for i in CellsToRemove:
            NeighbouringCells.remove(i)
        del CellsToRemove

        NewSntc = Sentence(NeighbouringCells,count)
        #del NeighbouringCells
        self.KB.append(NewSntc)
        print("New sntnc made!")
        Change = True
        ITR = 0
        while Change and ITR <= 800:
            Change = False
            for i in self.KB:
                if i.known_mines() != set():
                    ToMarkMine = i.known_mines().copy()
                    for x in ToMarkMine:
                        if x not in self.mines:
                            self.mark_mine(x)
                            Change = True
                            ITR+=1
                if i.known_safes() != set():
                    ToMarkSafe = i.known_safes().copy()
                    for x in ToMarkSafe:
                        if x not in self.safes:
                            self.mark_safe(x)
                            Change = True
                            ITR+=1
            #Sub-set infrence, may want to later remove it from the while loop and see if there are any performance benefits
            for i in self.KB:
                for j in self.KB:
                    if i == j or i.cells == j.cells:
                        continue
                    elif j.cells.issubset(i.cells):
                        SubSetExtras = i.cells - j.cells
                        ExtrasCount = i.count - j.count
                        if len(SubSetExtras) == 0:
                            continue
                        else:
                            NSntnc = Sentence(SubSetExtras, ExtrasCount)
                            if NSntnc not in self.KB and len(NSntnc.cells) > 0:
                                self.KB.append(NSntnc)
                                Change = True
                                ITR += 1
                    elif i.cells.issubset(j.cells):
                        SubSetExtras = j.cells - i.cells
                        ExtrasCount = j.count - i.count
                        if len(SubSetExtras) == 0:
                            continue
                        else:
                            NSntnc = Sentence(SubSetExtras, ExtrasCount)
                            if NSntnc not in self.KB and len(NSntnc.cells) > 0:
                                self.KB.append(NSntnc)
                                Change = True
                                ITR += 1
            self.KB = [s for s in self.KB if len(s.cells) > 0]
            unique_KB = []
            for sentence in self.KB:
                if sentence not in unique_KB:
                    unique_KB.append(sentence)
            self.KB = unique_KB
        if ITR >= 800:
            print("Debug: The while loop has been iterated over 800 times!")

    def make_safe_move(self):
        """
        Returns a safe cell to choose on the Minesweeper board.
        The move must be known to be safe, and not already a move
        that has been made.

        This function may use the KB in self.mines, self.safes
        and self.moves_made, but should not modify any of those values.
        """
        """Returns a truly safe cell or None"""
        available = self.safes - self.moves_made - self.mines
        if not available:
            print("DEBUG: No verified safe moves available")
            return None
        move = available.pop()
        print(f"DEBUG: Verified safe move available: {move}")
        return move

    def make_random_move(self):
        """
        Returns a move to make on the Minesweeper board.
        Should choose randomly among cells that:
            1) have not already been chosen, and
            2) are not known to be mines
        """
        possible_moves = [
        (i, j)
        for i in range(self.height)
        for j in range(self.width)
        if (i, j) not in self.moves_made
        and (i, j) not in self.mines
        ]
        return random.choice(possible_moves) if possible_moves else None

