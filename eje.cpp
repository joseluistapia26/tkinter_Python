#include <iostream>
#include<string>
using namespace std;
void ejemplo1(void);
void ejemplo2(void);
double suma(double a, double b);
int main(){
    //ejemplo1();
    ejemplo2();
    return 0;
}
void ejemplo1() {
    cout << "Bloque 1." << endl;
    string nombre;
    int num;
    cout << "Ingrese un numero: ";
    cin >> num;
    cout << "El numero ingresado es: " << num << endl;
    cout<< "Ingrese su nombre: ";
    cin >> nombre;
    cout << "Hola, " << nombre << "! Bienvenido a C++." << endl;
}

void ejemplo2() {
    double n1, n2, resultado;
    cout << "Ingrese el primer numero: ";
    cin >> n1;
    cout << "Ingrese el segundo numero: ";
    cin >> n2;
    resultado = suma(n1, n2);
    cout << "La suma de " << n1 << " y " << n2 << " es: " << resultado << endl;
}
double suma(double a, double b) {
    return a + b;
}



