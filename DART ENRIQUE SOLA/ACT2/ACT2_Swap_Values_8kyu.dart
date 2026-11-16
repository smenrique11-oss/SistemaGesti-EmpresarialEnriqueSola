/// Intercambia los dos elementos de una lista dada por referencia.
/// 
/// Recibe una lista [arr] y utiliza una variable temporal para evitar
/// perder el valor original al sobrescribir la primera posición.
void swapValues(List arr) {
  // Guardamos temporalmente el primer valor antes de perderlo
  var temp = arr[0];

  // Pasamos el segundo valor al primero
  arr[0] = arr[1];

  // Pasamos el valor guardado en el temporal al segundo
  arr[1] = temp;
}

void main() {
  var miLista = [1, 2];
  print('Antes: $miLista'); // [1, 2]

  swapValues(miLista);

  print('Después: $miLista'); // [2, 1] (¡Ahora sí funciona!)
}
