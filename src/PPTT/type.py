from copy import deepcopy
from dataclasses import dataclass, asdict, field
from typing import List, Dict, Union, Optional

from dacite import from_dict


@dataclass
class BaseSchema:
    @classmethod
    def from_dict(cls, data, **kwargs):
        return from_dict(data_class=cls, data=data, **kwargs)

    def to_dict(self):
        return asdict(self)


@dataclass
class DataType(BaseSchema):
    data_type: str = field(init=False, default='')


Text = Union[int, str, float]
Number = Union[int, float]


@dataclass
class FontData(BaseSchema):
    color: Optional[str]
    bold: Optional[bool]
    italic: Optional[bool]
    underline: Optional[bool]


@dataclass
class TextStyle(BaseSchema):
    value: Text
    font: Optional[FontData]


TextFrameDataType = Union[int, str, float, TextStyle]


@dataclass
class KVKey(BaseSchema):
    name: TextFrameDataType
    data_key: Text


KVKeys = List[Union[int, str, float, KVKey]]


@dataclass
class KeyValueData(DataType):
    keys: KVKeys = field(default_factory=[])
    data: List[Dict[Text, TextFrameDataType]] = field(default_factory=[])

    def __post_init__(self):
        self.data_type = 'key_value'

    @classmethod
    def from_dict(cls, data, **kwargs):
        change_data = deepcopy(data)
        keys = change_data['keys']
        change_data['keys'] = [KVKey.from_dict(k) if isinstance(k, dict) else k for k in keys]
        return from_dict(data_class=cls, data=change_data, **kwargs)


@dataclass
class RawData(DataType):
    data: List[List[TextFrameDataType]]

    def __post_init__(self):
        self.data_type = 'raw'


TableDataTypeMap = {
    "raw": RawData,
    "key_value": KeyValueData
}
TableDataTypeHint = Union[RawData, KeyValueData]


@dataclass
class ChartDataType(DataType):
    title: Optional[Text]


@dataclass
class CategoryData(ChartDataType):
    number_format: Optional[str]
    categories: List[Text] = field(default_factory=list)
    series: Dict[Text, List[int]] = field(default_factory=dict)

    def __post_init__(self):
        self.data_type = 'category_data'


@dataclass
class XYPoint(BaseSchema):
    y: Number
    x: Number


@dataclass
class XYData(ChartDataType):
    number_format: Optional[str]
    series: Dict[Text, List[XYPoint]]

    def __post_init__(self):
        self.data_type = 'xy_data'


@dataclass
class BubblePoint(XYPoint):
    size: Number


@dataclass
class BubbleData(ChartDataType):
    number_format: Optional[str]
    series: Dict[Text, List[BubblePoint]]

    def __post_init__(self):
        self.data_type = 'bubble_data'


ChartDataTypeMap = {
    "bubble_data": BubbleData,
    "xy_data": XYData,
    "category_data": CategoryData,

}

ChartDataTypeHints = Union[CategoryData, BubbleData, XYData]


@dataclass
class ChartData(BaseSchema):
    chart: ChartDataTypeHints

    @classmethod
    def from_dict(cls, data, **kwargs):
        change_data = deepcopy(data)
        chart = change_data['chart']
        change_data['chart'] = ChartDataTypeMap[chart['data_type']].from_dict(chart)
        return from_dict(data_class=cls, data=change_data, **kwargs)


@dataclass
class TextData(BaseSchema):
    text: TextFrameDataType


@dataclass
class TableData(BaseSchema):
    table: TableDataTypeHint

    @classmethod
    def from_dict(cls, data, **kwargs):
        change_data = deepcopy(data)
        table = change_data['table']
        change_data['table'] = TableDataTypeMap[table['data_type']].from_dict(table)
        return from_dict(data_class=cls, data=change_data, **kwargs)


@dataclass
class SlideData(BaseSchema):
    slide_pos: int


SlideContentsType = Dict[str, Union[TextData, ChartData, TableData]]
ContentTypeMap = {
    "text": TextData,
    "table": TableData,
    "chart": ChartData,

}


@dataclass
class ReplaceSlideType(SlideData):
    slide_pos: int
    contents: SlideContentsType

    @classmethod
    def from_dict(cls, data, **kwargs):
        change_data = deepcopy(data)
        origin_contents = data.get('contents')
        contents = {}
        for key, content in origin_contents.items():
            for field_name in content.keys():
                if field_name in ContentTypeMap:
                    contents[key] = ContentTypeMap[field_name].from_dict(content)
                    break

        change_data['contents'] = contents
        return from_dict(data_class=cls, data=change_data, **kwargs)


@dataclass
class InputData(BaseSchema):
    delete_pages: Optional[List[int]]


@dataclass
class ReplaceInputData(InputData):
    pages: List[ReplaceSlideType]

    @classmethod
    def from_dict(cls, data, **kwargs):
        change_data = deepcopy(data)
        origin_pages = change_data.get('pages', [])
        page_objs = []
        for page in origin_pages:
            page_objs.append(ReplaceSlideType.from_dict(page))
        change_data['pages'] = page_objs
        return from_dict(data_class=cls, data=change_data, **kwargs)
