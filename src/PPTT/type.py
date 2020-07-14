from typing import TypedDict, List, TypeVar, Dict, Union, Optional


class DataType(TypedDict):
    data_type: str


Text = TypeVar('Text', int, str)
Number = TypeVar('Number', float, int)


class KVKeyType(TypedDict):
    name: Text
    data_key: Text


KVKeys = List[Union[Text, KVKeyType]]


class KeyValueDataType(DataType):
    keys: KVKeys
    data: List[Dict[Text, Text]]


class RawDataType(DataType):
    data: List[List[Text]]


class ChartDataType(DataType):
    title: Text


class CategoryDataType(ChartDataType):
    number_format: Optional[str]
    categories: List[Text]
    series: Dict[Text, List[int]]


class XYPoint(TypedDict):
    y: Number
    x: Number


class XYDataType(ChartDataType):
    number_format: Optional[str]
    series: Dict[Text, List[XYPoint]]


class BubblePoint(XYPoint):
    size: Number


class BubbleDataType(ChartDataType):
    number_format: Optional[str]
    series: Dict[Text, List[BubblePoint]]


ChartDataTypes = Union[CategoryDataType, BubbleDataType, XYDataType]


class InputDataType(TypedDict):
    delete_pages: Optional[List[int]]
    pages: List[dict]
