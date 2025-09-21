#include <Python.h>
#include <string.h>

// Structure Monster
typedef struct {
    char name[20];
    int health;
    int mana;
} Monster;

// Fonction pour booster la santé et le mana des monstres
static PyObject* boost_monsters(PyObject* self, PyObject* args) {
    PyObject* list;
    
    // Parser l’argument Python (liste de dictionnaires)
    if (!PyArg_ParseTuple(args, "O!", &PyList_Type, &list)) {
        return NULL;
    }

    Py_ssize_t len = PyList_Size(list);
    for (Py_ssize_t i = 0; i < len; i++) {
        PyObject* monster = PyList_GetItem(list, i);
        PyObject* health = PyDict_GetItemString(monster, "health");
        PyObject* mana = PyDict_GetItemString(monster, "mana");

        if (health && mana) {
            int new_health = PyLong_AsLong(health) + 10;  // boost health
            int new_mana = PyLong_AsLong(mana) + 5;       // boost mana
            PyDict_SetItemString(monster, "health", PyLong_FromLong(new_health));
            PyDict_SetItemString(monster, "mana", PyLong_FromLong(new_mana));
        }
    }

    Py_RETURN_NONE;
}

// Table des méthodes
static PyMethodDef methods[] = {
    {"boost_monsters", boost_monsters, METH_VARARGS, "Boost health and mana of monsters"},
    {NULL, NULL, 0, NULL}
};

// Structure du module
static struct PyModuleDef moduledef = {
    PyModuleDef_HEAD_INIT,
    "monsters",  // nom du module
    "Module pour gérer les monstres",
    -1,
    methods
};

// Initialisation du module
PyMODINIT_FUNC PyInit_monsters(void) {
    return PyModule_Create(&moduledef);
}
