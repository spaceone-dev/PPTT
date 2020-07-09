# How to use it?

## make master pptx
[link how to make master pptx](#)

### master.pptx preview
![master_preview](./master_pptx_preview.png)

## make page!
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
            "keys": ["Name", "Age", "Hobby", {"name": "Language", "data_key": "language"}],
            "data": [
              {"Name": "sinsky", "Age": 28, "Hobby": "programming", "language": "korean"},
              {"Name": "summer", "Age": 4, "Hobby": "reading", "language": "korean"},
              {"Name": "emmit", "Age": 30, "Hobby": "lego", "language": "english"},
              {"Name": "agent", "Age": 20, "Hobby": "hiding", "language": "english"},
              {"Name": "python", "Age": 38, "Hobby": "making", "language": "python"}
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
              [null, "1Q", "2Q"],
              ["Apple", 10, 20],
              ["Google", 8, 6],
              ["AWS", 20, 15]
            ]
          }
        }
      }
    }
  ]
}
```

## make ppt!
```shell script
pptt make_ppt master.pptx clone.pptx -i slide.json
```

### clone.pptx preview
![clone_preview](./clone_pptx_preview.png)