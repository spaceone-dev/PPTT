import os
import unittest

from .testcase import PPTTTestCase
from ...PPTT.ppt import get_slide_by_pos, make_ppt

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class DeleteSlideTestCase(PPTTTestCase):
    debug = True
    temp_dir = BASE_DIR
    master_slide = os.path.join(BASE_DIR, 'delete_slide.pptx')

    def test_delete_slide_one(self):
        ms = self.get_master_ppt()
        before_total_slide = len(ms.slides)

        delete_slides_pos = [1]
        delete_slides_count = len(delete_slides_pos)
        delete_slides_id = [get_slide_by_pos(ms, pos).slide_id for pos in delete_slides_pos]

        make_ppt(self.master_slide, self.target_slide, delete_pages=delete_slides_pos)

        # check slide deleted
        ppt = self.get_target_ppt()

        # check slide count
        after_total_slide = len(ppt.slides)
        self.assertEqual(delete_slides_count, before_total_slide - after_total_slide)

        # check slide noe exists
        for slide_id in delete_slides_id:
            self.assertIsNone(ppt.slides.get(slide_id))

    def test_delete_table_slide(self):
        ms = self.get_master_ppt()
        before_total_slide = len(ms.slides)

        delete_slides_pos = [9]
        delete_slides_count = len(delete_slides_pos)
        delete_slides_id = [get_slide_by_pos(ms, pos).slide_id for pos in delete_slides_pos]

        make_ppt(self.master_slide, self.target_slide, delete_pages=delete_slides_pos)

        # check slide deleted
        ppt = self.get_target_ppt()

        # check slide count
        after_total_slide = len(ppt.slides)
        self.assertEqual(delete_slides_count, before_total_slide - after_total_slide)

        # check slide noe exists
        for slide_id in delete_slides_id:
            self.assertIsNone(ppt.slides.get(slide_id))

    def test_delete_slide_many(self):
        ms = self.get_master_ppt()
        before_total_slide = len(ms.slides)

        delete_slides_pos = [1, 2, 3]
        delete_slides_count = len(delete_slides_pos)
        delete_slides_id = [get_slide_by_pos(ms, pos).slide_id for pos in delete_slides_pos]

        make_ppt(self.master_slide, self.target_slide, pages=[], delete_pages=delete_slides_pos)

        # check slide deleted
        ppt = self.get_target_ppt()

        # check slide count
        after_total_slide = len(ppt.slides)
        self.assertEqual(delete_slides_count, before_total_slide - after_total_slide)

        # check slide noe exists
        for slide_id in delete_slides_id:
            self.assertIsNone(ppt.slides.get(slide_id))

    def test_delete_slide_complex(self):
        ms = self.get_master_ppt()
        before_total_slide = len(ms.slides)

        delete_slides_pos = [1, 3, 4, 7, 9]
        delete_slides_count = len(delete_slides_pos)
        delete_slides_id = [get_slide_by_pos(ms, pos).slide_id for pos in delete_slides_pos]

        make_ppt(self.master_slide, self.target_slide, pages=[], delete_pages=delete_slides_pos)

        # check slide deleted
        ppt = self.get_target_ppt()

        # check slide count
        after_total_slide = len(ppt.slides)
        self.assertEqual(delete_slides_count, before_total_slide - after_total_slide)

        # check slide noe exists
        for slide_id in delete_slides_id:
            self.assertIsNone(ppt.slides.get(slide_id))


if __name__ == '__main__':
    unittest.main()
