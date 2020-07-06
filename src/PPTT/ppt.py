from typing import List

from pptx import Presentation
from pptx.slide import SlideLayout

from .schema import SlideStub
from .stub import name_to_slugify


def find_shape_in_slide_layout(slide: SlideLayout, name):
    for shape in slide.shapes:
        if name in shape.name:
            return shape
        elif name_to_slugify(name) in shape.name:
            return shape


def find_match_shape(placeholder_shape, shapes, soft=False):
    """
    find match shape using left,top,with, height
    :param placeholder_shape:
    :param shapes:
    :param soft: if true only check shape_type,left,top
    :return:
    """
    for shape in shapes:
        if soft and all([
            placeholder_shape.left == shape.left,
            placeholder_shape.top == shape.top,
            placeholder_shape.shape_type == shape.shape_type,
        ]):
            return shape

        elif all([
            placeholder_shape.left == shape.left,
            placeholder_shape.top == shape.top,
            placeholder_shape.shape_type == shape.shape_type,
            placeholder_shape.width == shape.width,
            placeholder_shape.height == shape.height,
        ]):
            return shape


def find_shape(slide, name, soft=False):
    if isinstance(slide, SlideLayout):
        return find_shape_in_slide_layout(slide, name)
    else:
        sl = slide.slide_layout
        placeholder_shape = find_shape_in_slide_layout(sl, name)
        if placeholder_shape:
            return find_match_shape(placeholder_shape, slide.shapes, soft)


def replace_data(slide, contents: dict):
    for name, data in contents.items():
        shape = find_shape(slide, name)
        if shape:
            shape.name = name
            if 'text' in data:
                shape.text = data['text']


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
