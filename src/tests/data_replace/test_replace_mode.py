import os
from typing import List

from .testcase import PPTTTestCase
from ...PPTT.ppt import make_ppt

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class TextReplaceTestCase(PPTTTestCase):
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


class TableReplaceTestCase(PPTTTestCase):
    # deubg = True
    # temp_dir = BASE_DIR

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
        table_data: List[dict] = table_contents['data']

        table_records = [[f"{v}" for v in r.values()] for r in table_data]
        table_shape = self.find_shape(slide, shape_name)
        rows = table_shape.table.rows
        header_row = rows[0]
        self.assertEqual(table_headers, [cell.text for cell in header_row.cells])
        target_table_records = []
        for row_idx in range(len(rows) - 1):
            row_real_idx = row_idx + 1
            target_table_records.append([cell.text for cell in rows[row_real_idx].cells])
        self.assertEqual(table_records, target_table_records)

    def test_replace_raw_type(self):
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
                            "data_type": "raw",
                            "data": [
                                ['name', 'age', 'hobby', 'language'],
                                ["abc", 12, "reading", "english"],
                                ["summer", 3, "playing", "korean"],
                                ["sinsky", 28, "coding", "korean"],
                            ],
                        }
                    },
                }
            }
        ]
        make_ppt(self.master_slide, self.target_slide, input)
        ppt = self.get_target_ppt()
        slide = ppt.slides[real_slide_pos]
        self.assertEqual(1, len(slide.shapes))

        table_data = input[0]['contents'][shape_name]['table']['data']
        # change int to text
        origin_table_data = [[f"{cell}" for cell in row] for row in table_data]

        table_shape = self.find_shape(slide, shape_name)
        rows = table_shape.table.rows
        replace_table_data = [[cell.text for cell in row.cells] for row in rows]
        self.assertEqual(len(origin_table_data), len(replace_table_data))
        self.assertEqual(origin_table_data, replace_table_data)

    def test_init_key_value_type(self):
        ms = self.get_master_ppt()
        slide_pos = 3
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
        table_data: List[dict] = table_contents['data']

        table_records = [[f"{v}" for v in r.values()] for r in table_data]
        table_shape = self.find_shape(slide, shape_name)
        rows = table_shape.table.rows
        header_row = rows[0]
        self.assertEqual(table_headers, [cell.text for cell in header_row.cells])
        target_table_records = []
        for row_idx in range(len(rows) - 1):
            row_real_idx = row_idx + 1
            row_data = [cell.text for cell in rows[row_real_idx].cells]
            if all(row_data):
                target_table_records.append(row_data)
        self.assertEqual(table_records, target_table_records)

    def test_init_raw_type(self):
        ms = self.get_master_ppt()
        slide_pos = 3
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
                            "data_type": "raw",
                            "data": [
                                ['name', 'age', 'hobby', 'language'],
                                ["abc", 12, "reading", "english"],
                                ["summer", 3, "playing", "korean"],
                            ],
                        }
                    },
                }
            }
        ]
        make_ppt(self.master_slide, self.target_slide, input)
        ppt = self.get_target_ppt()
        slide = ppt.slides[real_slide_pos]
        self.assertEqual(1, len(slide.shapes))

        table_data = input[0]['contents'][shape_name]['table']['data']
        # change int to text
        origin_table_data = [[f"{cell}" for cell in row] for row in table_data]

        table_shape = self.find_shape(slide, shape_name)
        rows = table_shape.table.rows
        replace_table_data = [[cell.text for cell in row.cells] for row in rows]
        replace_table_data = [row for row in replace_table_data if all(row)]
        self.assertEqual(len(origin_table_data), len(replace_table_data))
        self.assertEqual(origin_table_data, replace_table_data)
