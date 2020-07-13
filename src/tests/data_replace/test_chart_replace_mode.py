import os
import unittest
from typing import Dict

from .testcase import PPTTTestCase
from ...PPTT.ppt import make_ppt

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class CategoryChartDataTestCase(PPTTTestCase):
    master_slide = os.path.join(BASE_DIR, 'chart_replace.pptx')

    def test_chart_title_text(self):
        ms = self.get_master_ppt()
        slide_pos = 1
        real_slide_pos = slide_pos - 1
        origin_slide = ms.slides[real_slide_pos]
        # check placeholder exists
        shape_name = 'bar_chart'
        self.assertTrue([s for s in origin_slide.shapes if s.name == shape_name][0])

        input = [
            {
                "slide_pos": slide_pos,
                "contents": {
                    shape_name: {
                        "chart": {
                            "data_type": "category_data",
                            "title": "this is new chart",
                            "categories": ['list', 'dict', 'str'],
                            "series": {
                                "series 1": [5, 13, 8]
                            }
                        }
                    },
                }
            }
        ]
        make_ppt(self.master_slide, self.target_slide, input)
        ppt = self.get_target_ppt()
        slide = ppt.slides[real_slide_pos]
        self.assertEqual(1, len(slide.shapes))

        chart_contents = input[0]['contents'][shape_name]['chart']
        chart_title = chart_contents['title']

        chart = self.find_shape(slide, shape_name).chart
        self.assertEqual(chart_title, chart.chart_title.text_frame.text)

    def check_chart_data(self, slide_pos, shape_name):
        ms = self.get_master_ppt()
        real_slide_pos = slide_pos - 1
        origin_slide = ms.slides[real_slide_pos]
        # check placeholder exists
        self.assertTrue([s for s in origin_slide.shapes if s.name == shape_name][0])

        input = [
            {
                "slide_pos": slide_pos,
                "contents": {
                    shape_name: {
                        "chart": {
                            "data_type": "category_data",
                            "categories": ['list', 'dict', 'str'],
                            "series": {
                                "series 1": [5, 13, 8],
                                "series 2": [6, 1, 3]
                            }
                        }
                    },
                }
            }
        ]
        make_ppt(self.master_slide, self.target_slide, input)
        ppt = self.get_target_ppt()
        slide = ppt.slides[real_slide_pos]

        chart_contents = input[0]['contents'][shape_name]['chart']
        chart_categories = chart_contents['categories']
        chart_series: Dict[str, list] = chart_contents['series']

        chart = self.find_shape(slide, shape_name).chart
        # check categories
        self.assertEqual(chart_categories, [cat.label for cat in chart.plots[0].categories])
        # check series names
        self.assertEqual(list(chart_series.keys()), [ser.name for ser in chart.series])
        # check series values
        self.assertEqual(
            [[float(v) for v in vs] for vs in chart_series.values()],
            [list(ser.values) for ser in chart.series]
        )

    def test_use_category_data_chart(self):
        charts = [
            [1, 'bar_chart'],
            [2, 'bar_mix_chart'],
            [2, 'bar_100_chart'],
            [3, 'line_chart'],
            [3, 'area_chart'],
            [4, 'circle_chart'],
            [4, 'donut_chart'],
            [5, 'radar_chart'],
        ]
        for args in charts:
            with self.subTest(slide_pos=args[0], chart_name=args[1]):
                self.check_chart_data(*args)
        pass


