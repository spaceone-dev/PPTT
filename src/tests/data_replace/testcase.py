import os
import tempfile
from unittest import TestCase

from pptx import Presentation
from pptx.presentation import Presentation as PresentationType

from PPTT.utils import find_shape, find_shape_by_slide_layout


class PPTTTestCase(TestCase):
    master_slide = ''
    temp_dir = None
    target_slide = ''

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.target_slide = os.path.join(self.temp_dir.name, 'target.pptx')

    def tearDown(self):
        self.temp_dir.cleanup()
        self.temp_dir = None

    def get_master_ppt(self) -> PresentationType:
        return Presentation(self.master_slide)

    def get_target_ppt(self) -> PresentationType:
        return Presentation(self.target_slide)

    @staticmethod
    def find_shape_by_slide_layout(slide, name):
        return find_shape_by_slide_layout(slide, name, soft=True)

    @staticmethod
    def find_shape(slide, name):
        return find_shape(slide, name)


class DebugPPTTestCase(PPTTTestCase):
    """
    help debuging pptx when develop testcase
    """
    temp_dir = None
    target_slide = ''

    def setUp(self):
        self.target_slide = os.path.join(self.temp_dir, 'target.pptx')

    def tearDown(self):
        pass
