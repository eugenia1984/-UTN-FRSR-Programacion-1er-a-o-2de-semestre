/*** Ejericico 1: Calcular la estacion del año ***/
let mes = 4;
let estacion = ""; 
// el profesor lo deja solo nombrandolo, pero es undefined, 
// ya lo inicializo como string vacio
// lo hace con muchos if else if else, pero lo hago con switch
switch (mes) {
  case 1:
  case 2:
  case 3:
    estacion = "Verano";  
    break;
  case 4:
  case 5:
  case 6:
    estacion = "Otoño";
    break;
  case 7:
  case 8:
  case 9:
    estacion = "Invierno";
    break;
  case 10:
  case 11:
  case 12:
    estacion = "Primavera";
    break;  
  default:
    primavera = "valor incorrecto";
    break;
}
console.log(`El valor que corresponde a la estación es: ${estacion}`);

/*** Ejercicio hora del dia ***/
let horaDia = 9;
let mensaje = "";

if(horaDia>06 && horaDia<=11) {
  mensaje="Buen día";
} else if(horaDia>=12 && horaDia <=16) {
  mensaje= "Buenas tardes"
} else if(horaDia>017 && horaDia <=19) {
  mensaje= "Buen atardecer";
} else if(horaDia <=20 && horaDia<=23) {
   mensaje="Buenas noches";
} else {
  mensaje="Valor incorrecto";
}
console.log(mensaje);
