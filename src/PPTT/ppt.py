from typing import List, Dict

from pptx import Presentation
from pptx.compat import to_unicode
from pptx.enum.dml import MSO_COLOR_TYPE
from pptx.shapes.graphfrm import GraphicFrame
from pptx.slide import SlideLayout
from pptx.text.text import TextFrame

from .schema import SlideStub
from .stub import name_to_slugify


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


def replace_paragraphs_text(paragraph, new_text):
    # copy from https://github.com/scanny/python-pptx/issues/285#issuecomment-300273686
    p = paragraph._p  # the lxml element containing the `<a:p>` paragraph element
    # remove all but the first run
    if paragraph.runs:
        for idx, run in enumerate(paragraph.runs):
            if idx == 0:
                continue
            p.remove(run._r)
    else:
        paragraph.add_run()
    paragraph.runs[0].text = new_text


def replace_run_style(style_run, target_run):
    target_run.font.name = style_run.font.name
    target_run.font.size = style_run.font.size
    target_run.font.bold = style_run.font.bold
    target_run.font.italic = style_run.font.italic
    target_run.font.underline = style_run.font.underline
    target_run.font.language_id = style_run.font.language_id

    if color_type := style_run.font.color.type:
        if color_type == MSO_COLOR_TYPE.RGB:
            target_run.font.color.rgb = style_run.font.color.rgb
        elif color_type == MSO_COLOR_TYPE.SCHEME:
            target_run.font.color.theme_color = style_run.font.color.theme_color
            target_run.font.color.brightness = style_run.font.color.brightness


def replace_paragraph_style(style_paragraph, target_paragraph):
    style_paragraph.alignment = target_paragraph.alignment
    style_paragraph.level = target_paragraph.level
    style_paragraph.line_spacing = target_paragraph.line_spacing
    style_paragraph.space_after = target_paragraph.space_after
    style_paragraph.space_before = target_paragraph.space_before


def clear_text_frame(text_frame: TextFrame):
    # remove all paragraphs
    for p in text_frame._txBody.p_lst[1:]:
        text_frame._txBody.remove(p)


def replace_text_frame(text_frame: TextFrame, new_text):
    clear_text_frame(text_frame)
    style_paragraph = text_frame.paragraphs[0]
    style_run = style_paragraph.runs[0]

    split_text = to_unicode(new_text).split('\n')
    if split_text:
        replace_paragraphs_text(text_frame.paragraphs[0], split_text[0])
        for text in split_text[1:]:
            p = text_frame.add_paragraph()
            replace_paragraph_style(style_paragraph, p)
            replace_paragraphs_text(p, text)
            replace_run_style(style_run, p.runs[0])


def replace_table_data_key_value(shape: GraphicFrame, data):
    keys: List[str or Dict[str, str]] = data.get('keys', [])
    datas: List[dict] = data.get('data', [])
    data_keys = [k.get('data_key') if isinstance(k, dict) else k for k in keys]
    for r_idx, row in enumerate(shape.table.rows):
        if r_idx == 0:
            for c_idx, cel in enumerate(row.cells):
                target_key = keys[c_idx]
                if isinstance(target_key, dict):
                    replace_text_frame(cel.text_frame, target_key.get('name', ''))
                elif isinstance(target_key, str):
                    replace_text_frame(cel.text_frame, target_key)
        else:
            data = datas[r_idx + 1]
            for idx, key in enumerate(data_keys):
                row.cells[idx].text = data.get(key)


TABLE_DATA_TYPE_HANDLER = {
    "key_value": replace_table_data_key_value,
    "raw": lambda shape, data: None
}


def replace_data(slide, contents: dict, mode="replace"):
    for name, data in contents.items():
        shape = find_shape(slide, name) if mode == 'replace' else find_shape_by_slide_layout(slide, name)
        if shape:
            # shape.name = name # for
            if 'text' in data:
                replace_text_frame(shape.text_frame, data['text'])
            if 'table' in data:
                try:
                    TABLE_DATA_TYPE_HANDLER[data.get('data_type', 'raw')](shape, data['table'])
                except Exception as e:
                    print(e)


def make_ppt(master_file: str, target_file: str, pages: list, mode: str = "replace"):
    master_pt = Presentation(master_file)
    for page in pages:
        if mode == 'template':
            slide_layout = master_pt.slide_layouts.get_by_name(page['slide_name'])
            slide = master_pt.slides.add_slide(slide_layout)
        elif mode == 'replace':
            slide = master_pt.slides[int(page['slide_pos']) - 1]
        else:
            raise NotImplementedError(f"doesn't support {mode} mode")
        replace_data(slide, page.get('contents'))

    master_pt.save(target_file)


def make_ppt_from_stub(master_file: str, target_file: str, pages: List[SlideStub]):
    master_pt = Presentation(master_file)
    for page in pages:
        slide_layout = master_pt.slide_layouts.get_by_name(page._slide_layout_name)
        slide = master_pt.slides.add_slide(slide_layout)
        replace_data(slide, page.get_contents())

    master_pt.save(target_file)
