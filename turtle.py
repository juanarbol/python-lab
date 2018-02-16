import turtle

def main():
  window = turtle.Screen()
  dave = turtle.Turtle()
  make_square(dave)

def make_square(tortoise):
  length = int(input('Size of square side: '))

  for i in range(4):
    make_line_and_turn(tortoise, length)

def make_line_and_turn(tortoise, length):
  tortoise.forward(length)
  tortoise.left(90)

if __name__ == '__main__':
  main()