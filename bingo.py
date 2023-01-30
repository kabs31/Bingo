import random

class Bingo:
    def __init__(self):
        self.grid = self._generate_grid()
        self.called_numbers = []

    def _generate_grid(self):
        # generate a 5x5 grid of random numbers
        return [[random.randint(1, 15) for _ in range(5)] for _ in range(5)]

    def play(self):
        while len(self.called_numbers) < 25:
            self._print_grid()
            try:
                num = int(input("Enter a number: "))
            except ValueError:
                print("Invalid input, try again.")
                continue
            if num in self.called_numbers:
                print("Number already called, try again.")
                continue
            self.called_numbers.append(num)
            if self._check_bingo():
                self._print_grid()
                print("BINGO!!!")
                break
        else:
            print("All numbers called, no bingo.")

    def _print_grid(self):
        print("\nB   I   N   G   O\n")
        for i in range(5):
            for j in range(5):
                if self.grid[i][j] in self.called_numbers:
                    print(f"{self.grid[i][j]:2}*", end=" | ")
                else:
                    print(f"{self.grid[i][j]:2} ", end=" | ")
            print("\n" + "-"*21)

    def _check_bingo(self):
        # check for a bingo by checking all possible winning combinations
        for row in self.grid:
            if all(num in self.called_numbers for num in row):
                return True
        for col in range(5):
            if all(self.grid[row][col] in self.called_numbers for row in range(5)):
                return True
        if all(self.grid[i][i] in self.called_numbers for i in range(5)):
            return True
        if all(self.grid[i][4-i] in self.called_numbers for i in range(5)):
            return True
        return False

if __name__ == "__main__":
    game = Bingo()
    game.play()
