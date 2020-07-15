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