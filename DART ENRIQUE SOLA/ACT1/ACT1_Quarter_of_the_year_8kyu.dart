/// Calcula a qué trimestre del año (del 1 al 4) pertenece un mes determinado.
/// 
/// Recibe [month] como un número entero entre 1 y 12 y aplica una fórmula
/// matemática de división entera para agrupar los meses en bloques de 3.
/// 
/// Lanza un [ArgumentError] si el mes está fuera del rango válido (1-12).
int quarter(int month) {
  if (month < 1 || month > 12) {
    throw ArgumentError('El mes debe estar entre 1 y 12');
  }
  return ((month - 1) ~/ 3) + 1;
}

void main() {
  print(quarter(3));  // Output: 1
  print(quarter(8));  // Output: 3
  print(quarter(11)); // Output: 4
}
