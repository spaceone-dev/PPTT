# Python API Example

## make stub file
```shell script
pptt make_stub master.pptx
```
## check stub
`pptt make_stub master.pptx` will make `slide_stubs.py` like this!
```python
# slide_stubs.py
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

```

## make page!
```python
# slide.py
import os

from PPTT.ppt import make_ppt_from_stub
# t
from slide_stubs import title_slide, chart_slide

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__':
    slieds = []
    # slide 1
    slide1 = title_slide()
    slide1.title = 'slide 1'
    slide1.subtitle = 'first slide using stub'
    slieds.append(slide1)

    # slide 2
    slide2 = chart_slide()
    slide2.title = 'slide2'
    slide2.text = "this is\n make by\nstub"
    slieds.append(slide2)

    master_file = os.path.join(BASE_DIR, 'master.pptx')
    export_file = os.path.join(BASE_DIR, 'clone.pptx')
    make_ppt_from_stub(master_file, export_file, slieds)
```

## Done!
you can make ppt using stub so easy! 