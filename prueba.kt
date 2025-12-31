// introduccion a Kotlin
// IntelliJ IDEA
fun main(){
   ejemplo2()
}

fun ejemplo1(){
    print("Hola, bienvenido a Kotlin!")
    var nombre = "Juan"
    println("Su nombre es:"+ nombre)
    nombre = "Pedro"
    println("Su nombre es:"+ nombre)
}
fun ejemplo2(){
    val pi = 3.1416
    println("El valor de pi es: $pi")
}

fun ejemplo3(){
    var nombre : String
    var edad : Int
    var sueldo : Double
    nombre = "Ana"
    edad = 28
    sueldo = 2500.50
    println("Nombre: $nombre, Edad: $edad, Sueldo: $sueldo")
}
fun ejemplo4(){
    var nombre : String
    var edad : Int
    var sueldo : Double
    print("Ingresa tu nombre: ")
    nombre = readLine() ?: ""
    print("Ingresa tu edad: ")
    edad = readLine()?.toIntOrNull() ?: 0
    print("Ingresa tu sueldo: ")
    sueldo = readLine()?.toDoubleOrNull() ?: 0.0
    println("Nombre: $nombre\nEdad: $edad\nSueldo: $sueldo")
}

