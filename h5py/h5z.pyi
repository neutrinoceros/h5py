FILTER_LZF: int

CLASS_T_VERS: int
FILTER_ERROR: int
FILTER_NONE: int
FILTER_ALL: int
FILTER_DEFLATE: int
FILTER_SHUFFLE: int
FILTER_FLETCHER32: int
FILTER_SZIP: int
FILTER_NBIT: int
FILTER_SCALEOFFSET: int
FILTER_RESERVED: int
FILTER_MAX: int
MAX_NFILTERS: int

FLAG_DEFMASK: int
FLAG_MANDATORY: int
FLAG_OPTIONAL: int

FLAG_INVMASK: int
FLAG_REVERSE: int
FLAG_SKIP_EDC: int

def filter_avail(filter_code: int) -> bool: ...
def _register_lzf() -> None: ...
