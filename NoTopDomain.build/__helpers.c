// This file contains helper functions that are automatically created from
// templates.

#include "nuitka/prelude.h"

extern PyObject *callPythonFunction(PyObject *func, PyObject *const *args, int count);


PyObject *CALL_FUNCTION_WITH_ARGS11(PyObject *called, PyObject *const *args) {
    CHECK_OBJECT(called);
     CHECK_OBJECTS(args, 11); 

    if (Nuitka_Function_Check(called)) {
        if (unlikely(Py_EnterRecursiveCall((char *)" while calling a Python object"))) {
            return NULL;
        }

        struct Nuitka_FunctionObject *function = (struct Nuitka_FunctionObject *)called;
        PyObject *result;

        if (function->m_args_simple && 11 == function->m_args_positional_count){
            for (Py_ssize_t i = 0; i < 11; i++) {
                Py_INCREF(args[i]);
            }
            result = function->m_c_code(function,  (PyObject **)args );
        } else if (function->m_args_simple && 11 + function->m_defaults_given == function->m_args_positional_count) {
            NUITKA_DYNAMIC_ARRAY_DECL(python_pars, PyObject *, function->m_args_positional_count);

            memcpy(python_pars, args, 11 * sizeof(PyObject *));
            memcpy(python_pars + 11, &PyTuple_GET_ITEM(function->m_defaults, 0), function->m_defaults_given * sizeof(PyObject *));

            for (Py_ssize_t i = 0; i < function->m_args_positional_count; i++) {
                Py_INCREF(python_pars[i]);
            }

            result = function->m_c_code(function, python_pars);
        } else {
            result = Nuitka_CallFunctionPosArgs(function, args, 11);
        }

        Py_LeaveRecursiveCall();

        return result;
    } else if (Nuitka_Method_Check(called)) {
        struct Nuitka_MethodObject *method = (struct Nuitka_MethodObject *)called;

        if (method->m_object == NULL) {
            PyObject *self = args[0];

            int res = PyObject_IsInstance(self, method->m_class);

            if (unlikely(res < 0)) {
                return NULL;
            } else if (unlikely(res == 0)) {
                PyErr_Format(PyExc_TypeError,
                             "unbound compiled_method %s%s must be called with %s instance as first argument (got %s "
                             "instance instead)",
                             GET_CALLABLE_NAME((PyObject *)method->m_function),
                             GET_CALLABLE_DESC((PyObject *)method->m_function), GET_CLASS_NAME(method->m_class),
                             GET_INSTANCE_CLASS_NAME((PyObject *)self));

                return NULL;
            }

            return Nuitka_CallFunctionPosArgs(method->m_function, args, 11);
        } else {
            if (unlikely(Py_EnterRecursiveCall((char *)" while calling a Python object"))) {
                return NULL;
            }

            struct Nuitka_FunctionObject *function = method->m_function;

            PyObject *result;

            if (function->m_args_simple && 11 + 1 == function->m_args_positional_count) {
                PyObject *python_pars[11 + 1];

                python_pars[0] = method->m_object;
                Py_INCREF(method->m_object);

                for (Py_ssize_t i = 0; i < 11; i++) {
                    python_pars[i + 1] = args[i];
                    Py_INCREF(args[i]);
                }
                result = function->m_c_code(function, python_pars);
            } else if (function->m_args_simple && 11 + 1 + function->m_defaults_given == function->m_args_positional_count) {
                NUITKA_DYNAMIC_ARRAY_DECL(python_pars, PyObject *, function->m_args_positional_count);

                python_pars[0] = method->m_object;
                Py_INCREF(method->m_object);

                memcpy(python_pars+1, args, 11 * sizeof(PyObject *));
                memcpy(python_pars+1 + 11, &PyTuple_GET_ITEM(function->m_defaults, 0), function->m_defaults_given * sizeof(PyObject *));

                for (Py_ssize_t i = 1; i < function->m_args_overall_count; i++) {
                    Py_INCREF(python_pars[i]);
                }

                result = function->m_c_code(function, python_pars);
            } else {
                result = Nuitka_CallMethodFunctionPosArgs(function, method->m_object, args, 11);
            }

            Py_LeaveRecursiveCall();

            return result;
        }
#if !defined(_NUITKA_EXPERIMENTAL_DISABLE_CFUNCTION_CALL_OPT)
    } else if (PyCFunction_CheckExact(called)) {
        // Try to be fast about wrapping the arguments.
        int flags = PyCFunction_GET_FLAGS(called) & ~(METH_CLASS | METH_STATIC | METH_COEXIST);

        if (unlikely(flags & METH_NOARGS)) {
            SET_CURRENT_EXCEPTION_TYPE0_FORMAT1(
                PyExc_TypeError,
                "%s() takes no arguments (11 given)",
                ((PyCFunctionObject *)called)->m_ml->ml_name
            );
            return NULL;
        } else if (unlikely(flags & METH_O)) {
            SET_CURRENT_EXCEPTION_TYPE0_FORMAT1(PyExc_TypeError,
                "%s() takes exactly one argument (11 given)",
                 ((PyCFunctionObject *)called)->m_ml->ml_name
            );
            return NULL;
        } else if (flags & METH_VARARGS) {
            // Recursion guard is not strictly necessary, as we already have
            // one on our way to here.
#ifdef _NUITKA_FULL_COMPAT
            if (unlikely(Py_EnterRecursiveCall((char *)" while calling a Python object"))) {
                return NULL;
            }
#endif
            PyCFunction method = PyCFunction_GET_FUNCTION(called);
            PyObject *self = PyCFunction_GET_SELF(called);

            PyObject *result;

#if PYTHON_VERSION < 0x360
            PyObject *pos_args = MAKE_TUPLE(args, 11);
            if (flags & METH_KEYWORDS) {
                result = (*(PyCFunctionWithKeywords)method)(self, pos_args, NULL);
            } else {
                result = (*method)(self, pos_args);
            }

            Py_DECREF(pos_args);
#else
            if (flags == (METH_VARARGS|METH_KEYWORDS)) {
            PyObject *pos_args = MAKE_TUPLE(args, 11);
                result = (*(PyCFunctionWithKeywords)method)(self, pos_args, NULL);
            Py_DECREF(pos_args);
            } else if (flags == METH_FASTCALL) {
#if PYTHON_VERSION < 0x370
                result = (*(_PyCFunctionFast)method)(self, (PyObject **)args, 11, NULL);
#else
            PyObject *pos_args = MAKE_TUPLE(args, 11);
                result = (*(_PyCFunctionFast)method)(self, &pos_args, 11);
            Py_DECREF(pos_args);
#endif
            } else {
            PyObject *pos_args = MAKE_TUPLE(args, 11);
                result = (*method)(self, pos_args);
            Py_DECREF(pos_args);
            }
#endif


#ifdef _NUITKA_FULL_COMPAT
            Py_LeaveRecursiveCall();
#endif

            return Nuitka_CheckFunctionResult(called, result);
        }
#endif
#if !defined(_NUITKA_EXPERIMENTAL_DISABLE_UNCOMPILED_FUNCTION_CALL_OPT)
    } else if (PyFunction_Check(called)) {
#if PYTHON_VERSION < 0x3b0
        return callPythonFunction(
            called,
            args,
            11
        );
#else
    return _PyFunction_Vectorcall(called, args, 11, NULL);
#endif
#endif
#if !defined(_NUITKA_EXPERIMENTAL_DISABLE_TYPE_CREATION_OPT)
    } else if (PyType_Check(called)) {
        PyTypeObject *type = Py_TYPE(called);

        if (type->tp_call == PyType_Type.tp_call) {
            PyTypeObject *called_type = (PyTypeObject *)(called);


            if (unlikely(called_type->tp_new == NULL)) {
                PyErr_Format(PyExc_TypeError, "cannot create '%s' instances", called_type->tp_name);
                return NULL;
            }

            PyObject *pos_args = NULL;
            PyObject *obj;

            if (called_type->tp_new == PyBaseObject_Type.tp_new) {
                if (unlikely(called_type->tp_flags & Py_TPFLAGS_IS_ABSTRACT)) {
                    formatCannotInstantiateAbstractClass(called_type);
                    return NULL;
                }

                obj = called_type->tp_alloc(called_type, 0);
                CHECK_OBJECT(obj);
            } else {
                pos_args = MAKE_TUPLE(args, 11);
                obj = called_type->tp_new(called_type, pos_args, NULL);
            }

            if (likely(obj != NULL)) {
                if (!Nuitka_Type_IsSubtype(obj->ob_type, called_type)) {
                    Py_DECREF(pos_args);
                    return obj;
                }

                // Work on produced type.
                type = Py_TYPE(obj);

                if (NuitkaType_HasFeatureClass(type) && type->tp_init != NULL) {
                    if (type->tp_init == default_tp_init_wrapper) {
                        Py_XDECREF(pos_args);
                        pos_args = NULL;

                        PyObject *init_method = Nuitka_TypeLookup(type, const_str_plain___init__);

                        // Not really allowed, since we wouldn't have the default wrapper set.
                        assert(init_method != NULL);

                        bool is_compiled_function = false;
                        bool init_method_needs_release = false;

                        if (likely(init_method != NULL)) {
                            descrgetfunc func = Py_TYPE(init_method)->tp_descr_get;

                            if (func == Nuitka_Function_Type.tp_descr_get) {
                                is_compiled_function = true;
                            } else if (func != NULL) {
                                init_method = func(init_method, obj, (PyObject *)(type));
                                init_method_needs_release = true;
                            }
                        }

                        if (unlikely(init_method == NULL)) {
                            if (!ERROR_OCCURRED()) {
                                SET_CURRENT_EXCEPTION_TYPE0_VALUE0(PyExc_AttributeError, const_str_plain___init__);
                            }

                            return NULL;
                        }

                        PyObject *result;
                        if (is_compiled_function) {
                            result = Nuitka_CallMethodFunctionPosArgs((struct Nuitka_FunctionObject const *)init_method, obj, args, 11);
                        } else {
                            result = CALL_FUNCTION_WITH_ARGS11(init_method, args);
                            if (init_method_needs_release) {
                                Py_DECREF(init_method);
                            }
                        }


                        if (unlikely(result == NULL)) {
                            Py_DECREF(obj);
                            return NULL;
                        }

                        Py_DECREF(result);

                        if (unlikely(result != Py_None)) {
                            Py_DECREF(obj);

                            SET_CURRENT_EXCEPTION_TYPE_COMPLAINT("__init__() should return None, not '%s'", result);
                            return NULL;
                        }
                    } else {
                        if (pos_args == NULL) {
                            pos_args = MAKE_TUPLE(args, 11);
                        }

                        if (unlikely(type->tp_init(obj, pos_args, NULL) < 0)) {
                            Py_DECREF(obj);
                            Py_XDECREF(pos_args);
                            return NULL;
                        }
                    }
                }
            }

            Py_XDECREF(pos_args);
            return obj;
        }
#endif
#if PYTHON_VERSION < 0x300
    } else if (PyClass_Check(called)) {
        PyObject *obj = PyInstance_NewRaw(called, NULL);

        PyObject *init_method = FIND_ATTRIBUTE_IN_CLASS((PyClassObject *)called, const_str_plain___init__);

        if (unlikely(init_method == NULL)) {
            if (unlikely(ERROR_OCCURRED())) {
                Py_DECREF(obj);
                return NULL;
            }

            Py_DECREF(obj);

            SET_CURRENT_EXCEPTION_TYPE0_STR(PyExc_TypeError, "this constructor takes no arguments");
            return NULL;
        }

        bool is_compiled_function = false;

        descrgetfunc descr_get = Py_TYPE(init_method)->tp_descr_get;

        if (descr_get == NULL) {
            Py_INCREF(init_method);
        } else if (descr_get == Nuitka_Function_Type.tp_descr_get) {
            is_compiled_function = true;
        } else if (descr_get != NULL) {
            PyObject *descr_method = descr_get(init_method, obj, called);

            if (unlikely(descr_method == NULL)) {
                return NULL;
            }

            init_method = descr_method;
        }

        PyObject *result;
        if (is_compiled_function) {
            result = Nuitka_CallMethodFunctionPosArgs((struct Nuitka_FunctionObject const *)init_method, obj, args, 11);
        } else {
            result = CALL_FUNCTION_WITH_ARGS11(init_method, args);
            Py_DECREF(init_method);
        }
        if (unlikely(result == NULL)) {
            return NULL;
        }

        Py_DECREF(result);

        if (unlikely(result != Py_None)) {
            SET_CURRENT_EXCEPTION_TYPE_COMPLAINT("__init__() should return None, not '%s'", result);
            return NULL;
        }

        return obj;
#endif
#if PYTHON_VERSION >= 0x380 && !defined(_NUITKA_EXPERIMENTAL_DISABLE_VECTORCALL_USAGE)
    } else if (PyType_HasFeature(Py_TYPE(called), _Py_TPFLAGS_HAVE_VECTORCALL)) {
        vectorcallfunc func = *((vectorcallfunc *)(((char *)called) + Py_TYPE(called)->tp_vectorcall_offset));

        if (likely(func != NULL)) {
            PyObject *result = func(called, args, 11, NULL);

            return Nuitka_CheckFunctionResult(called, result);
        }
#endif
    }

#if 0
    PRINT_NEW_LINE();
    PRINT_STRING("FALLBACK");
    PRINT_ITEM(called);
    PRINT_NEW_LINE();
#endif

    PyObject *pos_args = MAKE_TUPLE(args, 11);

    PyObject *result = CALL_FUNCTION(called, pos_args, NULL);

    Py_DECREF(pos_args);

    return result;
}
PyObject *CALL_FUNCTION_WITH_ARGS12(PyObject *called, PyObject *const *args) {
    CHECK_OBJECT(called);
     CHECK_OBJECTS(args, 12); 

    if (Nuitka_Function_Check(called)) {
        if (unlikely(Py_EnterRecursiveCall((char *)" while calling a Python object"))) {
            return NULL;
        }

        struct Nuitka_FunctionObject *function = (struct Nuitka_FunctionObject *)called;
        PyObject *result;

        if (function->m_args_simple && 12 == function->m_args_positional_count){
            for (Py_ssize_t i = 0; i < 12; i++) {
                Py_INCREF(args[i]);
            }
            result = function->m_c_code(function,  (PyObject **)args );
        } else if (function->m_args_simple && 12 + function->m_defaults_given == function->m_args_positional_count) {
            NUITKA_DYNAMIC_ARRAY_DECL(python_pars, PyObject *, function->m_args_positional_count);

            memcpy(python_pars, args, 12 * sizeof(PyObject *));
            memcpy(python_pars + 12, &PyTuple_GET_ITEM(function->m_defaults, 0), function->m_defaults_given * sizeof(PyObject *));

            for (Py_ssize_t i = 0; i < function->m_args_positional_count; i++) {
                Py_INCREF(python_pars[i]);
            }

            result = function->m_c_code(function, python_pars);
        } else {
            result = Nuitka_CallFunctionPosArgs(function, args, 12);
        }

        Py_LeaveRecursiveCall();

        return result;
    } else if (Nuitka_Method_Check(called)) {
        struct Nuitka_MethodObject *method = (struct Nuitka_MethodObject *)called;

        if (method->m_object == NULL) {
            PyObject *self = args[0];

            int res = PyObject_IsInstance(self, method->m_class);

            if (unlikely(res < 0)) {
                return NULL;
            } else if (unlikely(res == 0)) {
                PyErr_Format(PyExc_TypeError,
                             "unbound compiled_method %s%s must be called with %s instance as first argument (got %s "
                             "instance instead)",
                             GET_CALLABLE_NAME((PyObject *)method->m_function),
                             GET_CALLABLE_DESC((PyObject *)method->m_function), GET_CLASS_NAME(method->m_class),
                             GET_INSTANCE_CLASS_NAME((PyObject *)self));

                return NULL;
            }

            return Nuitka_CallFunctionPosArgs(method->m_function, args, 12);
        } else {
            if (unlikely(Py_EnterRecursiveCall((char *)" while calling a Python object"))) {
                return NULL;
            }

            struct Nuitka_FunctionObject *function = method->m_function;

            PyObject *result;

            if (function->m_args_simple && 12 + 1 == function->m_args_positional_count) {
                PyObject *python_pars[12 + 1];

                python_pars[0] = method->m_object;
                Py_INCREF(method->m_object);

                for (Py_ssize_t i = 0; i < 12; i++) {
                    python_pars[i + 1] = args[i];
                    Py_INCREF(args[i]);
                }
                result = function->m_c_code(function, python_pars);
            } else if (function->m_args_simple && 12 + 1 + function->m_defaults_given == function->m_args_positional_count) {
                NUITKA_DYNAMIC_ARRAY_DECL(python_pars, PyObject *, function->m_args_positional_count);

                python_pars[0] = method->m_object;
                Py_INCREF(method->m_object);

                memcpy(python_pars+1, args, 12 * sizeof(PyObject *));
                memcpy(python_pars+1 + 12, &PyTuple_GET_ITEM(function->m_defaults, 0), function->m_defaults_given * sizeof(PyObject *));

                for (Py_ssize_t i = 1; i < function->m_args_overall_count; i++) {
                    Py_INCREF(python_pars[i]);
                }

                result = function->m_c_code(function, python_pars);
            } else {
                result = Nuitka_CallMethodFunctionPosArgs(function, method->m_object, args, 12);
            }

            Py_LeaveRecursiveCall();

            return result;
        }
#if !defined(_NUITKA_EXPERIMENTAL_DISABLE_CFUNCTION_CALL_OPT)
    } else if (PyCFunction_CheckExact(called)) {
        // Try to be fast about wrapping the arguments.
        int flags = PyCFunction_GET_FLAGS(called) & ~(METH_CLASS | METH_STATIC | METH_COEXIST);

        if (unlikely(flags & METH_NOARGS)) {
            SET_CURRENT_EXCEPTION_TYPE0_FORMAT1(
                PyExc_TypeError,
                "%s() takes no arguments (12 given)",
                ((PyCFunctionObject *)called)->m_ml->ml_name
            );
            return NULL;
        } else if (unlikely(flags & METH_O)) {
            SET_CURRENT_EXCEPTION_TYPE0_FORMAT1(PyExc_TypeError,
                "%s() takes exactly one argument (12 given)",
                 ((PyCFunctionObject *)called)->m_ml->ml_name
            );
            return NULL;
        } else if (flags & METH_VARARGS) {
            // Recursion guard is not strictly necessary, as we already have
            // one on our way to here.
#ifdef _NUITKA_FULL_COMPAT
            if (unlikely(Py_EnterRecursiveCall((char *)" while calling a Python object"))) {
                return NULL;
            }
#endif
            PyCFunction method = PyCFunction_GET_FUNCTION(called);
            PyObject *self = PyCFunction_GET_SELF(called);

            PyObject *result;

#if PYTHON_VERSION < 0x360
            PyObject *pos_args = MAKE_TUPLE(args, 12);
            if (flags & METH_KEYWORDS) {
                result = (*(PyCFunctionWithKeywords)method)(self, pos_args, NULL);
            } else {
                result = (*method)(self, pos_args);
            }

            Py_DECREF(pos_args);
#else
            if (flags == (METH_VARARGS|METH_KEYWORDS)) {
            PyObject *pos_args = MAKE_TUPLE(args, 12);
                result = (*(PyCFunctionWithKeywords)method)(self, pos_args, NULL);
            Py_DECREF(pos_args);
            } else if (flags == METH_FASTCALL) {
#if PYTHON_VERSION < 0x370
                result = (*(_PyCFunctionFast)method)(self, (PyObject **)args, 12, NULL);
#else
            PyObject *pos_args = MAKE_TUPLE(args, 12);
                result = (*(_PyCFunctionFast)method)(self, &pos_args, 12);
            Py_DECREF(pos_args);
#endif
            } else {
            PyObject *pos_args = MAKE_TUPLE(args, 12);
                result = (*method)(self, pos_args);
            Py_DECREF(pos_args);
            }
#endif


#ifdef _NUITKA_FULL_COMPAT
            Py_LeaveRecursiveCall();
#endif

            return Nuitka_CheckFunctionResult(called, result);
        }
#endif
#if !defined(_NUITKA_EXPERIMENTAL_DISABLE_UNCOMPILED_FUNCTION_CALL_OPT)
    } else if (PyFunction_Check(called)) {
#if PYTHON_VERSION < 0x3b0
        return callPythonFunction(
            called,
            args,
            12
        );
#else
    return _PyFunction_Vectorcall(called, args, 12, NULL);
#endif
#endif
#if !defined(_NUITKA_EXPERIMENTAL_DISABLE_TYPE_CREATION_OPT)
    } else if (PyType_Check(called)) {
        PyTypeObject *type = Py_TYPE(called);

        if (type->tp_call == PyType_Type.tp_call) {
            PyTypeObject *called_type = (PyTypeObject *)(called);


            if (unlikely(called_type->tp_new == NULL)) {
                PyErr_Format(PyExc_TypeError, "cannot create '%s' instances", called_type->tp_name);
                return NULL;
            }

            PyObject *pos_args = NULL;
            PyObject *obj;

            if (called_type->tp_new == PyBaseObject_Type.tp_new) {
                if (unlikely(called_type->tp_flags & Py_TPFLAGS_IS_ABSTRACT)) {
                    formatCannotInstantiateAbstractClass(called_type);
                    return NULL;
                }

                obj = called_type->tp_alloc(called_type, 0);
                CHECK_OBJECT(obj);
            } else {
                pos_args = MAKE_TUPLE(args, 12);
                obj = called_type->tp_new(called_type, pos_args, NULL);
            }

            if (likely(obj != NULL)) {
                if (!Nuitka_Type_IsSubtype(obj->ob_type, called_type)) {
                    Py_DECREF(pos_args);
                    return obj;
                }

                // Work on produced type.
                type = Py_TYPE(obj);

                if (NuitkaType_HasFeatureClass(type) && type->tp_init != NULL) {
                    if (type->tp_init == default_tp_init_wrapper) {
                        Py_XDECREF(pos_args);
                        pos_args = NULL;

                        PyObject *init_method = Nuitka_TypeLookup(type, const_str_plain___init__);

                        // Not really allowed, since we wouldn't have the default wrapper set.
                        assert(init_method != NULL);

                        bool is_compiled_function = false;
                        bool init_method_needs_release = false;

                        if (likely(init_method != NULL)) {
                            descrgetfunc func = Py_TYPE(init_method)->tp_descr_get;

                            if (func == Nuitka_Function_Type.tp_descr_get) {
                                is_compiled_function = true;
                            } else if (func != NULL) {
                                init_method = func(init_method, obj, (PyObject *)(type));
                                init_method_needs_release = true;
                            }
                        }

                        if (unlikely(init_method == NULL)) {
                            if (!ERROR_OCCURRED()) {
                                SET_CURRENT_EXCEPTION_TYPE0_VALUE0(PyExc_AttributeError, const_str_plain___init__);
                            }

                            return NULL;
                        }

                        PyObject *result;
                        if (is_compiled_function) {
                            result = Nuitka_CallMethodFunctionPosArgs((struct Nuitka_FunctionObject const *)init_method, obj, args, 12);
                        } else {
                            result = CALL_FUNCTION_WITH_ARGS12(init_method, args);
                            if (init_method_needs_release) {
                                Py_DECREF(init_method);
                            }
                        }


                        if (unlikely(result == NULL)) {
                            Py_DECREF(obj);
                            return NULL;
                        }

                        Py_DECREF(result);

                        if (unlikely(result != Py_None)) {
                            Py_DECREF(obj);

                            SET_CURRENT_EXCEPTION_TYPE_COMPLAINT("__init__() should return None, not '%s'", result);
                            return NULL;
                        }
                    } else {
                        if (pos_args == NULL) {
                            pos_args = MAKE_TUPLE(args, 12);
                        }

                        if (unlikely(type->tp_init(obj, pos_args, NULL) < 0)) {
                            Py_DECREF(obj);
                            Py_XDECREF(pos_args);
                            return NULL;
                        }
                    }
                }
            }

            Py_XDECREF(pos_args);
            return obj;
        }
#endif
#if PYTHON_VERSION < 0x300
    } else if (PyClass_Check(called)) {
        PyObject *obj = PyInstance_NewRaw(called, NULL);

        PyObject *init_method = FIND_ATTRIBUTE_IN_CLASS((PyClassObject *)called, const_str_plain___init__);

        if (unlikely(init_method == NULL)) {
            if (unlikely(ERROR_OCCURRED())) {
                Py_DECREF(obj);
                return NULL;
            }

            Py_DECREF(obj);

            SET_CURRENT_EXCEPTION_TYPE0_STR(PyExc_TypeError, "this constructor takes no arguments");
            return NULL;
        }

        bool is_compiled_function = false;

        descrgetfunc descr_get = Py_TYPE(init_method)->tp_descr_get;

        if (descr_get == NULL) {
            Py_INCREF(init_method);
        } else if (descr_get == Nuitka_Function_Type.tp_descr_get) {
            is_compiled_function = true;
        } else if (descr_get != NULL) {
            PyObject *descr_method = descr_get(init_method, obj, called);

            if (unlikely(descr_method == NULL)) {
                return NULL;
            }

            init_method = descr_method;
        }

        PyObject *result;
        if (is_compiled_function) {
            result = Nuitka_CallMethodFunctionPosArgs((struct Nuitka_FunctionObject const *)init_method, obj, args, 12);
        } else {
            result = CALL_FUNCTION_WITH_ARGS12(init_method, args);
            Py_DECREF(init_method);
        }
        if (unlikely(result == NULL)) {
            return NULL;
        }

        Py_DECREF(result);

        if (unlikely(result != Py_None)) {
            SET_CURRENT_EXCEPTION_TYPE_COMPLAINT("__init__() should return None, not '%s'", result);
            return NULL;
        }

        return obj;
#endif
#if PYTHON_VERSION >= 0x380 && !defined(_NUITKA_EXPERIMENTAL_DISABLE_VECTORCALL_USAGE)
    } else if (PyType_HasFeature(Py_TYPE(called), _Py_TPFLAGS_HAVE_VECTORCALL)) {
        vectorcallfunc func = *((vectorcallfunc *)(((char *)called) + Py_TYPE(called)->tp_vectorcall_offset));

        if (likely(func != NULL)) {
            PyObject *result = func(called, args, 12, NULL);

            return Nuitka_CheckFunctionResult(called, result);
        }
#endif
    }

#if 0
    PRINT_NEW_LINE();
    PRINT_STRING("FALLBACK");
    PRINT_ITEM(called);
    PRINT_NEW_LINE();
#endif

    PyObject *pos_args = MAKE_TUPLE(args, 12);

    PyObject *result = CALL_FUNCTION(called, pos_args, NULL);

    Py_DECREF(pos_args);

    return result;
}
PyObject *CALL_FUNCTION_WITH_ARGS13(PyObject *called, PyObject *const *args) {
    CHECK_OBJECT(called);
     CHECK_OBJECTS(args, 13); 

    if (Nuitka_Function_Check(called)) {
        if (unlikely(Py_EnterRecursiveCall((char *)" while calling a Python object"))) {
            return NULL;
        }

        struct Nuitka_FunctionObject *function = (struct Nuitka_FunctionObject *)called;
        PyObject *result;

        if (function->m_args_simple && 13 == function->m_args_positional_count){
            for (Py_ssize_t i = 0; i < 13; i++) {
                Py_INCREF(args[i]);
            }
            result = function->m_c_code(function,  (PyObject **)args );
        } else if (function->m_args_simple && 13 + function->m_defaults_given == function->m_args_positional_count) {
            NUITKA_DYNAMIC_ARRAY_DECL(python_pars, PyObject *, function->m_args_positional_count);

            memcpy(python_pars, args, 13 * sizeof(PyObject *));
            memcpy(python_pars + 13, &PyTuple_GET_ITEM(function->m_defaults, 0), function->m_defaults_given * sizeof(PyObject *));

            for (Py_ssize_t i = 0; i < function->m_args_positional_count; i++) {
                Py_INCREF(python_pars[i]);
            }

            result = function->m_c_code(function, python_pars);
        } else {
            result = Nuitka_CallFunctionPosArgs(function, args, 13);
        }

        Py_LeaveRecursiveCall();

        return result;
    } else if (Nuitka_Method_Check(called)) {
        struct Nuitka_MethodObject *method = (struct Nuitka_MethodObject *)called;

        if (method->m_object == NULL) {
            PyObject *self = args[0];

            int res = PyObject_IsInstance(self, method->m_class);

            if (unlikely(res < 0)) {
                return NULL;
            } else if (unlikely(res == 0)) {
                PyErr_Format(PyExc_TypeError,
                             "unbound compiled_method %s%s must be called with %s instance as first argument (got %s "
                             "instance instead)",
                             GET_CALLABLE_NAME((PyObject *)method->m_function),
                             GET_CALLABLE_DESC((PyObject *)method->m_function), GET_CLASS_NAME(method->m_class),
                             GET_INSTANCE_CLASS_NAME((PyObject *)self));

                return NULL;
            }

            return Nuitka_CallFunctionPosArgs(method->m_function, args, 13);
        } else {
            if (unlikely(Py_EnterRecursiveCall((char *)" while calling a Python object"))) {
                return NULL;
            }

            struct Nuitka_FunctionObject *function = method->m_function;

            PyObject *result;

            if (function->m_args_simple && 13 + 1 == function->m_args_positional_count) {
                PyObject *python_pars[13 + 1];

                python_pars[0] = method->m_object;
                Py_INCREF(method->m_object);

                for (Py_ssize_t i = 0; i < 13; i++) {
                    python_pars[i + 1] = args[i];
                    Py_INCREF(args[i]);
                }
                result = function->m_c_code(function, python_pars);
            } else if (function->m_args_simple && 13 + 1 + function->m_defaults_given == function->m_args_positional_count) {
                NUITKA_DYNAMIC_ARRAY_DECL(python_pars, PyObject *, function->m_args_positional_count);

                python_pars[0] = method->m_object;
                Py_INCREF(method->m_object);

                memcpy(python_pars+1, args, 13 * sizeof(PyObject *));
                memcpy(python_pars+1 + 13, &PyTuple_GET_ITEM(function->m_defaults, 0), function->m_defaults_given * sizeof(PyObject *));

                for (Py_ssize_t i = 1; i < function->m_args_overall_count; i++) {
                    Py_INCREF(python_pars[i]);
                }

                result = function->m_c_code(function, python_pars);
            } else {
                result = Nuitka_CallMethodFunctionPosArgs(function, method->m_object, args, 13);
            }

            Py_LeaveRecursiveCall();

            return result;
        }
#if !defined(_NUITKA_EXPERIMENTAL_DISABLE_CFUNCTION_CALL_OPT)
    } else if (PyCFunction_CheckExact(called)) {
        // Try to be fast about wrapping the arguments.
        int flags = PyCFunction_GET_FLAGS(called) & ~(METH_CLASS | METH_STATIC | METH_COEXIST);

        if (unlikely(flags & METH_NOARGS)) {
            SET_CURRENT_EXCEPTION_TYPE0_FORMAT1(
                PyExc_TypeError,
                "%s() takes no arguments (13 given)",
                ((PyCFunctionObject *)called)->m_ml->ml_name
            );
            return NULL;
        } else if (unlikely(flags & METH_O)) {
            SET_CURRENT_EXCEPTION_TYPE0_FORMAT1(PyExc_TypeError,
                "%s() takes exactly one argument (13 given)",
                 ((PyCFunctionObject *)called)->m_ml->ml_name
            );
            return NULL;
        } else if (flags & METH_VARARGS) {
            // Recursion guard is not strictly necessary, as we already have
            // one on our way to here.
#ifdef _NUITKA_FULL_COMPAT
            if (unlikely(Py_EnterRecursiveCall((char *)" while calling a Python object"))) {
                return NULL;
            }
#endif
            PyCFunction method = PyCFunction_GET_FUNCTION(called);
            PyObject *self = PyCFunction_GET_SELF(called);

            PyObject *result;

#if PYTHON_VERSION < 0x360
            PyObject *pos_args = MAKE_TUPLE(args, 13);
            if (flags & METH_KEYWORDS) {
                result = (*(PyCFunctionWithKeywords)method)(self, pos_args, NULL);
            } else {
                result = (*method)(self, pos_args);
            }

            Py_DECREF(pos_args);
#else
            if (flags == (METH_VARARGS|METH_KEYWORDS)) {
            PyObject *pos_args = MAKE_TUPLE(args, 13);
                result = (*(PyCFunctionWithKeywords)method)(self, pos_args, NULL);
            Py_DECREF(pos_args);
            } else if (flags == METH_FASTCALL) {
#if PYTHON_VERSION < 0x370
                result = (*(_PyCFunctionFast)method)(self, (PyObject **)args, 13, NULL);
#else
            PyObject *pos_args = MAKE_TUPLE(args, 13);
                result = (*(_PyCFunctionFast)method)(self, &pos_args, 13);
            Py_DECREF(pos_args);
#endif
            } else {
            PyObject *pos_args = MAKE_TUPLE(args, 13);
                result = (*method)(self, pos_args);
            Py_DECREF(pos_args);
            }
#endif


#ifdef _NUITKA_FULL_COMPAT
            Py_LeaveRecursiveCall();
#endif

            return Nuitka_CheckFunctionResult(called, result);
        }
#endif
#if !defined(_NUITKA_EXPERIMENTAL_DISABLE_UNCOMPILED_FUNCTION_CALL_OPT)
    } else if (PyFunction_Check(called)) {
#if PYTHON_VERSION < 0x3b0
        return callPythonFunction(
            called,
            args,
            13
        );
#else
    return _PyFunction_Vectorcall(called, args, 13, NULL);
#endif
#endif
#if !defined(_NUITKA_EXPERIMENTAL_DISABLE_TYPE_CREATION_OPT)
    } else if (PyType_Check(called)) {
        PyTypeObject *type = Py_TYPE(called);

        if (type->tp_call == PyType_Type.tp_call) {
            PyTypeObject *called_type = (PyTypeObject *)(called);


            if (unlikely(called_type->tp_new == NULL)) {
                PyErr_Format(PyExc_TypeError, "cannot create '%s' instances", called_type->tp_name);
                return NULL;
            }

            PyObject *pos_args = NULL;
            PyObject *obj;

            if (called_type->tp_new == PyBaseObject_Type.tp_new) {
                if (unlikely(called_type->tp_flags & Py_TPFLAGS_IS_ABSTRACT)) {
                    formatCannotInstantiateAbstractClass(called_type);
                    return NULL;
                }

                obj = called_type->tp_alloc(called_type, 0);
                CHECK_OBJECT(obj);
            } else {
                pos_args = MAKE_TUPLE(args, 13);
                obj = called_type->tp_new(called_type, pos_args, NULL);
            }

            if (likely(obj != NULL)) {
                if (!Nuitka_Type_IsSubtype(obj->ob_type, called_type)) {
                    Py_DECREF(pos_args);
                    return obj;
                }

                // Work on produced type.
                type = Py_TYPE(obj);

                if (NuitkaType_HasFeatureClass(type) && type->tp_init != NULL) {
                    if (type->tp_init == default_tp_init_wrapper) {
                        Py_XDECREF(pos_args);
                        pos_args = NULL;

                        PyObject *init_method = Nuitka_TypeLookup(type, const_str_plain___init__);

                        // Not really allowed, since we wouldn't have the default wrapper set.
                        assert(init_method != NULL);

                        bool is_compiled_function = false;
                        bool init_method_needs_release = false;

                        if (likely(init_method != NULL)) {
                            descrgetfunc func = Py_TYPE(init_method)->tp_descr_get;

                            if (func == Nuitka_Function_Type.tp_descr_get) {
                                is_compiled_function = true;
                            } else if (func != NULL) {
                                init_method = func(init_method, obj, (PyObject *)(type));
                                init_method_needs_release = true;
                            }
                        }

                        if (unlikely(init_method == NULL)) {
                            if (!ERROR_OCCURRED()) {
                                SET_CURRENT_EXCEPTION_TYPE0_VALUE0(PyExc_AttributeError, const_str_plain___init__);
                            }

                            return NULL;
                        }

                        PyObject *result;
                        if (is_compiled_function) {
                            result = Nuitka_CallMethodFunctionPosArgs((struct Nuitka_FunctionObject const *)init_method, obj, args, 13);
                        } else {
                            result = CALL_FUNCTION_WITH_ARGS13(init_method, args);
                            if (init_method_needs_release) {
                                Py_DECREF(init_method);
                            }
                        }


                        if (unlikely(result == NULL)) {
                            Py_DECREF(obj);
                            return NULL;
                        }

                        Py_DECREF(result);

                        if (unlikely(result != Py_None)) {
                            Py_DECREF(obj);

                            SET_CURRENT_EXCEPTION_TYPE_COMPLAINT("__init__() should return None, not '%s'", result);
                            return NULL;
                        }
                    } else {
                        if (pos_args == NULL) {
                            pos_args = MAKE_TUPLE(args, 13);
                        }

                        if (unlikely(type->tp_init(obj, pos_args, NULL) < 0)) {
                            Py_DECREF(obj);
                            Py_XDECREF(pos_args);
                            return NULL;
                        }
                    }
                }
            }

            Py_XDECREF(pos_args);
            return obj;
        }
#endif
#if PYTHON_VERSION < 0x300
    } else if (PyClass_Check(called)) {
        PyObject *obj = PyInstance_NewRaw(called, NULL);

        PyObject *init_method = FIND_ATTRIBUTE_IN_CLASS((PyClassObject *)called, const_str_plain___init__);

        if (unlikely(init_method == NULL)) {
            if (unlikely(ERROR_OCCURRED())) {
                Py_DECREF(obj);
                return NULL;
            }

            Py_DECREF(obj);

            SET_CURRENT_EXCEPTION_TYPE0_STR(PyExc_TypeError, "this constructor takes no arguments");
            return NULL;
        }

        bool is_compiled_function = false;

        descrgetfunc descr_get = Py_TYPE(init_method)->tp_descr_get;

        if (descr_get == NULL) {
            Py_INCREF(init_method);
        } else if (descr_get == Nuitka_Function_Type.tp_descr_get) {
            is_compiled_function = true;
        } else if (descr_get != NULL) {
            PyObject *descr_method = descr_get(init_method, obj, called);

            if (unlikely(descr_method == NULL)) {
                return NULL;
            }

            init_method = descr_method;
        }

        PyObject *result;
        if (is_compiled_function) {
            result = Nuitka_CallMethodFunctionPosArgs((struct Nuitka_FunctionObject const *)init_method, obj, args, 13);
        } else {
            result = CALL_FUNCTION_WITH_ARGS13(init_method, args);
            Py_DECREF(init_method);
        }
        if (unlikely(result == NULL)) {
            return NULL;
        }

        Py_DECREF(result);

        if (unlikely(result != Py_None)) {
            SET_CURRENT_EXCEPTION_TYPE_COMPLAINT("__init__() should return None, not '%s'", result);
            return NULL;
        }

        return obj;
#endif
#if PYTHON_VERSION >= 0x380 && !defined(_NUITKA_EXPERIMENTAL_DISABLE_VECTORCALL_USAGE)
    } else if (PyType_HasFeature(Py_TYPE(called), _Py_TPFLAGS_HAVE_VECTORCALL)) {
        vectorcallfunc func = *((vectorcallfunc *)(((char *)called) + Py_TYPE(called)->tp_vectorcall_offset));

        if (likely(func != NULL)) {
            PyObject *result = func(called, args, 13, NULL);

            return Nuitka_CheckFunctionResult(called, result);
        }
#endif
    }

#if 0
    PRINT_NEW_LINE();
    PRINT_STRING("FALLBACK");
    PRINT_ITEM(called);
    PRINT_NEW_LINE();
#endif

    PyObject *pos_args = MAKE_TUPLE(args, 13);

    PyObject *result = CALL_FUNCTION(called, pos_args, NULL);

    Py_DECREF(pos_args);

    return result;
}
PyObject *CALL_METHOD_WITH_ARGS12(PyObject *source, PyObject *attr_name, PyObject *const *args) {
    CHECK_OBJECT(source);
    CHECK_OBJECT(attr_name);

     CHECK_OBJECTS(args, 12); 

    PyTypeObject *type = Py_TYPE(source);

    if (hasTypeGenericGetAttr(type)) {
        // Unfortunately this is required, although of cause rarely necessary.
        if (unlikely(type->tp_dict == NULL)) {
            if (unlikely(PyType_Ready(type) < 0)) {
                return NULL;
            }
        }

        PyObject *descr = Nuitka_TypeLookup(type, attr_name);
        descrgetfunc func = NULL;

        if (descr != NULL) {
            Py_INCREF(descr);

            if (NuitkaType_HasFeatureClass(Py_TYPE(descr))) {
                func = Py_TYPE(descr)->tp_descr_get;

                if (func != NULL && PyDescr_IsData(descr)) {
                    PyObject *called_object = func(descr, source, (PyObject *)type);
                    Py_DECREF(descr);

                    PyObject *result = CALL_FUNCTION_WITH_ARGS12(called_object, args)
;
                    Py_DECREF(called_object);
                    return result;
                }
            }
        }

        Py_ssize_t dictoffset = type->tp_dictoffset;
        PyObject *dict = NULL;

        if (dictoffset != 0) {
            // Negative dictionary offsets have special meaning.
            if (dictoffset < 0) {
                Py_ssize_t tsize;
                size_t size;

                tsize = ((PyVarObject *)source)->ob_size;
                if (tsize < 0) {
                    tsize = -tsize;
                }
                size = _PyObject_VAR_SIZE(type, tsize);

                dictoffset += (long)size;
            }

            PyObject **dictptr = (PyObject **) ((char *)source + dictoffset);
            dict = *dictptr;
        }

        if (dict != NULL) {
            CHECK_OBJECT(dict);

            Py_INCREF(dict);

            PyObject *called_object = DICT_GET_ITEM1(dict, attr_name);

            if (called_object != NULL) {
                Py_XDECREF(descr);
                Py_DECREF(dict);

                PyObject *result = CALL_FUNCTION_WITH_ARGS12(called_object, args)
;
                Py_DECREF(called_object);
                return result;
            }

            Py_DECREF(dict);
        }

        if (func != NULL) {
            if (func == Nuitka_Function_Type.tp_descr_get) {
                PyObject *result = Nuitka_CallMethodFunctionPosArgs(
                    (struct Nuitka_FunctionObject const *)descr,
                    source,
                    args,
                    12
                );
                Py_DECREF(descr);

                return result;
            } else {
                PyObject *called_object = func(descr, source, (PyObject *)type);
                CHECK_OBJECT(called_object);

                Py_DECREF(descr);

                PyObject *result = CALL_FUNCTION_WITH_ARGS12(called_object, args)
;
                Py_DECREF(called_object);
                return result;
            }
        }

        if (descr != NULL) {
            CHECK_OBJECT(descr);

            PyObject *result = CALL_FUNCTION_WITH_ARGS12(descr, args)
;
            Py_DECREF(descr);
            return result;
        }

#if PYTHON_VERSION < 0x300
        SET_CURRENT_EXCEPTION_TYPE0_FORMAT2(
            PyExc_AttributeError,
            "'%s' object has no attribute '%s'",
            type->tp_name,
            PyString_AS_STRING(attr_name)
        );
#else
        PyErr_Format(
            PyExc_AttributeError,
            "'%s' object has no attribute '%U'",
            type->tp_name,
            attr_name
        );
#endif
        return NULL;
    }
#if PYTHON_VERSION < 0x300
    else if (type == &PyInstance_Type) {
        PyInstanceObject *source_instance = (PyInstanceObject *)source;

        // The special cases have their own variant on the code generation level
        // as we are called with constants only.
        assert(attr_name != const_str_plain___dict__);
        assert(attr_name != const_str_plain___class__);

        // Try the instance dict first.
        PyObject *called_object = GET_STRING_DICT_VALUE(
            (PyDictObject *)source_instance->in_dict,
            (PyStringObject *)attr_name
        );

        // Note: The "called_object" was found without taking a reference,
        // so we need not release it in this branch.
        if (called_object != NULL) {
            return CALL_FUNCTION_WITH_ARGS12(called_object, args)
;
        }

        // Then check the class dictionaries.
        called_object = FIND_ATTRIBUTE_IN_CLASS(
            source_instance->in_class,
            attr_name
        );

        // Note: The "called_object" was found without taking a reference,
        // so we need not release it in this branch.
        if (called_object != NULL) {
            descrgetfunc descr_get = Py_TYPE(called_object)->tp_descr_get;

            if (descr_get == Nuitka_Function_Type.tp_descr_get) {
                return Nuitka_CallMethodFunctionPosArgs(
                    (struct Nuitka_FunctionObject const *)called_object,
                    source,
                    args,
                    12
                );
            } else if (descr_get != NULL) {
                PyObject *method = descr_get(
                    called_object,
                    source,
                    (PyObject *)source_instance->in_class
                );

                if (unlikely(method == NULL)) {
                    return NULL;
                }

                PyObject *result = CALL_FUNCTION_WITH_ARGS12(method, args)
;
                Py_DECREF(method);
                return result;
            } else {
                return CALL_FUNCTION_WITH_ARGS12(called_object, args)
;
            }

        } else if (unlikely(source_instance->in_class->cl_getattr == NULL)) {
            SET_CURRENT_EXCEPTION_TYPE0_FORMAT2(
                PyExc_AttributeError,
                "%s instance has no attribute '%s'",
                PyString_AS_STRING(source_instance->in_class->cl_name),
                PyString_AS_STRING(attr_name)
            );

            return NULL;
        } else {
            // Finally allow the "__getattr__" override to provide it or else
            // it's an error.

            PyObject *args2[] = {
                source,
                attr_name
            };

            called_object = CALL_FUNCTION_WITH_ARGS2(
                source_instance->in_class->cl_getattr,
                args2
            );

            if (unlikely(called_object == NULL)) {
                return NULL;
            }

            PyObject *result = CALL_FUNCTION_WITH_ARGS12(called_object, args)
;
            Py_DECREF(called_object);
            return result;
        }
    }
#endif
    else if (type->tp_getattro != NULL) {
        PyObject *descr = (*type->tp_getattro)(source, attr_name);

        if (unlikely(descr == NULL)) {
            return NULL;
        }

        descrgetfunc func = NULL;
        if (NuitkaType_HasFeatureClass(Py_TYPE(descr))) {
            func = Py_TYPE(descr)->tp_descr_get;

            if (func != NULL && PyDescr_IsData(descr)) {
                PyObject *called_object = func(descr, source, (PyObject *)type);
                Py_DECREF(descr);

                if (unlikely(called_object == NULL))
                {
                    return NULL;
                }

                PyObject *result = CALL_FUNCTION_WITH_ARGS12(called_object, args)
;
                Py_DECREF(called_object);
                return result;
            }
        }

        PyObject *result = CALL_FUNCTION_WITH_ARGS12(descr, args)
;
        Py_DECREF(descr);
        return result;
    } else if (type->tp_getattr != NULL) {
        PyObject *called_object = (*type->tp_getattr)(
            source,
            (char *)Nuitka_String_AsString_Unchecked(attr_name)
        );

        if (unlikely(called_object == NULL)) {
            return NULL;
        }

        PyObject *result = CALL_FUNCTION_WITH_ARGS12(called_object, args)
;
        Py_DECREF(called_object);
        return result;
    } else {
        SET_CURRENT_EXCEPTION_TYPE0_FORMAT2(
            PyExc_AttributeError,
            "'%s' object has no attribute '%s'",
            type->tp_name,
            Nuitka_String_AsString_Unchecked(attr_name)
        );

        return NULL;
    }
}