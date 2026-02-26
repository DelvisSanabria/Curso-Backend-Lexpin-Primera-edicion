//Los objetos son una colección de propiedades, y una propiedad es una asociación entre un nombre (o clave) y un valor. El valor de una propiedad puede ser una función, lo que entonces se llama un método.

let car = {
  //Propiedades clave - valor
    make: 'Toyota',
    model: 'Corolla',
    year: 2020,
    color: 'Blanco',
    //metodos
    start: function() {
        console.log('El coche se ha encendido');
    },
    stop: function() {
        console.log('El coche se ha apagado');
    }
}

//Acceder a las propiedades del objeto

console.log(car.make); // Output: Toyota
console.log(car['model']); // Output: Corolla

//Llamar a los métodos del objeto

car.start(); // Output: El coche se ha encendido
car.stop(); // Output: El coche se ha apagado

//Reasignar una propiedad del objeto

car.color = 'Rojo';
console.log(car.color); // Output: Rojo

car['year'] = 2021;
console.log(car.year); // Output: 2021


let car2 = {
  //Propiedades clave - valor
    make: 'Honda',
    model: 'Civic',
    year: 2019,
    colors : ['Rojo', 'Azul', 'Negro'],
    engine: "6 cilindros",
    tansmission: "Manual",
    //metodos
    start: function() {
      console.log(`El coche ${this.make} ${this.model} se ha encendido`);
        },
    stop: function() {
    console.log('El coche se ha apagado');
    },
    back : function() {
      console.log('El coche se ha retrocedido');
      }
    }


car2.start(); // Output: El coche Honda Civic se ha encendido


//Yo puedo agregar metodos al objeto en cualquier momento

car2.accelerate = function() {
  console.log('El coche se ha acelerado');
}

car2.accelerate(); // Output: El coche se ha acelerado


//Metodos de objetos propios de javascript

let person = {
  name: 'John',
  age: 30,
  country: 'USA',
  phone: '123-456-7890',
  direction: '123 Main St',
  city: 'New York'
}

//Object.key(object): Devuelve un array con las claves del objeto
console.log(Object.keys(person)); // Output: ['name', 'age', 'country', 'phone', 'direction', 'city']

//Object.values(object): Devuelve un array con los valores del objeto
console.log(Object.values(person)); // Output: ['John', 30, 'USA', '123-456-7890', '123 Main St', 'New York']

//Object.entries(object): Devuelve un array con los pares clave-valor del objeto
console.log(Object.entries(person)); // Output: [['name', 'John'], ['age', 30], ['country', 'USA'], ['phone', '123-456-7890'], ['direction', '123 Main St'], ['city', 'New York']]

//Object.assign(target, source): Copia las propiedades de un objeto a otro

const data = {
  name: 'John',
  age: 30,
  country: 'USA'
}

const newData = {
  activity: 'Running',
  city: 'New York'
}

Object.assign(data, newData, {phone: '123-456-7890'});

console.log(data); // Output: {name: 'John', age: 30, country: 'USA', activity: 'Running', city: 'New York', phone: '123-456-7890'}


//.hasOwnProperty(key): Devuelve true si el objeto tiene la propiedad especificada como una propiedad directa del objeto, en lugar de heredada a través de la cadena de prototipos.

console.log(data.hasOwnProperty('name'));


//.toString(): Devuelve una cadena que representa al objeto.

console.log(data.toString()); // Output: [object Object]
