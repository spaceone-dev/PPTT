from typing import TypedDict, List, TypeVar, Dict, Union, Optional


class DataType(TypedDict):
    data_type: str


Text = TypeVar('Text', int, str)


class KVKeyType(TypedDict):
    name: Text
    data_key: Text


KVKeys = List[Union[Text, KVKeyType]]


class KeyValueDataType(DataType):
    keys: KVKeys
    data: List[Dict[Text, Text]]


class ChartDataType(DataType):
    title: Text


class CategoryDataType(ChartDataType):
    number_format: Optional[str]
    categories: List[Text]
    series: Dict[Text, List[int]]


ChartDataTypes = Union[CategoryDataType]


class InputDataType(TypedDict):
    delete_pages: Optional[List[int]]
    pages: List[dict]
