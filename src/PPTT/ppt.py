from pptx import Presentation


def find_shape(slide, name):
    for shape in slide.shapes:
        cap_name = name.capitalize() + ' '
        if cap_name in shape.name:
            return shape


def make_ppt(maset_file: str, target_file: str, pages: list):
    master_pt = Presentation(maset_file)
    for page in pages:
        slide_layout = master_pt.slide_layouts.get_by_name(page['slide_name'])
        slide = master_pt.slides.add_slide(slide_layout)
        for name, contents in page['contents'].items():
            shape = find_shape(slide, name)
            text = contents.get('text')
            if text:
                shape.text = text

    master_pt.save(target_file)
