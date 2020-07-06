from marshmallow import fields
from PPTT.schema import SlideStub


class title_slide(SlideStub):
    _slide_layout_name = 'title_slide'
    title = fields.Str()
    subtitle = fields.Str()
    date = fields.Str()


class table_slide(SlideStub):
    _slide_layout_name = 'table_slide'
    title = fields.Str()
    date = fields.Str()
    footer = fields.Str()
    page_number = fields.Str()


class chart_slide(SlideStub):
    _slide_layout_name = 'chart_slide'
    page_number = fields.Str()
    title = fields.Str()
    text = fields.Str()
MAIN_SLIDES = {'title_slide': title_slide, 'table_slide': table_slide, 'chart_slide': chart_slide}
_SLIDES = {'title_slide': title_slide, 'table_slide': table_slide, 'chart_slide': chart_slide}
