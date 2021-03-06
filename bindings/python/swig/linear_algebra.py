# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.7
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _linear_algebra.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_linear_algebra', [dirname(__file__)])
        except ImportError:
            import _linear_algebra
            return _linear_algebra
        if fp is not None:
            try:
                _mod = imp.load_module('_linear_algebra', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _linear_algebra = swig_import_helper()
    del swig_import_helper
else:
    import _linear_algebra
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        object.__setattr__(self, name, value)
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0



def _swig_setattr_nondynamic_method(set):
    def set_attr(self, name, value):
        if (name == "thisown"):
            return self.this.own(value)
        if hasattr(self, name) or (name == "this"):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr


try:
    import weakref
    weakref_proxy = weakref.proxy
except:
    weakref_proxy = lambda x: x



_linear_algebra.SHARED_PTR_DISOWN_swigconstant(_linear_algebra)
SHARED_PTR_DISOWN = _linear_algebra.SHARED_PTR_DISOWN

def _new_from_init(cls, version, *args):
    '''For use with pickle, covers common case where we just store the
    arguments needed to create an object. See for example HdfFile'''
    if(cls.pickle_format_version() != version):
      raise RuntimeException("Class is expecting a pickled object with version number %d, but we found %d" % (cls.pickle_format_version(), version))
    inst = cls.__new__(cls)
    inst.__init__(*args)
    return inst

def _new_from_set(cls, version, *args):
    '''For use with pickle, covers common case where we use a set function 
    to assign the value'''
    if(cls.pickle_format_version() != version):
      raise RuntimeException("Class is expecting a pickled object with version number %d, but we found %d" % (cls.pickle_format_version(), version))
    inst = cls.__new__(cls)
    inst.__init__()
    inst.set(*args)
    return inst


def solve_least_squares(A, B, Rcond=1e-12):
    """

    Array< double, 1 > FullPhysics::solve_least_squares(const blitz::Array< double, 2 > &A, const blitz::Array< double, 1 >
    &B, double Rcond=1e-12)
    This solves the least squares system A*x = b, returning the minimum
    norm solution.

    It is perfectly ok for A to be rank deficient.

    Parameters:
    -----------

    A:  a M x N matrix, which may be rank deficient.

    B:  the right hand side, a M vector

    Rcond:  a singular value <= Rcond * max singular value is treated as
    0. You can pass Rcond < 0 to use machine precision if desired.

    The vector X, which is a N vector 
    """
    return _linear_algebra.solve_least_squares(A, B, Rcond)

def svd(A, S, U, VT):
    """

    void FullPhysics::svd(const blitz::Array< double, 2 > &A, blitz::Array< double, 1 > &S,
    blitz::Array< double, 2 > &U, blitz::Array< double, 2 > &VT)
    Compute the SVD decomposition of a matrix A = U * SIGMA * V^T.

    Parameters:
    -----------

    A:  Matrix to get decomposition for.

    S:  On exit, Singular values

    U:  On exit, U matrix. Note that this is the "thin" version of U,
    this is M x N rather than M x M. The "full" version would just have
    extra columns of zeros.

    VT:  On exit, V^T matrix 
    """
    return _linear_algebra.svd(A, S, U, VT)

def generalized_inverse(*args):
    """

    Array< double, 2 > FullPhysics::generalized_inverse(const blitz::Array< double, 2 > &A, const blitz::Array< bool, 1 >
    &Zero_unused, double Rcond=std::numeric_limits< double >::epsilon())
    This returns the generalized inverse of the given matrix.

    This is the same as the inverse, except that if A is rank deficient we
    set the SVD value to 0.

    This variation takes a boolean array indicating which parameters are
    to be held at zero.

    Parameters:
    -----------

    A:  Matrix to get inverse of

    Zero_unused:  Boolean array indicating parameters that are unused and
    should be held to zero

    Rcond:  We set singular values < Rcond * max singular value to 0. 
    """
    return _linear_algebra.generalized_inverse(*args)

def solve_least_squares_qr(A, B):
    """

    Array< double, 1 > FullPhysics::solve_least_squares_qr(const blitz::Array< double, 2 > &A, const blitz::Array< double, 1 >
    &B)
    This finds the least squares solution to the overdetermined system A x
    = b where the matrix A has more rows than columns.

    The least squares solution minimizes the Euclidean norm of the
    residual, ||Ax - b||. The solution is determined using a QR
    decomposition of A.

    Parameters:
    -----------

    A:  a M x N matrix, which may be rank deficient.

    B:  the right hand side, a M vector

    The vector X, which is a N vector 
    """
    return _linear_algebra.solve_least_squares_qr(A, B)


