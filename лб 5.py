class ProtectedDictInt
    d= ProtectedDictInt()
    dd = {}


    Class Rational:
    def __init__(self,n,d):
        self._n = n
        self._d = d

        def __str__(self):
            return str(self._n)+'/'+str(self._d)
        def __call__(self):
            return self._n/self._d

