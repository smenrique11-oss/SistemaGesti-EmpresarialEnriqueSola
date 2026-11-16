/// Suma todos los números enteros encontrados dentro de una cadena de texto.
/// 
/// Utiliza una expresión regular para extraer todos los bloques numéricos,
/// los convierte a enteros y los acumula en una suma total.
int sumOfIntegersInString(String s) {
  // Buscamos todas las secuencias de dígitos en el texto
  RegExp regExp = RegExp(r'\d+');
  Iterable<Match> matches = regExp.allMatches(s);

  int total = 0;

  for (Match match in matches) {
    // Extraemos el número encontrado como texto y lo sumamos convertido a int
    total += int.parse(match.group(0)!);
  }

  return total;
}

void main() {
  print(sumOfIntegersInString('12.4'));                                                      // Output: 16
  print(sumOfIntegersInString('h3ll0w0rld'));                                                // Output: 3
  print(sumOfIntegersInString('2 + 3 = '));                                                 // Output: 5
  print(sumOfIntegersInString('Our company made approximately 1 million in gross revenue')); // Output: 1
}
