from .base import *  # NOOA

try:
    from .local import *  # NOOA
except ImportError:
    import warnings
    warnings.warn('No local settings module found.')