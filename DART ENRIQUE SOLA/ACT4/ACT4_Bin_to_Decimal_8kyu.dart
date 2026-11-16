/// Convierte un número binario en formato de texto (String) a un número entero decimal (int).
/// 
/// Recibe [bin] como una cadena de ceros y unos y utiliza `int.parse` con
/// `radix: 2` para interpretarlo correctamente como binario.
int binToDec(String bin) {
  return int.parse(bin, radix: 2);
}

void main() {
  print(binToDec("1011")); // Output: 11
  print(binToDec("10"));   // Output: 2
}
