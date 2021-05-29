from 爬虫.爬虫1905050223鲁成运.dataAnalysis import *
from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.globals import ThemeType
import datetime

day = ["2020-12-16", "2020-12-22", "2020-12-23", "2020-12-24", "2020-12-26", "2020-12-28"]
# today = datetime.datetime.now().strftime("%Y-%m-%d")
today = day[-1]
timeLine1 = (
    Timeline(init_opts=opts.InitOpts(theme=ThemeType.ESSOS, width="1000px", height="800px"))
)
for i in existing_DataList:
    map1 = (
        Map()
        .add("现有确诊", data_pair=i, maptype="china", is_map_symbol_show=False)
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="国内各省疫情情况", pos_left="center", pos_top="2%", subtitle="更新日期：{}".format(today),
                title_textstyle_opts=opts.TextStyleOpts(font_size=50, color="red", font_family="华文楷体")),
            legend_opts=opts.LegendOpts(is_show=False),
            tooltip_opts=opts.TooltipOpts(is_show=True, trigger_on="mousemove|click", background_color="skyblue"),
            visualmap_opts=opts.VisualMapOpts(
                is_piecewise=True,
                pieces=[
                    {"min": 100, "label": "≥100人", "color": "#FF0000"},
                    {"min": 50, "max": 99, "label": "50-99人", "color": "#FF4500"},
                    {"min": 20, "max": 49, "label": "20-49人", "color": "#FA8072"},
                    {"min": 1, "max": 19, "label": "1-19人", "color": "#FFFF00"},
                    {"min": 0, "max": 0, "label": "0人", "color": "#DCDCDC"}
                ])
        )
    )
    timeLine1.add(map1, day[existing_DataList.index(i)])

timeLine2 = (
    Timeline(init_opts=opts.InitOpts(theme=ThemeType.CHALK, width="1000px", height="600px"))
)
for i in day:
    bar1 = (
        Bar()
        .add_xaxis(newExisting_DataList[day.index(i)][0])
        .add_yaxis("现有确诊", newExisting_DataList[day.index(i)][1], bar_width="60%")
        .set_global_opts(title_opts=opts.TitleOpts(
            title="各省现有确诊人数变化趋势图", pos_left="center", pos_top="2%", subtitle="更新日期：{}".format(today),
            title_textstyle_opts=opts.TextStyleOpts(font_size=40, font_family="华文楷体")),
            xaxis_opts=opts.AxisOpts(name="（地区）"),
            yaxis_opts=opts.AxisOpts(name="（人数)", max_=150),
            legend_opts=opts.LegendOpts(is_show=True, pos_right="5%", pos_bottom="85%", legend_icon="roundRect"),
            tooltip_opts=opts.TooltipOpts(is_show=True, trigger_on="mousemove|click", background_color="green")
        )
    )
    timeLine2.add(bar1, i)
line1 = (
    Line(init_opts=opts.InitOpts(theme=ThemeType.DARK, width="1000px", height="550px"))
    .add_xaxis(day)
    .add_yaxis("总人数", existingSum, linestyle_opts=opts.LineStyleOpts(width=3, color="#43CD80"))
    .set_global_opts(title_opts=opts.TitleOpts(title="现有确诊总人数变化趋势图", pos_left="center", pos_top="2%",
                                               subtitle="更新日期：{}".format(today),
                                               title_textstyle_opts=opts.TextStyleOpts(font_size=40, font_family="华文楷体")),
                     xaxis_opts=opts.AxisOpts(name="（日期）"),
                     yaxis_opts=opts.AxisOpts(name="（人数)"),
                     legend_opts=opts.LegendOpts(is_show=True, pos_right="5%", pos_bottom="85%", legend_icon="circle"),
                     tooltip_opts=opts.TooltipOpts(is_show=True, trigger_on="mousemove|click", background_color="green")
                     )
)

timeline3 = (
    Timeline(init_opts=opts.InitOpts(theme=ThemeType.DARK, width="1000px", height="550px"))
)
newDay = ["2020-12-22", "2020-12-23", "2020-12-24", "2020-12-26", "2020-12-28"]
for i in newDay:
    line2 = (
        Line()
        .add_xaxis(newAddExisting_DataList[newDay.index(i)][0])
        .add_yaxis("新增人数(较前一日期)", newAddExisting_DataList[newDay.index(i)][1])
        .set_global_opts(title_opts=opts.TitleOpts(title="各省新增人数趋势图", pos_left="center", pos_top="2%",
                                                   subtitle="更新日期：{}".format(today),
                                                   title_textstyle_opts=opts.TextStyleOpts(font_size=40,
                                                                                           font_family="华文楷体")),
                         xaxis_opts=opts.AxisOpts(name="（日期）"),
                         yaxis_opts=opts.AxisOpts(name="（人数)"),
                         legend_opts=opts.LegendOpts(is_show=True, pos_right="5%", pos_bottom="85%",
                                                     legend_icon="circle"),
                         tooltip_opts=opts.TooltipOpts(is_show=True, trigger_on="mousemove|click",
                                                       background_color="green")
                         )
    )
    timeline3.add(line2, i)

page = (
    Page(page_title="国内疫情情况").add(
        timeLine1,
        timeLine2,
        line1,
        timeline3,
    )
)

page.render("国内疫情情况.html")
