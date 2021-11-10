import random
import keyboard


def main():
  key = None
  i = 1  # iterations
  f = [0, 0, 0, 0, 0, 0]  # frequency
  s = 6  # dice sides
  while key != 'q':
    key = input("Type'q' to exit, or 'enter' to roll the dice.\n")
    number = random.randint(1, 6)
    f[number-1] = f[number-1]+1
    print(f"""
          Number: {number}
          Math chances: {(1/s):.4f}%
          Times rolled: {i}
          1: {c_p(f[0], i)} 4: {c_p(f[3], i)}
          2: {c_p(f[1], i)} 5: {c_p(f[4], i)}
          3: {c_p(f[2], i)} 6: {c_p(f[5], i)}
          """)
    i = i + 1
  return


def c_p(number, iterations):  # calc percentage and fix zero division
  if number == 0:
    return '0%'
  else:
    return f'{(number*100/iterations):.4f}%'


if __name__ == '__main__':

  main()
