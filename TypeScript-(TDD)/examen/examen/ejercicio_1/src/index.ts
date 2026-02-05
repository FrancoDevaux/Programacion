import { Calculator } from './calculator';

//La respuesta para cada uno de estos ejercicios colocar un console.log
//con el nombre ejercicio mas el numero del ejercicio mas el resultado
console.log('a desarrollar los ejercicios!!');

//1. Ordernar alfabeticamente el siguiente array
const lettersArray = ['e', 'b', 'g', 'z', 'y', 'm'];
const sortLetters = [...lettersArray].sort();
console.log('\nEjercicio 1:', sortLetters);

//2. Ordenar del mas pequeño al mas grande el siguiente array
const numArray = [5, 2, 7, 0, 10, 6];
const sortNumAsc = [...numArray].sort((a, b) => a - b);
console.log('\nEjercicio 2:', sortNumAsc);

//3. Ordenar numArray del mas grande al mas pequeño
const sortNumDesc = [...numArray].sort((a, b) => b - a);
console.log('\nEjercicio 3:', sortNumDesc);

//4. Agregarle a este array de objetos un nuevo campo llamado fullName
//que tiene que llevar tanto el name como el lastName
const objectArray = [
  {
    name: 'Josue',
    lastName: 'Escobar',
  },
  {
    name: 'Sofia',
    lastName: 'Escobar',
  },
  {
    name: 'Daniel',
    lastName: 'Escobar',
  },
  {
    name: 'Bernabe',
    lastName: 'Escobar',
  },
];

const objectArrayWithFullName = objectArray.map(person => ({
  ...person,
  fullName: `${person.name} ${person.lastName}`
}));
console.log('\nEjercicio 4:', objectArrayWithFullName);

//5. Crear un nuevo array donde el key sea el nombre del mes, y el value su valor numerico
//eje. {Enero: 1}
const monthsArray = [
  'enero',
  'febrero',
  'marzo',
  'abril',
  'mayo',
  'junio',
  'julio',
];
 
const monthsObjectArray = monthsArray.map((month, index) => ({
  [month]: index + 1
}));
console.log('\nEjercicio 5:', monthsObjectArray);

//6. Crear un nuevo array apartir de este, donde solo se tengan los emails de cada usuario
const usersArray = [
  {
    name: 'Josue',
    lastName: 'Escobar',
    email: 'josue.com',
  },
  {
    name: 'Sofia',
    lastName: 'Escobar',
    email: 'sofia.com',
  },
  {
    name: 'Daniel',
    lastName: 'Escobar',
    email: 'daniel.com',
  },
  {
    name: 'Bernabe',
    lastName: 'Escobar',
    email: 'bernabe.com',
  },
];

const emailsArray = usersArray.map(user => user.email);
console.log('\nEjercicio 6:', emailsArray);

//7. Filtrar array para que solo muestre los paises habilitados, osea enabled: true
const countryArray = [
  {
    name: 'Guatemala',
    enabled: false,
  },
  {
    name: 'EEUU',
    enabled: true,
  },
  {
    name: 'Peru',
    enabled: false,
  },
  {
    name: 'Mexico',
    enabled: true,
  },
];

const enabledCountry = countryArray.filter(country => country.enabled === true);
console.log('\nEjercicio 7:', enabledCountry);

//8. Generar un nuevo array en donde solo se agregen los elementos que esten en los 2 arrays
const firstArray = [
  {
    id: 1,
    name: 'Josue',
    lastName: 'Escobar',
  },
  {
    id: 2,
    name: 'Sofia',
    lastName: 'Escobar',
  },
  {
    id: 3,
    name: 'Daniel',
    lastName: 'Escobar',
  },
  {
    id: 4,
    name: 'Bernabe',
    lastName: 'Escobar',
  },
];

const secondArray = [
  {
    id: 5,
    name: 'Lorena',
    lastName: 'Escobar',
  },
  {
    id: 6,
    name: 'Edis',
    lastName: 'Escobar',
  },
  {
    id: 1,
    name: 'Josue',
    lastName: 'Escobar',
  },
  {
    id: 7,
    name: 'Douglas',
    lastName: 'Escobar',
  },
  {
    id: 8,
    name: 'Rony',
    lastName: 'Escobar',
  },
  {
    id: 4,
    name: 'Bernabe',
    lastName: 'Escobar',
  },
];

const elements = firstArray.filter(person1 => 
  secondArray.find(person2 => person2.id === person1.id)
);
console.log('\nEjercicio 8:', elements);

//9. Crear un nuevo array, donde solo se agregen los elementos que no estan compartidos entre los 2 arrays aenteriores
const notElements = [
  ...firstArray.filter(person1 => !secondArray.some(person2 => person2.id === person1.id)),
  ...secondArray.filter(person2 => !firstArray.some(person1 => person1.id === person2.id))
];
console.log('\nEjercicio 9:', notElements);

//10. Agregar los meses faltantes al array de meses, y que esten en el orden cronologico es decir, enero, febrero...
const newMonthArray = [
  {
    id: 1,
    name: 'enero',
  },
  {
    id: 5,
    name: 'mayo',
  },
  {
    id: 8,
    name: 'agosto',
  },
  {
    id: 10,
    name: 'octubre',
  },
  {
    id: 12,
    name: 'diciembre',
  },
];

const missingMonthArray = [
  {
    id: 11,
    name: 'noviembre',
  },
  {
    id: 2,
    name: 'febrero',
  },
  {
    id: 9,
    name: 'septiembre',
  },
  {
    id: 3,
    name: 'marzo',
  },
  {
    id: 6,
    name: 'junio',
  },
  {
    id: 4,
    name: 'abril',
  },
  {
    id: 7,
    name: 'julio',
  },
];

const allMonths = [...newMonthArray, ...missingMonthArray];
const sortMonths = allMonths.sort((a, b) => a.id - b.id);
console.log('\nEjercicio 10:', sortMonths);

//11. Agregar el campo faltante de email a los usuarios obteniendolo desde el array de userDetails
const usersWithoutEmail = [
  {
    name: 'Josue',
    lastName: 'Escobar',
    phone: '123456789',
  },
  {
    name: 'Sofia',
    lastName: 'Escobar',
    phone: '123456779',
  },
  {
    name: 'Daniel',
    lastName: 'Escobar',
    phone: '123456769',
  },
  {
    name: 'Bernabe',
    lastName: 'Escobar',
    phone: '123456759',
  },
];

const userDetails = [
  {
    email: 'josue.com',
    phone: '123456789',
  },
  {
    email: 'sofia.com',
    phone: '123456779',
  },
  {
    email: 'daniel.com',
    phone: '123456769',
  },
  {
    email: 'bernabe.com',
    phone: '123456759',
  },
];

const usersWithEmail = usersWithoutEmail.map(user => {const userDetail = userDetails.find(detail => detail.phone === user.phone);
  return {
    ...user,
    email: userDetail ? userDetail.email : "No email"
  };
});
console.log('\nEjercicio 11:', usersWithEmail);

//12. En un nuevo archivo crear la clase llamada calculator, esta clase tiene que tener los siguientes metodos
//sum, sub, div y mult que cada uno tiene que poder recibir 2 numeros y dependiendo de la funcion que sea, suma
//divide, resta o multiplica, y al final muestra el resultado de la operacion con un console.log,.
//hacer una instancia de esta clase aqui en este archivo y mandar a llamar los 4 metodos
const calculator = new Calculator();
console.log('\nEjercicio 12:');
calculator.suma(10, 10);
calculator.resta(10, 5);
calculator.division(10, 2);
calculator.multiplicacion(10, 10);