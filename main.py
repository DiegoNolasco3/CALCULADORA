from sumar import sumar
from resta import restar
from multiplicacion import multiplicar
from dividir import dividir
from suma_avanzada import suma_avanzada

def menu():
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Suma avanzada")
    print("6. Salir")

def main():
    while True:
        menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            print("El resultado de la suma es:", sumar(a, b))
        elif opcion == '2':
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            print("El resultado de la resta es:", restar(a, b))
        elif opcion == '3':
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            print("El resultado de la multiplicación es:", multiplicar(a, b))
        elif opcion == '4':
            a = float(input("Ingrese el dividendo: "))
            b = float(input("Ingrese el divisor: "))
            print("El resultado de la división es:", dividir(a, b))
        elif opcion == '5':
            cantidad_numeros = int(input("Ingrese la cantidad de números a sumar: "))
            numeros = [float(input(f"Ingrese el número {i+1}: ")) for i in range(cantidad_numeros)]
            print("El resultado de la suma avanzada es:", suma_avanzada(*numeros))
        elif opcion == '6':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
