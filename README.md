# PPTT
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/PPTT?style=flat-square)](https://pypi.org/project/PPTT)
[![PyPI](https://img.shields.io/pypi/v/PPTT?style=flat-square)](https://pypi.org/project/PPTT)
[![PyPI download month](https://img.shields.io/pypi/dm/PPTT?style=flat-square)](https://pypi.org/project/PPTT)
[![codecov](https://codecov.io/gh/spaceone-dev/PPTT/branch/master/graph/badge.svg)](https://codecov.io/gh/spaceone-dev/PPTT)
[![HitCount](http://hits.dwyl.com/spaceone-dev/PPTT.svg)](http://hits.dwyl.com/spaceone-dev/PPTT)


PowerPoint Template for python

## Installation
```bash
$ pip install PPTT
✨🍰✨
```
### How to use it?
#### make master pptx
[link how to make master pptx](#)

#### master.pptx preview
![master_preview](https://raw.githubusercontent.com/spaceone-dev/PPTT/master/example/simple_ppt/master_pptx_preview.png)

#### make page!
create `slide.json` like this
```json
{
  "pages": [
    {
      "slide_pos": 1,
      "contents": {
        "title": {
          "text": "PPTT"
        },
        "subtitle": {
          "text": "you don't need to config design"
        }
      }
    },
    {
      "slide_pos": 2,
      "contents": {
        "title": {
          "text": "Replace Table Data"
        },
        "table": {
          "table": {
            "data_type": "key_value",
            "keys": [
              "Name",
              "Age",
              {
                "name": "Hobby",
                "data_key": "hobby"
              },
              {
                "name": {
                  "value": "Language",
                  "font": {
                    "bold": true,
                    "italic": true,
                    "underline": true,
                    "color": "#00F900"
                  }
                },
                "data_key": "language"
              }
            ],
            "data": [
              {"Name": "sinsky", "Age": 28, "hobby": "programming", "language": "korean"},
              {"Name": "summer", "Age": 4, "hobby": "reading", "language": "korean"},
              {"Name": "emmit", "Age": 30, "hobby": "lego", "language": "english"},
              {"Name": "agent", "Age": 20, "hobby": "hiding", "language": "english"},
              {
                "Name": "python",
                "Age": 38,
                "hobby": "making",
                "language": {
                  "value": "python",
                  "font": {
                    "bold": true,
                    "color": "#FFC107"
                  }
                }
              }
            ]
          }
        }
      }
    },
    {
      "slide_pos": 3,
      "contents": {
        "title": {
          "text": "Replace Chart Data"
        },
        "chart": {
          "chart": {
            "data_type": "category_data",
            "title": "this is new chart",
            "categories": ["list", "dict", "str"],
            "series": {
              "series 1": [5, 13, 8]
            }
          }
        }
      }
    },
    {
      "slide_pos": 4,
      "contents": {
        "body": {
          "text": "support multi-line\ntext\nlike this"
        },
        "table": {
          "table": {
            "data_type": "raw",
            "data": [
              [null, "1Q", {"value": "2Q", "font": {"bold": true}}],
              ["Apple", 10, {"value": 20, "font": {"italic": true}}],
              ["Google", 8, {"value": 8, "font": {"underline": true}}],
              ["AWS", 20, {"value": 15, "font": {"color": "00F900"}}]
            ]
          }
        },
        "chart": {
          "chart": {
            "data_type": "category_data",
            "categories": ["Apple", "Google", "AWS"],
            "series": {
              "1Q": [10, 8, 20],
              "2Q": [20, 6, 15]
            }
          }
        }
      }
    }
  ]
}
``` 

#### make ppt!
```shell script
pptt make_ppt master.pptx clone.pptx -i slide.json
```

##### clone.pptx preview
![master_preview](https://raw.githubusercontent.com/spaceone-dev/PPTT/master/example/simple_ppt/clone_pptx_preview.png)

### Python API
#### make stub file
```shell script
pptt make_stub master.pptx -o slide_stubs.py
```
#### make ppt as code
```shell script
import os

from PPTT.ppt import make_ppt
from PPTT.type import TextData, KeyValueData, TableData, KVKey, FontData, ChartCategoryData, \
    CategoryData, TextStyle, RawData
from slide_stubs import \
    Slide1 as CoverSlide, Slide1Content as CoverSlideContent, \
    Slide2 as TableSlide, Slide2Content as TableSlideContent, \
    Slide3 as ChartSlide, Slide3Content as ChartSlideContent, \
    Slide4 as ComboSlide, Slide4Content as ComboSlideContent

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__':
    slieds = []
    # slide 1
    cover_content = CoverSlideContent(
        title=TextData(text='PPTT'),
        subtitle=TextData(text="you don't need to config design")
    )

    slieds.append(CoverSlide(contents=cover_content))

    python_font = FontData(bold=True, color="#FFC107")
    language_font = FontData(bold=True, italic=True, underline=True, color="#00F900")
    # slide 2
    table_content = TableSlideContent(
        title=TextData(text="Replace Table Data"),
        table=TableData(table=KeyValueData(
            keys=[
                'Name',
                "Age",
                KVKey(name='Hobby', data_key="hobby"),
                KVKey(name=TextStyle(value="Language", font=language_font), data_key="language")
            ],
            data=[
                {"Name": "sinsky", "Age": 28, "hobby": "programming", "language": "korean"},
                {"Name": "summer", "Age": 4, "hobby": "reading", "language": "korean"},
                {"Name": "emmit", "Age": 30, "hobby": "lego", "language": "english"},
                {"Name": "agent", "Age": 20, "hobby": "hiding", "language": "english"},
                {"Name": "python", "Age": 38, "hobby": "making",
                 "language": TextStyle(value="python", font=python_font)
                 }
            ]
        )
        )
    )
    slieds.append(TableSlide(contents=table_content))

    # slide3
    chart_data = CategoryData(
        title="this is new chart",
        categories=['list', 'dict', 'str'],
        series={
            "series 1": [5, 13, 8]
        }
    )

    chart_content = ChartSlideContent(
        title=TextData(text="Replace Chart Data"),
        chart=ChartCategoryData(chart_data)
    )
    slieds.append(ChartSlide(contents=chart_content))

    # slide4
    table_raw_data = RawData(data=[
        [None, "1Q", TextStyle("2Q", font=FontData(bold=True))],
        ["Apple", 10, TextStyle(20, font=FontData(italic=True))],
        ["Google", 8, TextStyle(8, font=FontData(underline=True))],
        ["AWS", 20, TextStyle(15, font=FontData(color="#00F900"))]
    ])

    chart_category_data = CategoryData(
        categories=["Apple", "Google", "AWS"],
        series={
            "1Q": [10, 8, 20],
            "2Q": [20, 6, 15]
        }
    )

    combo_content = ComboSlideContent()
    combo_content.body = TextData("support multi-line\ntext\nlike this")
    combo_content.table = TableData(table_raw_data)
    combo_content.chart = ChartCategoryData(chart_category_data)

    slieds.append(ComboSlide(contents=combo_content))

    master_file = os.path.join(BASE_DIR, 'master.pptx')
    export_file = os.path.join(BASE_DIR, 'clone.pptx')

    make_ppt(master_file, export_file, pages=slieds)

```

# test
```
. ./tests.sh
```

# Change Logs
- 0.0.1
    - add cli version
    - cli usecase example
- 0.0.2
    - support [python api](https://github.com/spaceone-dev/PPTT/tree/master/example/python_api)
- 0.0.3
    - remove feature : I will refactoring ASAP
        - python api feature 
        - template mode
    - add replace mode
    - update simple usecase example
    - support table data replace
        - support data type : raw, key_value
    - support chart data replace
        - support data type :  category_data
- 0.0.4
    - New Feature
        - support all chart data tye : xy_data, bubble_data
    - Docs
        - add [chart example](https://github.com/spaceone-dev/PPTT/tree/master/example/chart_example)
- 0.0.5
    - Bug Fix
        - fix table replace data dose not reset issue
- 0.0.6
    - New Feature
        - change text font style #10
- 0.0.7
    - New Feature
        - make slide stub for python api
        
- 0.0.8
    - New Feature
        - now you can give alias to stub class [example](https://github.com/spaceone-dev/PPTT/tree/master/example/stub_alias)
        
- 0.0.9
    - New Feature
        - support delete slide
