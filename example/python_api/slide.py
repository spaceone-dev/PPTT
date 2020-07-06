import os

from PPTT.ppt import make_ppt_from_stub
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

    # slides is equal this
    # [
    #     {
    #         "slide_name": "title_slide",
    #         "contents": {
    #             "title": {
    #                 "text": "slide 1"
    #             },
    #             "subtitle": {
    #                 "text": "first slide using stub"
    #             }
    #         }
    #     },
    #     {
    #         "slide_name": "chart_slide",
    #         "contents": {
    #             "title": {
    #                 "text": "slide2"
    #             },
    #             "text": {
    #                 "text": "this is\n make by\nstub"
    #             }
    #         }
    #     }
    # ]
