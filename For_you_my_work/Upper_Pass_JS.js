var a = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"];
var number = -1;
while (number != a.lenght + 1) {
  number = a.length + 1;
  a[number] = a[number].toUpperCase();
}
console.log(a);