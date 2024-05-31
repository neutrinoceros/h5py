from typing import Any
import numpy as np

from ._objects import ObjectID

SELECT_NOOP: int
SELECT_SET: int
SELECT_OR: int
SELECT_AND: int
SELECT_XOR: int
SELECT_NOTB: int
SELECT_NOTA: int
SELECT_APPEND: int
SELECT_PREPEND: int
SELECT_INVALID: int

UNLIMITED: int

class SpaceID(ObjectID):
    @property
    def shape(self): ...
    def copy(self) -> SpaceID: ...
    def encode(self) -> str: ...
    def __reduce__(self) -> tuple[type[SpaceID], tuple[Any, ...], str]: ...
    def __setstate__(self, state) -> None: ...
    def is_simple(self) -> bool: ...
    def offset_simple(self, offset: tuple[int, ...] | None = None) -> None: ...
    def get_simple_extent_ndims(self) -> int: ...
    def get_simple_extent_dims(self, maxdims: int = 0): ...
    def get_simple_extent_npoints(self) -> int: ...
    def get_simple_extent_type(self) -> int: ...
    def extent_copy(self, source: SpaceID) -> None: ...
    def set_extent_simple(self, dims_tpl, max_dims_tpl=None) -> None: ...
    def set_extent_none(self) -> None: ...
    def get_select_type(self) -> int: ...
    def get_select_npoints(self) -> int: ...
    def get_select_bounds(self): ...
    def select_all(self) -> None: ...
    def select_none(self) -> None: ...
    def select_valid(self) -> bool: ...
    def get_select_elem_npoints(self) -> int: ...
    def get_select_elem_pointlist(self) -> np.ndarray: ...
    def select_elements(self, coords, op: int = SELECT_SET) -> None: ...
    def get_select_hyper_nblocks(self) -> int: ...
    def get_select_hyper_blocklist(self) -> np.ndarray: ...
    def select_hyperslab(
        self,
        start,
        count,
        stride=None,
        block=None,
        op: int = SELECT_SET,
    ) -> None: ...
    def is_regular_hyperslab(self) -> bool: ...
    def get_regular_hyperslab(
        self,
    ) -> tuple[tuple[int], tuple[int], tuple[int], tuple[int]]: ...
