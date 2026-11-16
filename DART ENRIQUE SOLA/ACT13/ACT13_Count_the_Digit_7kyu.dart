/// Cuenta cuántas veces aparece un dígito [d] en los cuadrados de los
/// números desde 0 hasta [n].
/// 
/// Recorre los números en un bucle, eleva cada uno al cuadrado,
/// lo convierte en texto y cuenta cuántas veces coincide el carácter [d].
int nbDig(int n, int d) {
  int count = 0;
  String targetDigit = d.toString();

  for (int i = 0; i <= n; i++) {
    // Calculamos el cuadrado y lo convertimos a String
    int cuadrado = i * i;
    String textoCuadrado = cuadrado.toString();

    // Contamos cuántas veces aparece el dígito en este número
    for (int j = 0; j < textoCuadrado.length; j++) {
      if (textoCuadrado[j] == targetDigit) {
        count++;
      }
    }
  }

  return count;
}

void main() {
  print(nbDig(5750, 0));  // Output: 4700
  print(nbDig(11011, 2)); // Output: 9481
  print(nbDig(12224, 8)); // Output: 7733
  print(nbDig(11549, 1)); // Output: 11905
  print(nbDig(14550, 7)); // Output: 8014
}
