def sizer(cls):
    class SizedClass(cls):
        @property
        def size(self):
            if hasattr(self, "__len__"):
                return len(self)
            elif hasattr(self, "__abs__"):
                return abs(self)
            else:
                return 0

    return SizedClass


def sizer(cls):
    class SizedClass(cls):
        @property
        def size(self):
            if hasattr(self, "__len__"):
                return len(self)
            elif hasattr(self, "__abs__"):
                return abs(self)
            else:
                return 0

    return SizedClass

