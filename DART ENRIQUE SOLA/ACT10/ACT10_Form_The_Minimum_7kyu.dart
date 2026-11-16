/// Forma el número entero más pequeño posible a partir de una lista de dígitos.
/// 
/// Elimina los números duplicados convirtiéndolos a un Set, los ordena de
/// menor a mayor y los une para transformarlos de nuevo en un número entero.
int minValue(List<int> arr) {
  // Convertimos a Set para eliminar duplicados, pasamos a lista y ordenamos
  List<int> unicosOrdenados = arr.toSet().toList()..sort();

  // Unimos los números en un String y los parseamos a entero
  String resultado = unicosOrdenados.join('');

  return int.parse(resultado);
}

void main() {
  print(minValue([1, 3, 1]));       // Output: 13
  print(minValue([4, 7, 5, 7]));    // Output: 457
  print(minValue([4, 8, 1, 4]));    // Output: 148
  print(minValue([5, 7, 9, 5, 7])); // Output: 579
}
