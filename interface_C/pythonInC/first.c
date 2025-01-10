#include <Python.h>

int main() {
    // Initialiser l'interpréteur Python
    Py_Initialize();

    // Exécuter une simple commande Python
    PyRun_SimpleString("print('Hello from Python!')");

    // Terminer l'interpréteur Python
    Py_Finalize();

    return 0;
}
