from marshmallow import Schema, fields
from pptx.presentation import Presentation
from pptx.shapes.base import BaseShape
from pptx.slide import SlideMaster, SlideLayout


class ShapeSchema(Schema):
    name = fields.Str(required=True)
    is_placeholder = fields.Bool()
    type = fields.Str()

    @classmethod
    def load_by_pptx(cls, _sh: BaseShape):
        sh = cls()
        sh.name = _sh.name
        sh.is_placeholder = _sh.is_placeholder
        if _sh.has_table:
            sh.type = 'table'
        elif _sh.has_chart:
            sh.type = 'chart'
        elif _sh.has_text_frame:
            sh.type = 'text'
        return sh


class SlideLayoutSchema(Schema):
    name = fields.Str(required=True)
    shapes = fields.List(fields.Nested(ShapeSchema))

    @classmethod
    def load_by_pptx(cls, _sl: SlideLayout):
        sl = cls()
        sl.name = _sl.name
        sl.shapes = [ShapeSchema.load_by_pptx(sh) for sh in _sl.shapes]
        return sl


class SlideMasterSchema(Schema):
    name = fields.Str(required=True)
    main = fields.Bool(default=True)
    slides = fields.List(fields.Nested(SlideLayoutSchema))

    @classmethod
    def load_by_pptx(cls, _sm: SlideMaster, main=True):
        sm = cls()
        sm.name = _sm.name
        sm.main = main
        sm.slides = [SlideLayoutSchema.load_by_pptx(sl) for sl in _sm.slide_layouts]
        return sm


class PPTTemplate(Schema):
    main = fields.Str()
    masters = fields.List(fields.Nested(SlideMasterSchema))

    @classmethod
    def load_by_pptx(cls, _ppt: Presentation):
        ppt = cls()
        ppt.name = _ppt.slide_master.name
        ppt.masters = [SlideMasterSchema.load_by_pptx(sm, sm.name == ppt.name) for sm in _ppt.slide_masters]
        return ppt
