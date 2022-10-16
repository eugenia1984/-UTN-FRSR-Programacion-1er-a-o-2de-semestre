let firstName = " Maria Eugenia";
let lastName = "Costa";
let nameInThreeRows = "\nMaría\nEugenia\nCosta"
console.log(`${firstName} ${lastName}`);
console.info(`El nombre completo en filas: ${nameInThreeRows}`)
// Data type
// String
let name = "Maria Eugenia"
console.log(`La variable de tipo String es: name = ${name}`)
// number
let number_one = 1
console.log(`La variable de tipo Number es: number_one = ${number_one}`)
// Object
console.info("**** OBJECT **** ")
const objetoPersona = {
  firstName: "Maria Eugenia ",
  lastName: "Costa"
}
console.log(`Este es mi objeto objetoPersona.`)
console.log(`Tiene la clave firstName con su valor: ${objetoPersona.firstName} y la clave lastName con su valor ${objetoPersona.lastName}`)
// Boolean
let bandera = true
console.log(`Mi variable boolean bandera, tiene el valor: ${bandera}`)
// Function (declarativa)
function myFunctionSayHi() {
  console.log("Hi")
}
myFunctionSayHi(); // Hi
/*
La misma per en ARROW FUNCTION 
myFunctionSayHi() => console.log("Hi")
*/

// Symbol
const simbolo = Symbol(1)
console.log(simbolo) // 1

// Class
class Persona {
  // constructor
  constructor(firstName, lastName) {
    // Atributos
    this.firstName = firstName;
    this.lastName = lastName;
  }
  // Metodos
}
let persona1 = new Persona("Maria Eugenia", "Costa")
console.log(persona1)
// undefined
let indefinida;
console.log(`Mi variable indefinida: ${indefinida}`)
// arrays
const cars = ["Citroen", "Audi", "BMW"]