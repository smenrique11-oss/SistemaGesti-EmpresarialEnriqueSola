/// Convierte un número entero en su representación en formato de texto (String).
/// 
/// Recibe un número [n] y utiliza el método nativo de Dart para transformarlo.
String numberToString(int n) {
  return n.toString();
}

void main() {
  print(numberToString(123));  // Output: "123"
  print(numberToString(-100)); // Output: "-100"
}
