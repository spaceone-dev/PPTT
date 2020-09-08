from dataclasses import dataclass, field
from typing import Optional

from PPTT.type import SlideData, TextData, ChartData, TableData


@dataclass
class Slide1Content:
    title: Optional[TextData] = field(default=None)
    subtitle: Optional[TextData] = field(default=None)
    date: Optional[TextData] = field(default=None)


@dataclass
class Slide1(SlideData):
    contents: Optional[Slide1Content]
    slide_pos: int = 1


@dataclass
class Slide2Content:
    title: Optional[TextData]
    chart: Optional[ChartData]
    table: Optional[TableData]


@dataclass
class Slide2(SlideData):
    slide_pos = 2
    contents: Optional[Slide2Content]


class EC2Slide2(Slide2):
    pass

class EC2Slide2Content(Slide2Content):
    pass

SLIDES = [Slide1, Slide2]
