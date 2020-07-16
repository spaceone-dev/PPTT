from dataclasses import dataclass, field
from typing import Optional
from PPTT.type import (
    SlideData,
    TextData,
    ChartCategoryData,
    ChartBubbleData,
    ChartXYData,
    TableData,
)


@dataclass
class Slide1Content():
    title: Optional[TextData] = field(default=None)
    subtitle: Optional[TextData] = field(default=None)


@dataclass
class Slide1(SlideData):
    contents: Optional[Slide1Content] = field(default=None)
    slide_pos: int = 1


@dataclass
class Slide2Content():
    title: Optional[TextData] = field(default=None)
    table: Optional[TableData] = field(default=None)


@dataclass
class Slide2(SlideData):
    contents: Optional[Slide2Content] = field(default=None)
    slide_pos: int = 2


@dataclass
class Slide3Content():
    title: Optional[TextData] = field(default=None)
    chart: Optional[ChartCategoryData] = field(default=None)


@dataclass
class Slide3(SlideData):
    contents: Optional[Slide3Content] = field(default=None)
    slide_pos: int = 3


@dataclass
class Slide4Content():
    text_bg: Optional[TextData] = field(default=None)
    chart: Optional[ChartCategoryData] = field(default=None)
    table: Optional[TableData] = field(default=None)
    body: Optional[TextData] = field(default=None)


@dataclass
class Slide4(SlideData):
    contents: Optional[Slide4Content] = field(default=None)
    slide_pos: int = 4


@dataclass
class Slide5Content():
    title: Optional[TextData] = field(default=None)


@dataclass
class Slide5(SlideData):
    contents: Optional[Slide5Content] = field(default=None)
    slide_pos: int = 5


@dataclass
class Slide6Content():
    title: Optional[TextData] = field(default=None)


@dataclass
class Slide6(SlideData):
    contents: Optional[Slide6Content] = field(default=None)
    slide_pos: int = 6
SLIDES = [Slide1, Slide2, Slide3, Slide4, Slide5, Slide6]
