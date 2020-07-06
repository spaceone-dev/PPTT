from marshmallow import fields

from PPTT.schema import SlideStub


class TitleSlide(SlideStub):
    title = fields.Str()
    subtitle = fields.Str()
    date = fields.Str()


class ChartInit(SlideStub):
    _slide_layout_name = 'asb'
    title = fields.Str()
    chart = fields.Str()
    text = fields.Str()


SLIDES = {
    "title slide": TitleSlide,
    "chart init": ChartInit
}
