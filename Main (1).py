def factorial(n):
  """Calculates the factorial of a given number.

  Args:
    n: The number to calculate the factorial of.

  Returns:
    The factorial of n.
  """
  if n < 0:
    raise ValueError("n must be a non-negative integer.")
  elif n == 0:
    return 1
  else:
    return n * factorial(n - 1)