# PPTT
PowerPoint Template for python


# How to use it?

## check your slide master schema
```shell script
pptt make_schema master.pptx -o output.json
```

## make page!
```json
# slide.json
[
  {
    "slide_name": "title slide",
    "contents": {
      "title": {
        "text": "It's So Easy"
      },
      "subtitle": {
        "text": "you don't need to config design"
      }
    }
  },
  {
    "slide_name": "chart init",
    "contents": {
      "title": {
        "text": "we will support easy chart data"
      },
      "text": {
        "text": "you can put\nmultiline\ntext"
      }
    }
  },
  {
    "slide_name": "title slide",
    "contents": {
      "title": {
        "text": "You can set many page\n what you want"
      },
      "subtitle": {
        "text": "hahahaha"
      }
    }
  },
  {
    "slide_name": "title slide",
    "contents": {
      "title": {
        "text": "One More Thing!"
      },
      "subtitle": {
        "text": "Not Thing!"
      }
    }
  }
]
```

## make ppt!
```shell script
pptt make_ppt master.pptx clone.pptx -i slide.json
```

# Change List
- 0.0.1
    - add cli version
    - cli usecase example
- 0.0.2
    - support [python api](https://github.com/spaceone-dev/PPTT/tree/master/example/python_api)