/// Convierte las horas, minutos y segundos a milisegundos totales desde medianoche.
/// 
/// Multiplica las horas por 3,600,000, los minutos por 60,000 y los segundos por 1,000.
int past(int h, int m, int s) {
  int horasEnMs = h * 60 * 60 * 1000;
  int minutosEnMs = m * 60 * 1000;
  int segundosEnMs = s * 1000;

  return horasEnMs + minutosEnMs + segundosEnMs;
}

void main() {
  print(past(0, 1, 1)); // Output: 61000
  print(past(1, 1, 1)); // Output: 3661000
  print(past(0, 0, 0)); // Output: 0
  print(past(1, 0, 1)); // Output: 3601000
  print(past(1, 0, 0)); // Output: 3600000
}
