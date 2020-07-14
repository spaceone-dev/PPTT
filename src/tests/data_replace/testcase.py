import os
import tempfile
from unittest import TestCase

from pptx import Presentation
from pptx.presentation import Presentation as PresentationType

from ...PPTT.utils import find_shape, find_shape_by_slide_layout


class PPTTTestCase(TestCase):
    deubg = False  # if true you can get target.ppt easy and doesn't delete after test end
    master_slide = ''
    temp_dir = None
    target_slide = ''

    def setUp(self):
        temp_dir_name = self.temp_dir
        if not all([self.deubg, self.temp_dir]):
            self.temp_dir = tempfile.TemporaryDirectory()
            temp_dir_name = self.temp_dir.name

        self.target_slide = os.path.join(temp_dir_name, 'target.pptx')

    def tearDown(self):
        if not all([self.deubg, self.temp_dir]):
            self.temp_dir.cleanup()
        if all([self.deubg, self.temp_dir]):
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
