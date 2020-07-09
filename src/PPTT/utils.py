from pptx.slide import SlideLayout
from slugify import slugify


def name_to_slugify(name: str):
    return slugify(name, separator='_')


def find_shape(slide: SlideLayout, name):
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


def find_shape_by_slide_layout(slide, name, soft=False):
    if isinstance(slide, SlideLayout):
        return find_shape(slide, name)
    else:
        sl = slide.slide_layout
        placeholder_shape = find_shape(sl, name)
        if placeholder_shape:
            return find_match_shape(placeholder_shape, slide.shapes, soft)
