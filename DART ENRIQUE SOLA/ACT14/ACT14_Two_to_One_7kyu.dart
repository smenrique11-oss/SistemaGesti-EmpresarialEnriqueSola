/// Une dos cadenas de texto, elimina las letras duplicadas y las ordena alfabéticamente.
/// 
/// Recibe [a] y [b], las divide en caracteres individuales, las pasa a un Set
/// para quitar duplicados, las ordena y las vuelve a unir en un String.
String longest(String a, String b) {
  // Juntamos los strings, los separamos por cada letra y los metemos en un Set
  var letrasUnicas = (a + b).split('').toSet().toList();

  // Ordenamos alfabéticamente
  letrasUnicas.sort();

  // Unimos todo en un solo String
  return letrasUnicas.join('');
}

void main() {
  print(longest("aretheyhere", "yestheyarehere")); // Output: "aehrsty"
  print(longest("loopingisfunbutdangerous", "lessdangerousthancoding")); // Output: "abcdefghilnoprstu"
}
