def main():
  print('CALCULADORA DE DIVISAS\n')

  amount = float(input('Ingrese la cantidad de pesos que quieres convertir $'))
  dollar_price = float(input('Ingrese el valor del dolar $'))

  total_dollars = exchange(amount, dollar_price)
  print("%f COP son %f USD $" %(amount, total_dollars))

def exchange(amount, currency):
  return amount / currency


if __name__ == '__main__':
  main()
