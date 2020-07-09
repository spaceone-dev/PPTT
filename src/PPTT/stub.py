from ast import ImportFrom, alias, Module, Name, Load, Assign, Store, Dict, Constant, ClassDef, Attribute, Call
from dataclasses import dataclass
from functools import partial
from typing import List as ListType, Tuple as TupleType, Any as AnyType

from ast_decompiler import decompile
from marshmallow import fields
from slugify import slugify

from .schema import SlideLayoutSchema, PPTTemplate, SlideMasterSchema, ShapeSchema
from .utils import name_to_slugify


class ShapeStub(ShapeSchema):

    def to_ast(self):
        make_ast = partial(Assign, targets=[Name(id=name_to_slugify(self.name), ctx=Store())], )
        if self.type == 'text':
            return make_ast(value=Call(
                func=Attribute(value=Name(id='fields', ctx=Load()), attr='Str', ctx=Load()),
                args=[],
                keywords=[]),
                type_comment=None)
            pass
        elif not self.is_placeholder:
            if self.type == 'chart':
                pass
            elif self.type == 'table':
                pass


class SlideLayoutStub(SlideLayoutSchema):
    shape_schema_class = ShapeStub

    shapes: ListType[ShapeStub] = fields.List(fields.Nested(ShapeStub))

    def to_ast(self, master_name: str, is_main: bool) -> TupleType[str, str, AnyType]:
        prefix = f"{master_name}_"
        slug_name = slugify(self.name, separator='_')

        slug_name = slug_name if is_main else f"{prefix}{slug_name}"
        slide_layout_name = Assign(targets=[Name(id='_slide_layout_name', ctx=Store())],
                                   value=Constant(value=self.name, kind=None),
                                   type_comment=None)
        shape_asts = [slide_layout_name] + [shape.to_ast() for shape in self.shapes]
        # remove None data
        shape_asts = [at for at in shape_asts if at]
        sl_ast = ClassDef(
            name=slug_name,
            bases=[Name(id='SlideStub', ctx=Load())],
            keywords=[],
            body=shape_asts,
            decorator_list=[]
        )
        return self.name, slug_name, sl_ast


@dataclass
class MasterAstInfo:
    asts: list
    slug_name: str
    origin_slide_names: ListType[str]
    slugify_slide_names: ListType[str]


class SlideMasterStub(SlideMasterSchema):
    slide_layout_class = SlideLayoutStub

    slides: ListType[SlideLayoutStub] = fields.List(fields.Nested(SlideLayoutStub))

    def to_ast(self) -> MasterAstInfo:
        slug_name = slugify(self.name, separator='_').upper()
        asts = []
        slugify_slide_names = []
        origin_slide_names = []

        for sl_name, sl_slug_name, sl_ast in (sl.to_ast(slug_name, self.main) for sl in self.slides):
            origin_slide_names.append(sl_name)
            slugify_slide_names.append(sl_slug_name)
            asts.append(sl_ast)

        return MasterAstInfo(
            asts=asts,
            slug_name=slug_name,
            origin_slide_names=origin_slide_names,
            slugify_slide_names=slugify_slide_names
        )


class PPTTemplateStub(PPTTemplate):
    slide_master_class = SlideMasterStub
    masters: ListType[SlideMasterStub] = fields.List(fields.Nested(SlideMasterStub))

    def to_ast(self):
        pre_body = [
            ImportFrom(module='marshmallow', names=[alias(name='fields', asname=None)], level=0),
            ImportFrom(module='PPTT.schema', names=[alias(name='SlideStub', asname=None)], level=0),
        ]

        slide_stubs = []
        master_maps = []
        for idx, master in enumerate(self.masters):
            master_ast_info = master.to_ast()
            slide_stubs += master_ast_info.asts
            make_dict = partial(
                Assign,
                value=Dict(
                    keys=[Constant(value=name, kind=None) for name in master_ast_info.origin_slide_names],
                    values=[Name(id=sl_name, ctx=Load()) for sl_name in master_ast_info.slugify_slide_names]),
                type_comment=None)
            if idx == 0:
                master_maps.append(make_dict(targets=[Name(id='MAIN_SLIDES', ctx=Store())], ))
            master_maps.append(make_dict(targets=[Name(id=f"{master_ast_info.slug_name}_SLIDES", ctx=Store())], ))

        return Module(body=[*pre_body, *slide_stubs, *master_maps])

    def to_str(self):
        return decompile(self.to_ast())

    def to_file(self, path):
        with open(path, mode='w') as fp:
            fp.write(self.to_str())
