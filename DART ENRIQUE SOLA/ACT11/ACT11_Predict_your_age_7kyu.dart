/// Predice la edad a la que se va a vivir basándose en las edades de los 8 bisabuelos.
/// 
/// Recibe 8 edades como parámetros, las eleva al cuadrado, las suma,
/// calcula la raíz cuadrada del total, divide entre dos y redondea hacia abajo.
import 'dart:math';

int predictAge(int age1, int age2, int age3, int age4, int age5, int age6, int age7, int age8) {
  // Guardamos las edades en una lista para recorrerlas fácilmente
  List<int> edades = [age1, age2, age3, age4, age5, age6, age7, age8];

  double sumaCuadrados = 0;

  for (int edad in edades) {
    sumaCuadrados += edad * edad;
  }

  // Raíz cuadrada de la suma
  double raiz = sqrt(sumaCuadrados);

  // Dividir entre dos y redondear hacia abajo
  return (raiz / 2).floor();
}

void main() {
  print(predictAge(65, 60, 75, 55, 60, 63, 64, 45)); // Output: 86
  print(predictAge(32, 54, 76, 65, 34, 63, 64, 45)); // Output: 79
}
