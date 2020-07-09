from typing import List

from pptx import Presentation

from .replace import replace_data
from .schema import SlideStub


def make_ppt(
        master_file: str, target_file: str,
        pages: List[dict], delete_pages: List[int] = None,
        mode: str = "replace"):
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
