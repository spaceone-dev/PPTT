import ast
from ast import Module, ImportFrom, ClassDef, alias, Load, Name, Call, Attribute, Store, Assign, Dict, Constant

from ast_decompiler import decompile

clone = Module(
    body=[
        ImportFrom(module='marshmallow', names=[alias(name='fields', asname=None)], level=0),
        ImportFrom(module='PPTT.schema', names=[alias(name='SlideStub', asname=None)], level=0),
        ClassDef(
            name='TitleSlide',
            bases=[Name(id='SlideStub', ctx=Load())],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='title', ctx=Store())],
                    value=Call(func=Attribute(value=Name(id='fields', ctx=Load()), attr='Str', ctx=Load()),
                               args=[],
                               keywords=[]),
                    type_comment=None),
                Assign(
                    targets=[Name(id='subtitle', ctx=Store())],
                    value=Call(func=Attribute(
                        value=Name(id='fields', ctx=Load()),
                        attr='Str', ctx=Load()), args=[],
                        keywords=[]), type_comment=None),
                Assign(targets=[Name(id='date', ctx=Store())],
                       value=Call(func=Attribute(value=Name(id='fields', ctx=Load()), attr='Str', ctx=Load()), args=[],
                                  keywords=[]), type_comment=None)], decorator_list=[]),
        ClassDef(
            name='ChartInit',
            bases=[Name(id='SlideStub', ctx=Load())],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='title', ctx=Store())],
                    value=Call(func=Attribute(value=Name(id='fields', ctx=Load()), attr='Str', ctx=Load()), args=[],
                               keywords=[]), type_comment=None),
                Assign(targets=[Name(id='chart', ctx=Store())],
                       value=Call(func=Attribute(
                           value=Name(id='fields', ctx=Load()),
                           attr='Str', ctx=Load()), args=[],
                           keywords=[]), type_comment=None),
                Assign(targets=[Name(id='text', ctx=Store())],
                       value=Call(func=Attribute(value=Name(id='fields', ctx=Load()), attr='Str', ctx=Load()), args=[],
                                  keywords=[]), type_comment=None)], decorator_list=[]),

    ],
    type_ignores=[]
)

Module(body=[
    ImportFrom(module='marshmallow', names=[alias(name='fields', asname=None)], level=0),
    ImportFrom(module='PPTT.schema', names=[alias(name='SlideStub', asname=None)], level=0),
    ClassDef(name='TitleSlide', bases=[Name(id='SlideStub', ctx=Load())], keywords=[], body=[
        Assign(targets=[Name(id='title', ctx=Store())],
               value=Call(func=Attribute(value=Name(id='fields', ctx=Load()), attr='Str', ctx=Load()), args=[],
                          keywords=[]), type_comment=None), Assign(targets=[Name(id='subtitle', ctx=Store())],
                                                                   value=Call(func=Attribute(
                                                                       value=Name(id='fields', ctx=Load()),
                                                                       attr='Str', ctx=Load()), args=[],
                                                                       keywords=[]), type_comment=None),
        Assign(targets=[Name(id='date', ctx=Store())],
               value=Call(func=Attribute(value=Name(id='fields', ctx=Load()), attr='Str', ctx=Load()), args=[],
                          keywords=[]), type_comment=None)], decorator_list=[]),
    ClassDef(name='ChartInit', bases=[Name(id='SlideStub', ctx=Load())], keywords=[], body=[
        Assign(
            targets=[Name(id='title', ctx=Store())],
            value=Call(
                func=Attribute(value=Name(id='fields', ctx=Load()), attr='Str', ctx=Load()), args=[], keywords=[]),
            type_comment=None),
        Assign(
            targets=[Name(id='chart', ctx=Store())],
            value=Call(func=Attribute(
                value=Name(id='fields', ctx=Load()),
                attr='Str', ctx=Load()), args=[],
                keywords=[]),
            type_comment=None),
        Assign(
            targets=[Name(id='text', ctx=Store())],
            value=Call(func=Attribute(value=Name(id='fields', ctx=Load()), attr='Str', ctx=Load()), args=[],
                       keywords=[]), type_comment=None)], decorator_list=[]),
    Assign(
        targets=[Name(id='SLIDES', ctx=Store())],
        value=Dict(keys=[Constant(value='title slide', kind=None), Constant(value='chart init', kind=None)],
                   values=[Name(id='TitleSlide', ctx=Load()), Name(id='ChartInit', ctx=Load())]),
        type_comment=None)], type_ignores=[])

if __name__ == '__main__':
    target = '/Users/mzc01-sinsky/code/PPTT/sutb_sample.py'
    with open(target, mode='r') as fp:
        data = fp.read()
    at = ast.parse(data)
    print(ast.dump(at))

    print(decompile(at))
