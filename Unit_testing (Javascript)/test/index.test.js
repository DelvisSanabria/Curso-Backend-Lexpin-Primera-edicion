let variable1 = 10
let variable2 = 20

test('Suma de variable1 y variable2', () => {
    expect(variable1 + variable2).toBe(30)
})

//Aqui se ejecutaria el AfterEach

test('Resta de variable1 y variable2', () => {
    expect(variable1 - variable2).toBe(-10)
})

//metodo describe para agrupar pruebas
describe('Pruebas matematicas', () => {
    test('Multiplicacion de variable1 y variable2', () => {
        expect(variable1 * variable2).toBe(200)
    }, 1000) //tiempo de espera para la prueba
    test('Division de variable1 y variable2', () => {
        expect(variable1 / variable2).toBe(0.5)
    })
})

//metodo it para pruebas individuales
it('Suma de variable1 y variable2', () => {
    expect(variable1 + variable2).toBe(30)
})

//metodo beforeEach para ejecutar una funcion antes de cada prueba

/* beforeEach(() => {
    variable1 = 15
    variable2 = 25
}) */

//metodo afterEach para ejecutar una funcion despues de cada prueba
/* afterEach(() => {
    variable1 = 0
    variable2 = 0
})
 */
/* test('Suma de variable1 y variable2 despues de afterEach', () => {
    expect(variable1 + variable2).toBe(0)
})  */

//metodo beforeAll para ejecutar una funcion antes de todas las pruebas
/* beforeAll(() => {
    variable1 = 15
    variable2 = 25
}) */

/* test('Suma de variable1 y variable2 despues de beforeAll', () => {
    expect(variable1 + variable2).toBe(40)
})
 */
//metodo afterAll para ejecutar una funcion despues de todas las pruebas
/* afterAll(() => {
    variable1 = 0
    variable2 = 0
}) */

/* test('Suma de variable1 y variable2 despues de afterAll', () => {
    expect(variable1 + variable2).toBe(0)
}) */

//aserciones y matchers

//not: invertir el resultado de la asercion
test('Suma de variable1 y variable2 no es 40', () => {
    expect(variable1 + variable2).not.toBe(40)
})

//any: verificar que el valor es del tipo especificado
//toEqual: verificar que el valor es igual al esperado
test('Variable1 es un numero', () => {
    expect(variable1).toEqual(expect.any(Number))
})

//toBe: verificar que el valor es exactamente igual al esperado
test('Variable1 es igual a 10', () => {
    expect(variable1).toBe(10)
})

//toBeTruthy: verificar que el valor es verdadero
test('Variable1 es verdadero', () => {
    expect(variable1).toBeTruthy()
})

//toBeFalsy: verificar que el valor es falso
test('Variable1 es falso', () => {
    expect(variable1).toBeFalsy()
})

//toMatch: verificar que el valor coincide con una expresion regular
test('Variable1 es un numero', () => {
    expect(variable1).toMatch(/^\d+$/)
}) 

//toContain: verificar que el valor contiene un elemento especifico
test('Variable1 contiene el numero 1', () => {
    expect(variable1.toString()).toContain('1')
})

//toBeCloseTo: verificar que el valor es cercano al esperado
test('Variable1 es cercano a 10', () => {
    expect(3.14159).toBeCloseTo(3.14, 2)
})

//toBeDefined: verificar que el valor esta definido
test('Variable1 esta definida', () => {
    expect(variable1).toBeDefined()
})

//toBeUndefined: verificar que el valor no esta definido
test('Variable3 no esta definida', () => {
    expect(variable2).toBeUndefined()
})

//toBeNull: verificar que el valor es null
test('Variable3 es null', () => {
    expect(variable2).toBeNull()
})

//toBeGreaterThan: verificar que el valor es mayor que el esperado
test('Variable1 es mayor que 5', () => {
    expect(variable1).toBeGreaterThan(5)
})

//toBeLessThan: verificar que el valor es menor que el esperado
test('Variable1 es menor que 15', () => {
    expect(variable1).toBeLessThan(15)
})

//toBeGreaterThanOrEqual: verificar que el valor es mayor o igual que el esperado
test('Variable1 es mayor o igual que 10', () => {
    expect(variable1).toBeGreaterThanOrEqual(10)
})

//toBeLessThanOrEqual: verificar que el valor es menor o igual que el esperado
test('Variable1 es menor o igual que 10', () => {
    expect(variable1).toBeLessThanOrEqual(10)
})

//toBeNaN: verificar que el valor es NaN
test('Variable1 es NaN', () => {
    expect(variable1).toBeNaN()
})

//toBeContainEqual: verificar que el valor contiene un elemento especifico y es igual al esperado
test('Array contiene el numero 1', () => {
    const array = [1, 2, 3, 4, 5]
    expect(array).toContainEqual(1)
})

//toHaveLength: verificar que el valor tiene una longitud especifica
test('Array tiene una longitud de 5', () => {
    const array = [1, 2, 3, 4]
    expect(array).toHaveLength(5)
})

//toBeInstanceOf: verificar que el valor es una instancia de una clase
test('Variable1 es una instancia de Number', () => {
    expect(variable1).toBeInstanceOf(Number)
})

//toHaveProperty: verificar que el valor tiene una propiedad especifica
test('Objeto tiene la propiedad nombre', () => {
    const objeto = { nombre: 'jesus', edad: 30 }
    expect(objeto).toHaveProperty('nombre')
})

//toMatchObject: verificar que el valor coincide con un objeto especifico
test('Objeto coincide con el objeto esperado', () => {
    const objeto = { nombre: 'jesus', edad: 30 }
    expect(objeto).toMatchObject({ nombre: 'jesus' })
})

//toThrow: verificar que una funcion lanza un error
test('Funcion lanza un error', () => {
    const funcion = () => { throw new Error('Error de prueba') }
    expect(funcion).toThrow('Error de prueba')
})

//toThrowError: verificar que una funcion lanza un error especifico
test('Funcion lanza un error especifico', () => {
    const funcion1 = () => { throw new Error('Error de prueba') }
    expect(funcion1).toThrowError('Error de prueba')
})


//Pruebas asincronas
test('Prueba asincrona con done', async() => {
    const data = await fetchData()
    expect(data).toBe('data')
});

function fetchData() {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve('data')
        }, 1000)
    })
}

//Promises
test('Prueba asincrona con Promises', () => {
    return fetchData().then(data => {
        expect(data).toBe('data')
    })
});

test('Prueba asincrona con Promises', () => {
  return expect(fetchData()).resolves.toBe('data')
});

//rejects
test('Prueba asincrona con Promises', () => {
    return expect(fetchData()).rejects.toBe('error')
});


/* 

#Proyecto de practica opcional de Jest:

Realizar pruebas unitarias a todos los middlewares y controladores de su propio proyecto final de
NodeJS o NestJS, utilizando Jest como framework de pruebas. Asegurarse de cubrir todos los casos posibles, incluyendo casos de éxito y casos de error. Documentar los resultados de las pruebas y cualquier problema encontrado durante el proceso.

*/