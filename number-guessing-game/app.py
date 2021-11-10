import io
import random


def main():
  welcome_text = """
  ------------------------------------------
  |   Welcome to the number gessing game!  |
  |                                        |
  |  I'll think in a number between 0-10.  |
  |                                        |
  |     Type your guess and hit enter!     |
  ------------------------------------------
    """
  print(welcome_text)

  number = 1
  guess = None
  interval_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

  while number != guess:
    number = random.randrange(11)
    try:
      guess = int(input("type some number: "))
      if guess not in interval_list:
        print("This number/text is invalid!")
        continue
    except ValueError:
      print("This is not a integer number. Are you OK? Go drink some water")
      continue
    if number != guess:
      print(f"You typed {guess} and I thought {number}. Wrong answer!")
    print('\n')

  right_text = """
  ------------------------------------------
  |         YOU GOT IT MASTER!             |
  ------------------------------------------
    """
  print(right_text)


if __name__ == '__main__':
  main()
