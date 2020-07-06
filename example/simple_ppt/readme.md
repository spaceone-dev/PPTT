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
    "slide_name": "title_slide",
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
    "slide_name": "chart_slide",
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
    "slide_name": "title_slide",
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
    "slide_name": "title_slide",
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