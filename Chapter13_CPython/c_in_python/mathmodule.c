#define PY_SSIZE_T_CLEAN
#include "Python.h"

static PyObject *method_add(PyObject *self, PyObject *args)
{
    PyObject *list_a = NULL;
    PyObject *list_b = NULL;

    /* Parse arguments */
    if (!PyArg_ParseTuple(args, "OO", &list_a, &list_b))
    {
        PyErr_SetString(PyExc_TypeError, "parameter must be a list.");
        return NULL;
    }

    Py_ssize_t len_a = PyList_Size(list_a);
    Py_ssize_t len_b = PyList_Size(list_b);

    if (len_a != len_b)
    {
        PyErr_SetString(PyExc_ValueError, "lists must have equal length.");
        return NULL;
    }

    PyObject *result = PyList_New(len_a);

    for (int i = 0; i < len_a; i++)
    {
        PyObject *item_a = PyList_GetItem(list_a, i);
        PyObject *item_b = PyList_GetItem(list_b, i);

        if ((!PyLong_Check(item_a) && !PyFloat_Check(item_a)) ||
            (!PyLong_Check(item_b) && !PyFloat_Check(item_b)))
        {
            PyErr_SetString(PyExc_ValueError, "list items must be numbers.");
            return NULL;
        }

        long long sum = PyLong_AsLong(item_a) + PyLong_AsLong(item_b);
        PyList_SetItem(result, i, PyLong_FromLong(sum));
    }

    return result;
}

static PyObject *method_clip(PyObject *self, PyObject *args)
{
    PyObject *list = NULL;
    double min_value = 0.0;
    double max_value = 0.0;

    /* Parse arguments */
    if (!PyArg_ParseTuple(args, "Off", &list, &min_value, max_value))
    {
        PyErr_SetString(PyExc_TypeError, "parameter must be a list.");
        return NULL;
    }

    Py_ssize_t len = PyList_Size(list);

    if (len == 0)
    {
        return NULL;
    }

    PyObject *result = PyList_New(len);

    for (int i = 0; i < len; i++)
    {
        PyObject *item = PyList_GetItem(list, i);

        if (!PyLong_Check(item) && !PyFloat_Check(item))
        {
            PyErr_SetString(PyExc_ValueError, "list items must be numbers.");
            return NULL;
        }

        double temp = PyLong_AsLong(item);

        if (temp < min_value)
        {
            temp = min_value;
        }
        else if (temp > max_value)
        {
            temp = max_value;
        }

        PyList_SetItem(result, i, PyLong_FromLong(temp));
    }

    return result;
}

static PyMethodDef addMethods[] = {
    {"add", method_add, METH_VARARGS, "CPython Function"},
    {"clip", method_clip, METH_VARARGS, "CPython Function"},
    {NULL, NULL, 0, NULL} };

static struct PyModuleDef addmodule = {
    PyModuleDef_HEAD_INIT, "add", "CPython Module", -1, addMethods };

PyMODINIT_FUNC PyInit_add(void)
{
    return PyModule_Create(&addmodule);
}
