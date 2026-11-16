/// Encuentra el número más alto y el más bajo de una cadena de texto
/// con números separados por espacios y los devuelve en formato "máximo mínimo".
/// 
/// Recibe [numbers], lo divide por espacios, convierte cada trozo a entero,
/// calcula el mayor y el menor, y los une en un String.
String highAndLow(String numbers) {
  // Separamos el texto por espacios y convertimos cada elemento a entero
  List<int> listaNumeros = numbers.split(' ').map(int.parse).toList();

  // Encontramos el número máximo y el mínimo
  int max = listaNumeros.reduce((a, b) => a > b ? a : b);
  int min = listaNumeros.reduce((a, b) => a < b ? a : b);

  // Retornamos ambos en un String separados por un espacio
  return '$max $min';
}

void main() {
  print(highAndLow("8 3 -5 42 -1 0 0 -9 4 7 4 -4")); // Output: "42 -9"
  print(highAndLow("1 2 3"));                       // Output: "3 1"
}
