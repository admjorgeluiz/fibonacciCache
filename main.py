fib_cache = {}

def fibonacciCache(n):
  if n in fib_cache:
    return fib_cache[n]
  if n<= 1:
    resultado = n
  else:
    resultado = fibonacciCache(n-1) + fibonacciCache(n-2)

  fib_cache[n] = resultado
  return resultado

consulta_fib = int(input("Insira um número: "))
print(fibonacciCache(consulta_fib))