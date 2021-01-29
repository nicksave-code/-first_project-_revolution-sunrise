/*function forest2(y) {
 return y+1;
}
forest2(6);*/
//f = fahrenheit
function f(c) {
  return c + " C° is equal to "+ ((9/5)*c+32);
}
//k = kelvin
function k(c) {
  return c + " C° is equal to " + ((c + 273.15)*(1/1));
}
//fahrenheit to celsius
document.getElementById("demo").innerHTML=(f(10)+ " F°")
//kelvin to celsius
document.getElementById("kelvin").innerHTML=(k(22)+ " K°")
