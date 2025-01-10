#include <Python.h>

// Fonction qui retourne la somme de deux nombres
static PyObject* somme(PyObject* self, PyObject* args) {
    double a, b;
    
    // Parser les arguments
    if (!PyArg_ParseTuple(args, "dd", &a, &b)) {
        return NULL;
    }
    
    // Retourner la somme sous forme d'objet Python
    return PyFloat_FromDouble(a + b);
}

// Table des méthodes du module
static PyMethodDef methods[] = {
    {"somme", somme, METH_VARARGS, "Calcule la somme de deux nombres"},
    {NULL, NULL, 0, NULL}  // Indicateur de fin
};

// Structure du module
static struct PyModuleDef moduledef = {
    PyModuleDef_HEAD_INIT,
    "extensions",   // Nom du module
    "Un module pour additionner deux nombres",  // Description
    -1,         // Taille du module (non utilisé ici)
    methods     // Méthodes définies dans le module
};

// Fonction d'initialisation du module
PyMODINIT_FUNC PyInit_extensions(void) {
    return PyModule_Create(&moduledef);
}
