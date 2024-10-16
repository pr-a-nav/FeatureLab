from typing import Dict, Optional
import typing
import pandas as pd
import typing
# import pyspark


class Feature:
  
    def __init__(
        self,
        name: Optional[str],
        dtype: typing.Optional[any],
        description: str = "",
        labels: Optional[Dict[str, str]] = None,
    ):
        pass

    def __eq__(self, other):
        if self.name != other.name or self.dtype != other.dtype:
            return False
        return True

    def __lt__(self, other):
        return self.name < other.name

    def __repr__(self):
        return f"{self.name}-{self.dtype}"

    def __str__(self):
        return f"Feature<{self.__repr__()}>"

    @property
    def name(self):
        return self._name

    @property
    def dtype(self) :
      return self._dtype

    @property
    def description(self) -> str:
        return self._description

    @property
    def labels(self) -> Dict[str, str]:
        return self._labels
    
    def detect_new_feature(self, df: pd.DataFrame, orig:list):
         curr = df.columns.to_list()
         fnew =[i for i in curr if i not in orig]
         print(fnew)
         return fnew
    
    
class Field:

    def __init__(
        self,
        *,
        name: str,
        dtype: typing.Any,
        description: str = "",
        tags: Optional[Dict[str, str]] = None,
    ):
        """
        Creates a Field object.

        Args:
            name: The name of the field.
            dtype: The type of the field, such as string or float.
            description (optional): A human-readable description.
            tags (optional): User-defined metadata in dictionary form.
        """
        self.name = name
        self.dtype = dtype
        self.description = description
        self.tags = tags or {}

    def __eq__(self, other):
        if type(self) != type(other):
            return False

        if (
            self.name != other.name
            or self.dtype != other.dtype
            or self.description != other.description
            or self.tags != other.tags
        ):
            return False
        return True

    def __hash__(self):
        return hash((self.name, hash(self.dtype)))

    def __lt__(self, other):
        return self.name < other.name

    def __repr__(self):
        return f"{self.name}-{self.dtype}"

    def __str__(self):
        return f"Field(name={self.name}, dtype={self.dtype}, tags={self.tags})"