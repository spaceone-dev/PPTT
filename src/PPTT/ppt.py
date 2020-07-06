from typing import List

from pptx import Presentation

from .schema import SlideStub
from .stub import name_to_slugify


def find_shape(slide, name):
    for shape in slide.shapes:
        cap_name = name.capitalize() + ' '
        if cap_name in shape.name:
            return shape
        elif name_to_slugify(name).capitalize() + ' ' in shape.name:
            return shape


def replace_data(slide, contents: dict):
    for name, data in contents.items():
        shape = find_shape(slide, name)
        if text := data.get('text'):
            shape.text = text


def make_ppt(master_file: str, target_file: str, pages: list):
    master_pt = Presentation(master_file)
    for page in pages:
        slide_layout = master_pt.slide_layouts.get_by_name(page['slide_name'])
        slide = master_pt.slides.add_slide(slide_layout)
        replace_data(slide, page.get('contents'))

    master_pt.save(target_file)


def make_ppt_from_stub(master_file: str, target_file: str, pages: List[SlideStub]):
    master_pt = Presentation(master_file)
    for page in pages:
        slide_layout = master_pt.slide_layouts.get_by_name(page._slide_layout_name)
        slide = master_pt.slides.add_slide(slide_layout)
        replace_data(slide, page.get_contents())

    master_pt.save(target_file)
