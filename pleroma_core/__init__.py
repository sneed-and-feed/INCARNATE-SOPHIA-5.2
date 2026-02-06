# pleroma_core package initialization
try:
    # This assumes the binary extension is named _pleroma_core or similar, 
    # or that the symbols are exported via the shared library.
    # For Maturin, it often produces a single module.
    from .pleroma_core import *
except ImportError:
    pass