class XYChartDataTestCase(PPTTTestCase):
    # deubg = True
    # temp_dir = BASE_DIR
    master_slide = os.path.join(BASE_DIR, 'chart_replace.pptx')

    def check_chart_data(self, slide_pos, shape_name):
        ms = self.get_master_ppt()
        real_slide_pos = slide_pos - 1
        origin_slide = ms.slides[real_slide_pos]
        # check placeholder exists
        self.assertTrue([s for s in origin_slide.shapes if s.name == shape_name][0])

        input = [
            {
                "slide_pos": slide_pos,
                "contents": {
                    shape_name: {
                        "chart": {
                            "data_type": "xy_data",
                            "series": {
                                "apple": [
                                    {"x": 1, "y": 7},
                                    {"x": 3, "y": 4},
                                    {"x": 6, "y": 5},
                                    {"x": 4, "y": 3},
                                    {"x": 9, "y": 5},
                                ],
                                "google": [
                                    {"x": 5, "y": 7},
                                    {"x": 6, "y": 2},
                                    {"x": 10, "y": 5},
                                    {"x": 3, "y": 1},
                                    {"x": 9, "y": 4},
                                ]
                            }
                        }
                    },
                }
            }
        ]
        make_ppt(self.master_slide, self.target_slide, input)
        ppt = self.get_target_ppt()
        slide = ppt.slides[real_slide_pos]

        chart_contents = input[0]['contents'][shape_name]['chart']
        chart_series = chart_contents['series']

        chart = self.find_shape(slide, shape_name).chart

        # check series names
        self.assertEqual(list(chart_series.keys()), [ser.name for ser in chart.series])

        # check series values
        xy_values = {}
        for ser in chart.series:
            y_values = ser._element.yVal
            x_values = ser._element.xVal
            xy_values[ser.name] = [
                {"x": x_values.pt_v(idx), "y": y_values.pt_v(idx)} for idx in range(len(ser.values))
            ]
        self.assertEqual(chart_series, xy_values)

    def test_use_xy_data_chart(self):
        charts = [
            [7, 'xy_chart'],
        ]
        for args in charts:
            with self.subTest(slide_pos=args[0], chart_name=args[1]):
                self.check_chart_data(*args)
        pass


class BubbleChartDataTestCase(PPTTTestCase):
    deubg = True
    temp_dir = BASE_DIR
    master_slide = os.path.join(BASE_DIR, 'chart_replace.pptx')

    def check_chart_data(self, slide_pos, shape_name):
        ms = self.get_master_ppt()
        real_slide_pos = slide_pos - 1
        origin_slide = ms.slides[real_slide_pos]
        # check placeholder exists
        self.assertTrue([s for s in origin_slide.shapes if s.name == shape_name][0])

        input = [
            {
                "slide_pos": slide_pos,
                "contents": {
                    shape_name: {
                        "chart": {
                            "data_type": "bubble_data",
                            "series": {
                                "apple": [
                                    {"x": 1, "y": 7, "size": 5},
                                    {"x": 3, "y": 4, "size": 4},
                                    {"x": 6, "y": 5, "size": 1},
                                    {"x": 4, "y": 3, "size": 8},
                                    {"x": 9, "y": 5, "size": 3},
                                ],
                                "google": [
                                    {"x": 5, "y": 7, "size": 5},
                                    {"x": 6, "y": 2, "size": 3},
                                    {"x": 10, "y": 5, "size": 7},
                                    {"x": 3, "y": 1, "size": 2},
                                    {"x": 9, "y": 4, "size": 3},
                                ]
                            }
                        }
                    },
                }
            }
        ]
        make_ppt(self.master_slide, self.target_slide, input)
        ppt = self.get_target_ppt()
        slide = ppt.slides[real_slide_pos]

        chart_contents = input[0]['contents'][shape_name]['chart']
        chart_series = chart_contents['series']
        # chart_points = [ [ for point in ser] for ser in chart_series]

        chart = self.find_shape(slide, shape_name).chart

        # check series names
        self.assertEqual(list(chart_series.keys()), [ser.name for ser in chart.series])

        # check series values
        series_values = {}
        for ser in chart.series:
            y_values = ser._element.yVal
            x_values = ser._element.xVal
            size_values = ser._element.bubbleSize
            series_values[ser.name] = [
                {
                    "x": x_values.pt_v(idx),
                    "y": y_values.pt_v(idx),
                    "size": size_values.pt_v(idx)
                } for idx in range(len(ser.values))
            ]
        print(series_values)
        self.assertEqual(chart_series, series_values)

    def test_use_buble_data_chart(self):
        charts = [
            [8, 'bubble_chart'],
        ]
        for args in charts:
            with self.subTest(slide_pos=args[0], chart_name=args[1]):
                self.check_chart_data(*args)
        pass


if __name__ == '__main__':
    unittest.main()
