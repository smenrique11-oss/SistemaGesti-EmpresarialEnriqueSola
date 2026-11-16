/// Calcula los puntos totales sumando 3 por victoria y 1 por empate.
/// 
/// Recibe cada partido, separa el marcador con [split] y acumula los puntos.
int points(List<String> games) {
  int total = 0;

  for (String partido in games) {
    // Separa el texto "x:y" en una lista con dos elementos: ["x", "y"]
    var goles = partido.split(':');

    int x = int.parse(goles[0]); // Nuestros goles
    int y = int.parse(goles[1]); // Goles del rival

    if (x > y) {
      total += 3; // Victoria
    } else if (x == y) {
      total += 1; // Empate
    }
  }

  return total;
}

void main() {
  print(points(['1:0', '2:0', '3:0', '4:0', '2:1', '3:1', '4:1', '3:2', '4:2', '4:3'])); // Output: 30
  print(points(['1:1', '2:2', '3:3', '4:4', '2:2', '3:3', '4:4', '3:3', '4:4', '0:0'])); // Output: 10
  print(points(['0:1', '0:2', '0:3', '0:4', '1:2', '1:3', '1:4', '2:3', '2:4', '3:4'])); // Output: 0
}
