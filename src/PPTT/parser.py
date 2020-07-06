from pptx import Presentation

from .stub import PPTTemplateStub
from .schema import PPTTemplate


def parser(file: str)->PPTTemplate:
    master_ppt = Presentation(file)
    template = PPTTemplate.load_by_pptx(master_ppt)
    return template
