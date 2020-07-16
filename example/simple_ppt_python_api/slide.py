import os

from PPTT.ppt import make_ppt
from PPTT.type import TextData, KeyValueData, TableData, KVKey, FontData, ChartCategoryData, \
    CategoryData, TextStyle, RawData
from slide_stubs import \
    Slide1 as CoverSlide, Slide1Content as CoverSlideContent, \
    Slide2 as TableSlide, Slide2Content as TableSlideContent, \
    Slide3 as ChartSlide, Slide3Content as ChartSlideContent, \
    Slide4 as ComboSlide, Slide4Content as ComboSlideContent

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__':
    slieds = []
    # slide 1
    cover_content = CoverSlideContent(
        title=TextData(text='PPTT'),
        subtitle=TextData(text="you don't need to config design")
    )

    slieds.append(CoverSlide(contents=cover_content))

    python_font = FontData(bold=True, color="#FFC107")
    language_font = FontData(bold=True, italic=True, underline=True, color="#00F900")
    # slide 2
    table_content = TableSlideContent(
        title=TextData(text="Replace Table Data"),
        table=TableData(table=KeyValueData(
            keys=[
                'Name',
                "Age",
                KVKey(name='Hobby', data_key="hobby"),
                KVKey(name=TextStyle(value="Language", font=language_font), data_key="language")
            ],
            data=[
                {"Name": "sinsky", "Age": 28, "hobby": "programming", "language": "korean"},
                {"Name": "summer", "Age": 4, "hobby": "reading", "language": "korean"},
                {"Name": "emmit", "Age": 30, "hobby": "lego", "language": "english"},
                {"Name": "agent", "Age": 20, "hobby": "hiding", "language": "english"},
                {"Name": "python", "Age": 38, "hobby": "making",
                 "language": TextStyle(value="python", font=python_font)
                 }
            ]
        )
        )
    )
    slieds.append(TableSlide(contents=table_content))

    # slide3
    chart_data = CategoryData(
        title="this is new chart",
        categories=['list', 'dict', 'str'],
        series={
            "series 1": [5, 13, 8]
        }
    )

    chart_content = ChartSlideContent(
        title=TextData(text="Replace Chart Data"),
        chart=ChartCategoryData(chart_data)
    )
    slieds.append(ChartSlide(contents=chart_content))

    # slide4
    table_raw_data = RawData(data=[
        [None, "1Q", TextStyle("2Q", font=FontData(bold=True))],
        ["Apple", 10, TextStyle(20, font=FontData(italic=True))],
        ["Google", 8, TextStyle(8, font=FontData(underline=True))],
        ["AWS", 20, TextStyle(15, font=FontData(color="#00F900"))]
    ])

    chart_category_data = CategoryData(
        categories=["Apple", "Google", "AWS"],
        series={
            "1Q": [10, 8, 20],
            "2Q": [20, 6, 15]
        }
    )

    combo_content = ComboSlideContent()
    combo_content.body = TextData("support multi-line\ntext\nlike this")
    combo_content.table = TableData(table_raw_data)
    combo_content.chart = ChartCategoryData(chart_category_data)

    slieds.append(ComboSlide(contents=combo_content))
    master_file = os.path.join(BASE_DIR, 'master.pptx')
    export_file = os.path.join(BASE_DIR, 'clone.pptx')
    make_ppt(master_file, export_file, pages=slieds)
