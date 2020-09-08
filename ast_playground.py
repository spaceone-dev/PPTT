import ast
import os
from ast import AnnAssign, Assign, ClassDef, Constant, ImportFrom, Index, List, Load, Module, Name, Store, Subscript, \
    alias

from ast_decompiler import decompile

dataclass_decorator = Name(id='dataclass', ctx=Load())
text_data_value = Subscript(
    value=Name(id='Optional', ctx=Load()),
    slice=Index(value=Name(id='TextData', ctx=Load())),
    ctx=Load()
)
chart_xy_data_value = Subscript(
    value=Name(id='Optional', ctx=Load()),
    slice=Index(value=Name(id='ChartXYData', ctx=Load())),
    ctx=Load()
)
chart_category_data_value = Subscript(
    value=Name(id='Optional', ctx=Load()),
    slice=Index(value=Name(id='ChartCategoryData', ctx=Load())),
    ctx=Load()
)
chart_bubble_data_value = Subscript(
    value=Name(id='Optional', ctx=Load()),
    slice=Index(value=Name(id='ChartBubbleData', ctx=Load())),
    ctx=Load()
)
table_data_value = Subscript(
    value=Name(id='Optional', ctx=Load()),
    slice=Index(value=Name(id='TableData', ctx=Load())),
    ctx=Load()
)
clone = Module(
    body=[
        ImportFrom(module='dataclasses', names=[alias(name='dataclass', asname=None)], level=0),
        ImportFrom(module='typing', names=[alias(name='Optional', asname=None)], level=0),
        ImportFrom(module='PPTT.type',
                   names=[
                       alias(name='SlideData', asname=None),
                       alias(name='TextData', asname=None),
                       alias(name='ChartCategoryData', asname=None),
                       alias(name='ChartBubbleData', asname=None),
                       alias(name='ChartXYData', asname=None),
                       alias(name='TableData', asname=None),
                   ],
                   level=0),
        ClassDef(
            name='Slide1Content',
            bases=[], keywords=[],
            body=[
                Assign(
                    targets=[Name(id='title', ctx=Store())],
                    value=text_data_value,
                    type_comment=None),
                Assign(
                    targets=[Name(id='subtitle', ctx=Store())],
                    value=text_data_value,
                    type_comment=None),
                Assign(
                    targets=[Name(id='date', ctx=Store())],
                    value=text_data_value,
                    type_comment=None)
            ],
            decorator_list=[dataclass_decorator]
        ),
        ClassDef(
            name='Slide1',
            bases=[Name(id='SlideData', ctx=Load())],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='slide_pos', ctx=Store())],
                    value=Constant(value=1, kind=None),
                    type_comment=None
                ),
                AnnAssign(
                    target=Name(id='contents', ctx=Store()),
                    annotation=Subscript(
                        value=Name(id='Optional', ctx=Load()),
                        slice=Index(value=Name(id='Slide1Content', ctx=Load())),
                        ctx=Load()
                    ),
                    value=None,
                    simple=1)
            ],
            decorator_list=[dataclass_decorator]),
        ClassDef(
            name='Slide2Content',
            bases=[],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='title', ctx=Store())],
                    value=text_data_value,
                    type_comment=None
                ),
                Assign(
                    targets=[Name(id='chart', ctx=Store())],
                    value=chart_xy_data_value,
                    type_comment=None
                ),
                Assign(
                    targets=[Name(id='table', ctx=Store())],
                    value=table_data_value,
                    type_comment=None)
            ],
            decorator_list=[dataclass_decorator]
        ),
        ClassDef(
            name='Slide2',
            bases=[Name(id='SlideData', ctx=Load())],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='slide_pos', ctx=Store())],
                    value=Constant(value=2, kind=None),
                    type_comment=None),
                AnnAssign(
                    target=Name(id='contents', ctx=Store()),
                    annotation=Subscript(
                        value=Name(id='Optional', ctx=Load()),
                        slice=Index(value=Name(id='Slide2Content', ctx=Load())),
                        ctx=Load()
                    ),
                    value=None,
                    simple=1)
            ],
            decorator_list=[dataclass_decorator]
        ),
        Assign(
            targets=[
                Name(id='SLIDES', ctx=Store())
            ],
            value=List(
                elts=[
                    Name(id='Slide1', ctx=Load()),
                    Name(id='Slide2', ctx=Load())
                ],
                ctx=Load()
            ),
            type_comment=None
        )
    ],
    type_ignores=[]
)

if __name__ == '__main__':
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    target = os.path.join(BASE_DIR, 'stub_sample.py')
    with open(target, mode='r') as fp:
        data = fp.read()
    at = ast.parse(data)
    print(ast.dump(at))
    # print(decompile(clone))
    print(decompile(at))
