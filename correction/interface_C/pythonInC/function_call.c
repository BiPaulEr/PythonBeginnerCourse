#include <Python.h>

int main() {
    // Initialisation de l'interpréteur Python
    Py_Initialize();

    // Importation d'un module Python
    PyObject *pName = PyUnicode_DecodeFSDefault("math");
    PyObject *pModule = PyImport_Import(pName);
    Py_XDECREF(pName);

    if (pModule != NULL) {
        // Récupérer la fonction "sqrt" du module math
        PyObject *pFunc = PyObject_GetAttrString(pModule, "sqrt");

        if (PyCallable_Check(pFunc)) {
            // Appeler la fonction sqrt avec un argument
            PyObject *pArgs = PyTuple_Pack(1, PyFloat_FromDouble(16.0));
            PyObject *pValue = PyObject_CallObject(pFunc, pArgs);

            if (pValue != NULL) {
                // Afficher le résultat
                printf("La racine carrée de 16.0 est : %f\n", PyFloat_AsDouble(pValue));
                Py_XDECREF(pValue);
            } else {
                PyErr_Print();
            }
            Py_XDECREF(pArgs);
        } else {
            PyErr_Print();
        }
        Py_XDECREF(pFunc);
        Py_XDECREF(pModule);
    } else {
        PyErr_Print();
    }

    // Finalisation de l'interpréteur Python
    Py_Finalize();

    return 0;
}
