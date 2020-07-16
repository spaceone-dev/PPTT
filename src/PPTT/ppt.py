from typing import List, Union, Dict

from pptx import Presentation

from .replace import replace_data
from .type import ReplaceSlideType, SlideData


def make_ppt(
        master_file: str, target_file: str,
        pages: List[Union[Dict, ReplaceSlideType, SlideData]], delete_pages: List[int] = None,
        mode: str = "replace"):
    master_pt = Presentation(master_file)
    for page in pages:
        if mode == 'template':
            raise NotImplementedError("doesn't support Template mode")
        elif mode == 'replace':
            if isinstance(page, dict):
                page = ReplaceSlideType.from_dict(page)
            slide = master_pt.slides[int(page.slide_pos) - 1]
        else:
            raise NotImplementedError(f"doesn't support {mode} mode")
        replace_data(slide, page.contents)

    master_pt.save(target_file)
