/// Calcula el peso final de las patatas después de perder agua en el horno.
/// 
/// Recibe el porcentaje inicial de agua ([p0]), el peso inicial ([w0])
/// y el porcentaje final de agua ([p1]). Calcula la materia seca constante
/// y retorna el peso total resultante truncado a entero.
import 'dart:math';

int potatoes(int p0, int w0, int p1) {
  // Calculamos la materia seca que no cambia (peso inicial por el porcentaje de sólidos)
  double dryMatter = w0 * (100 - p0) / 100;

  // Calculamos el peso final dividiendo la materia seca entre el porcentaje de sólidos final
  double finalWeight = dryMatter / ((100 - p1) / 100);

  // Truncamos el resultado a entero
  return finalWeight.floor();
}

void main() {
  print(potatoes(82, 127, 80)); // Output: 114
  print(potatoes(93, 129, 91)); // Output: 100
  print(potatoes(82, 134, 77)); // Output: 104
}
