import os

# from .testcase import PPTTTestCase
# from ...PPTT.ppt import make_ppt

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# class TextPlaceholderTestCase(PPTTTestCase):
#     master_slide = os.path.join(BASE_DIR, 'text_placeholder.pptx')
#
#     def test_replace_text(self):
#         ms = self.get_master_ppt()
#         slide_layout_name = 'simple_title'
#         origin_layout = ms.slide_master.slide_layouts.get_by_name(slide_layout_name)
#         # check placeholder exists
#         title_shape_name = 'title'
#         body_shape_name = 'body'
#         self.assertTrue([s for s in origin_layout.shapes if s.name == title_shape_name][0])
#         self.assertTrue([s for s in origin_layout.shapes if s.name == body_shape_name][0])
#
#         input = [
#             {
#                 "slide_name": slide_layout_name,
#                 "contents": {
#                     title_shape_name: {
#                         "text": "this is test title",
#                     },
#                     body_shape_name: {
#                         "text": "test body",
#                     }
#                 }
#             }
#         ]
#         make_ppt(self.master_slide, self.target_slide, input, mode='template')
#         ppt = self.get_target_ppt()
#         print(ppt.slides)
#         self.assertEqual(1, len(ppt.slides))
#         shapes = ppt.slides[0].shapes
#         self.assertEqual(2, len(shapes))
#
#         slide = ppt.slides[0]
#         contents = input[0]['contents']
#         title_shape = self.find_shape_by_slide_layout(slide, title_shape_name)
#         self.assertEqual(contents[title_shape_name]['text'], title_shape.text)
#
#         body_shape = self.find_shape_by_slide_layout(slide, body_shape_name)
#         self.assertEqual(contents[body_shape_name]['text'], body_shape.text)
#
#     def test_dirty_shape_name(self):
#         ms = self.get_master_ppt()
#         slide_layout_name = 'dirty_shape_name'
#         origin_layout = ms.slide_master.slide_layouts.get_by_name(slide_layout_name)
#         # check placeholder exists
#         title_shape_name = "TITLE@@ AB"
#         body_shape_name = "This is Body"
#         self.assertTrue([s for s in origin_layout.shapes if s.name == title_shape_name][0])
#         self.assertTrue([s for s in origin_layout.shapes if s.name == body_shape_name][0])
#
#         input = [
#             {
#                 "slide_name": slide_layout_name,
#                 "contents": {
#                     title_shape_name: {
#                         "text": "this is test title",
#                     },
#                     body_shape_name: {
#                         "text": "test body",
#                     }
#                 }
#             }
#         ]
#         make_ppt(self.master_slide, self.target_slide, input, mode='template')
#         ppt = self.get_target_ppt()
#         print(ppt.slides)
#         self.assertEqual(1, len(ppt.slides))
#         shapes = ppt.slides[0].shapes
#         self.assertEqual(2, len(shapes))
#
#         slide = ppt.slides[0]
#         contents = input[0]['contents']
#         title_shape = self.find_shape_by_slide_layout(slide, title_shape_name)
#         self.assertEqual(contents[title_shape_name]['text'], title_shape.text)
#
#         body_shape = self.find_shape_by_slide_layout(slide, body_shape_name)
#         self.assertEqual(contents[body_shape_name]['text'], body_shape.text)

#
# class TablePlaceholderTestCase(PPTTTestCase):
#     master_slide = os.path.join(BASE_DIR, 'table_placeholder.pptx')
#
#     def test_replace_key_value_type(self):
#         ms = self.get_master_ppt()
#         slide_layout_name = 'simple_table'
#         origin_layout = ms.slide_master.slide_layouts.get_by_name(slide_layout_name)
#         # check placeholder exists
#         shape_name = 'table'
#         table_shape = [s for s in origin_layout.shapes if s.name == shape_name][0]
#         self.assertTrue(table_shape.has_table)
#
#         input = [
#             {
#                 "slide_name": slide_layout_name,
#                 "contents": {
#                     shape_name: {
#                         "table": {
#                             "data_type": "key_value",
#                             "keys": ['name', 'age'],
#                             "data": [
#                                 {"name": "NAME", "age": "AGE"},
#                                 {"name": "abc", "age": 1},
#                                 {"name": "aasdfasdf", "age": 3},
#                                 {"name": "bcd", "age": 4},
#                             ]
#                         }
#                     },
#                 }
#             }
#         ]
#         make_ppt(self.master_slide, self.target_slide, input)
#         ppt = self.get_target_ppt()
#         self.assertEqual(1, len(ppt.slides))
#         shapes = ppt.slides[0].shapes
#         self.assertEqual(1, len(shapes))
#
#         slide = ppt.slides[0]
#         contents = input[0]['contents']
#         table_shape = self.find_shape(slide, shape_name)
#         # self.assertEqual(contents[shape_name]['text'], table_shape.text)

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
