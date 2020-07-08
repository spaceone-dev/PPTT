import os
from typing import List

from .testcase import PPTTTestCase
from ...PPTT.ppt import make_ppt

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class TextPlaceholderTestCase(PPTTTestCase):
    master_slide = os.path.join(BASE_DIR, 'text_replace.pptx')

    def test_replace_text(self):
        ms = self.get_master_ppt()
        slide_pos = 1
        real_slide_pos = slide_pos - 1
        origin_slide = ms.slides[real_slide_pos]
        # check placeholder exists
        title_shape_name = 'title'
        body_shape_name = 'body'
        self.assertTrue([s for s in origin_slide.shapes if s.name == title_shape_name][0])
        self.assertTrue([s for s in origin_slide.shapes if s.name == body_shape_name][0])

        input = [
            {
                "slide_pos": slide_pos,
                "contents": {
                    title_shape_name: {
                        "text": "this is test title",
                    },
                    body_shape_name: {
                        "text": "test \nbody",
                    }
                }
            }
        ]
        make_ppt(self.master_slide, self.target_slide, input)
        ppt = self.get_target_ppt()
        slide = ppt.slides[real_slide_pos]
        self.assertEqual(2, len(slide.shapes))

        contents = input[0]['contents']
        title_shape = self.find_shape(slide, title_shape_name)
        self.assertEqual(contents[title_shape_name]['text'], title_shape.text)

        body_shape = self.find_shape(slide, body_shape_name)
        self.assertEqual(contents[body_shape_name]['text'], body_shape.text)

    def test_dirty_shape_name(self):
        ms = self.get_master_ppt()
        slide_pos = 2
        real_slide_pos = slide_pos - 1
        origin_slide = ms.slides[real_slide_pos]
        # check placeholder exists
        title_shape_name = "TITLE@@ AB"
        body_shape_name = "This is Body"
        self.assertTrue([s for s in origin_slide.shapes if s.name == title_shape_name][0])
        self.assertTrue([s for s in origin_slide.shapes if s.name == body_shape_name][0])

        input = [
            {
                "slide_pos": slide_pos,
                "contents": {
                    title_shape_name: {
                        "text": "this is test title",
                    },
                    body_shape_name: {
                        "text": "test body",
                    }
                }
            }
        ]
        make_ppt(self.master_slide, self.target_slide, input)
        ppt = self.get_target_ppt()
        slide = ppt.slides[real_slide_pos]
        self.assertEqual(2, len(slide.shapes))

        contents = input[0]['contents']
        title_shape = self.find_shape(slide, title_shape_name)
        self.assertEqual(contents[title_shape_name]['text'], title_shape.text)

        body_shape = self.find_shape(slide, body_shape_name)
        self.assertEqual(contents[body_shape_name]['text'], body_shape.text)


class TablePlaceholderTestCase(PPTTTestCase):
    master_slide = os.path.join(BASE_DIR, 'table_replace.pptx')

    def test_replace_key_value_type(self):
        ms = self.get_master_ppt()
        slide_pos = 1
        real_slide_pos = slide_pos - 1
        origin_slide = ms.slides[real_slide_pos]
        # check placeholder exists
        shape_name = 'table'
        self.assertTrue([s for s in origin_slide.shapes if s.name == shape_name][0])

        input = [
            {
                "slide_pos": slide_pos,
                "contents": {
                    shape_name: {
                        "table": {
                            "data_type": "key_value",
                            "keys": ['name', 'age', 'hobby', 'language'],
                            "data": [
                                {"name": "abc", "age": 12, 'hobby': "reading", "language": "english"},
                                {"name": "summer", "age": 3, 'hobby': "playing", "language": "korean"},
                                {"name": "sinsky", "age": 28, 'hobby': "coding", "language": "korean"},
                            ]
                        }
                    },
                }
            }
        ]
        make_ppt(self.master_slide, self.target_slide, input)
        ppt = self.get_target_ppt()
        slide = ppt.slides[real_slide_pos]
        self.assertEqual(1, len(slide.shapes))

        table_contents = input[0]['contents'][shape_name]['table']
        table_headers = table_contents['keys']
        talbe_data: List[dict] = table_contents['data']

        table_records = [[f"{v}" for v in r.values()] for r in talbe_data]
        table_shape = self.find_shape(slide, shape_name)
        rows = table_shape.table.rows
        header_row = rows[0]
        self.assertEqual(table_headers, [cell.text for cell in header_row.cells])
        target_table_records = []
        for row_idx in range(len(rows) - 1):
            row_real_idx = row_idx + 1
            target_table_records.append([cell.text for cell in rows[row_real_idx].cells])
        self.assertEqual(table_records, target_table_records)

        # def test_replace_key_value_type_struct_keys(self):
        #     ms = self.get_master_ppt()
        #     slide_layout_name = 'simple_table'
        #     origin_layout = ms.slide_master.slide_layouts.get_by_name(slide_layout_name)
        #     # check placeholder exists
        #     shape_name = 'table'
        #     table_shape = [s for s in origin_layout.shapes if s.name == shape_name][0]
        #     self.assertTrue(table_shape.has_table)
        #
        #     input = [
        #         {
        #             "slide_name": slide_layout_name,
        #             "contents": {
        #                 shape_name: {
        #                     "table": {
        #                         "data_type": "key-value",
        #                         "keys": [
        #                             {"text": "Name", "data_key": "name"},
        #                             {"text": "Age", "data_key": "name"}
        #                         ],
        #                         "data": [
        #                             {"name": "NAME", "age": "AGE"},
        #                             {"name": "abc", "age": 1},
        #                             {"name": "aasdfasdf", "age": 3},
        #                             {"name": "bcd", "age": 4},
        #                         ]
        #                     }
        #                 },
        #             }
        #         }
        #     ]
        #     make_ppt(self.master_slide, self.target_slide, input)
        #     ppt = self.get_target_ppt()
        #     self.assertEqual(1, len(ppt.slides))
        #     shapes = ppt.slides[0].shapes
        #     self.assertEqual(1, len(shapes))
        #
        #     slide = ppt.slides[0]
        #     contents = input[0]['contents']
        #     table_shape = self.find_shape(slide, shape_name)
        #     # self.assertEqual(contents[shape_name]['text'], table_shape.text)
