/// Multiplica todos los elementos de una lista de enteros entre sí.
/// 
/// Recibe una lista [arr] y recorre cada número multiplicándolo
/// para acumular el resultado total.
int grow(List<int> arr) {
  int resultado = 1;

  for (int numero in arr) {
    resultado *= numero;
  }

  return resultado;
}

void main() {
  print(grow([1, 2, 3]));          // Output: 6
  print(grow([4, 1, 1, 1, 4]));    // Output: 16
  print(grow([2, 2, 2, 2, 2, 2])); // Output: 64
}
