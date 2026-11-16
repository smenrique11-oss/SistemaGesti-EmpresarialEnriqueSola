/// Beginner Series #2 Clock (8 kyu)
/// 
/// Convierte las horas, minutos y segundos a milisegundos totales desde medianoche.
int past(int h, int m, int s) {
  // Good Luck!
  return (h * 3600 + m * 60 + s) * 1000;
}

void main() {
  print(past(0, 1, 1)); // Output: 61000
  print(past(1, 1, 1)); // Output: 3661000
  print(past(0, 0, 0)); // Output: 0
  print(past(1, 0, 1)); // Output: 3601000
  print(past(1, 0, 0)); // Output: 3600000
}
