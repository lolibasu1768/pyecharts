# pyecharts Documentation

pyecharts is a library to generate charts using Echarts. It simply provides the interface between Echarts and Python.

[![Build Status](https://travis-ci.org/chenjiandongx/pyecharts.svg?branch=master)](https://travis-ci.org/chenjiandongx/pyecharts)  

* [First-steps](https://github.com/chenjiandongx/pyecharts/blob/master/document/en-us/documentation.md#First-steps)
* [Global-options](https://github.com/chenjiandongx/pyecharts/blob/master/document/en-us/documentation.md#Global-options)
    * xyAxis：x, y axis in cartesian coordinate system(Line, Bar, Scatter, EffectScatter, Kline)
    * dataZoom：dataZoom components for zoom-in and zoom-out. With them, it is possible to magnify a small area, to see the overall picture or to stay away from scattered points(Line, Bar, Scatter, EffectScatter, Kline)
    * legend：legend component has different symbol, colour and name, and provide the interactive clicking functions to show or hide its associated data series.
    * label：text string on the chart, for marking the charts with sensible details, such as value, name.
    * lineStyle：line style for Line, Polar, Radar, Graph, Parallel.
    * grid3D：gird3D components in cartesian coordinate system(Bar3D, Line3D, Scatter3D)
    * visualMap：It is a type of component for visual encoding, which maps the data to visual channels
* [Chart-types](https://github.com/chenjiandongx/pyecharts/blob/master/document/en-us/documentation.md#Chart-types)
    * Bar
    * Bar3D
    * EffectScatter
    * Funnel
    * Gauge
    * Geo
    * Graph
    * HeatMap
    * Kline
    * Line
    * Line3D
    * Liquid
    * Map
    * Parallel
    * Pie
    * Polar
    * Radar
    * Scatter
    * Scatter3D
    * WordCloud
* [Customize](https://github.com/chenjiandongx/pyecharts/blob/master/document/en-us/documentation.md#Customize)
* [Example](https://github.com/chenjiandongx/pyecharts/blob/master/document/en-us/documentation.md#Example)
* [About](https://github.com/chenjiandongx/pyecharts/blob/master/document/en-us/documentation.md#About)


# First-steps
### Make sure you have installed the latest version pyecharts
Now, you are ready to make your first chart!
```python
from pyecharts import Bar

bar = Bar("我的第一个图表", "这里是副标题")
bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
bar.show_config()
bar.render()
```
![guide-0](https://github.com/chenjiandongx/pyecharts/blob/master/images/guide-0.png)

**Tip：** You can click the download button on the right side to download the picture to your local disk.

* ```add()```
    main method，add the data and set up various options of the chart
* ```show_config()```
    print and output all options of the chart
* ```render()```
    creat a file named render.html in the root directory defaultly,which supports path parameter and set the location the file save in,for instance render(r"e:\my_first_chart.html")，open file with your browser.

### A note on Jupyter notebook

For existing users, in order to play with the offline mode coming with 0.1.9.5, it is recommended that 1) the old version must be uninstalled. 2) Your existing notebooks must be refreshed and re-ran. 3) You must have installed **jupyter**. This restriction will be gone when jupyter-pip will release its next version.

How the offline mode works is: all echarts javascript libraries are copied into nbextensions directory. The following command helps you find out whether pyecharts js components are installed or not

```shell
$ jupyter nbextension list
Known nbextensions:
  config dir: /Users/jaska/.jupyter/nbconfig
    notebook section
      echarts/main  enabled 
      - Validating: OK
```

Rarely, you would enforce pyecharts to reload all echarts javascript libraries. However if you intend to do so, you can issue these commands:

```shell
$ git clone https://github.com/chfw/jupyter-echarts.git
$ cd jupyter-echarts
$ jupyter nbextensions install echarts --user
```
Upon next rendering, all javascript libraries will be copied again.

And rarely again unless you are a developer of pyecharts, you choose to remove the extension:

```shell
$ jupyter nbextensions uninstall echarts --user
```

### Python2 Coding Problem
default code type is UTF-8, there's no problem in Python3, because Python3 have a good support in chinese. But in Python2, please use the following sentence to ensure avoiding wrong coding problem:
```
#!/usr/bin/python
#coding=utf-8
from __future__ import unicode_literals
```
The first two sentences are telling your editor that it should use UTF-8 ([PEP-0263](https://www.python.org/dev/peps/pep-0263/)). And the last sentence is telling Python all the characters are UTF-8 ([unicode literals](http://python-future.org/unicode_literals.html))


almost all the chart type drawed like this:
1. ```chart_name = Type()``` Initialise the concrete chart type.
2. ```add()``` Add data and options.
3. ```render()``` Creat .html file.

```add()``` Data is two lists commonly(the same length),if your data is dictionary or dictionary with tuple,use ```cast()``` to convert.

```python
@staticmethod
cast(seq)
``` Convert the sequence with the dictionary and tuple type into k_lst, v_lst. ```
```
1. Tuple Lists
    [(A1, B1), (A2, B2), (A3, B3), (A4, B4)] --> k_lst[ A[i1, i2...] ], v_lst[ B[i1, i2...] ]
2. Dictionary Lists
    [{A1: B1}, {A2: B2}, {A3: B3}, {A4: B4}] --> k_lst[ A[i1, i2...] ], v_lst[ B[i1, i2...] ]
3. Dictionaries
    {A1: B1, A2: B2, A3: B3, A4: B4} -- > k_lst[ A[i1, i2...] ], v_lst[ B[i1, i2...] ]

In the context of Numpy and/or Pandas, ```pdcast(pddata)``` and ``` npcast(npdata)``` methods, provided in 0.19.2 are no log required. Please see the advanced example in README.

If your DataFrame returns a transposed list(such as, [ [1], [2], [3] ]), you have to tranpose it by yourself (make it like [ 1, 2, 3 ] ). This transpose operation applies to Radar, Parallel, HeatMap.

Series type
```python
from pyecharts import Bar
import pandas as pd

pddata = pd.Series([1, 2, 3, 4], index=[1, 'b', 'c', 'd'])
vlst, ilst = Bar.pdcast(pddata)

print(vlst)
>>> [1.0, 2.0, 3.0, 4.0] 
print(ilst)
>>> ['1', 'b', 'c', 'd']
```

DataFrame type
```python
from pyecharts import Bar
import pandas as pd

pddt = pd.DataFrame([[1, 2, 3, 4], [2, 3, 4, 5], [4.1, 5.2, 6.3, 7.4]], index=["A", "B", "C"])
vlst, ilst = Bar.pdcast(pddata)

print(vlst)
>>> [[1.0, 2.0, 3.0, 4.0], [2.0, 3.0, 4.0, 5.0], [4.1, 5.2, 6.3, 7.4]]
print(ilst)
>>> ['A', 'B', 'C']
```

npcast()，It accepts numpy.array type.
```python
@staticmethod
npcast(npdata)
``` handle the ndarray type in Numpy, return a list that ensures the correct type. Returns the nested list if there are multiple dimensions.```
```

Numpy.array type
```python
from pyecharts import Bar
import numpy ad np

npdata = np.array([[1, 2, 3, 4], [2, 4, 5.0, 6.3]])
print(npdata)
>>> [[1.0, 2.0, 3.0, 4.0], [2.0, 4.0, 5.0, 6.3]]
```

**Of course you can use the cooler way,use Jupyter Notebook to show the chart.But what matplotlib have，so do pyecharts**

like this

![notebook-0](https://github.com/chenjiandongx/pyecharts/blob/master/images/notebook-0.gif)

and this

![notebook-1](https://github.com/chenjiandongx/pyecharts/blob/master/images/notebook-1.gif)

more Jupyter notebook examples, please refer to [notebook-use-cases](https://github.com/chenjiandongx/pyecharts/blob/master/document/notebook-use-cases.ipynb)。you could download and run it on your notebook.

**Tip：** The function was official added in 0.1.9.2 version,please update the newest version to use it.

If you want use Jupyter Notebook to show your chart,just call Chart instance,compatible with Python2 and Python3's Jupyter Notebook environment at sametime.All the chart can display normaly,the same interaction experience to browser,there's no need to make a complex powerpoint!!

The parameter a chart type initialize accept（the same to all the chart type）.

* title -> str  
    default -> ''  
    The main title text, supporting for \n for newlines.
* subtitle -> str  
    defalut -> ''  
    Subtitle text, supporting for \n for newlines.
* width -> int  
    defalut -> 800(px)  
    Canvas width
* height -> int  
    defalut -> 400(px)  
    Canvas height
* title_pos -> str/int  
    defalut => 'left'  
    Distance between grid component and the left side of the container.title_pos value can be instant pixel value like 20;  
    it can also be percentage value relative to container width like '20%';it can also be 'left', 'center', or 'right'.  
    If the title_pos value is set to be 'left', 'center', or 'right',then the component will be aligned automatically based on position.
* title_top -> str/int  
    default -> 'top'  
    Distance between grid component and the top side of the container.top value can be instant pixel value like 20;  
    it can also be percentage value relative to container width like '20%';it can also be 'top', 'middle', or 'bottom'.  
    If the left value is set to be 'top', 'middle', or 'bottom',then the component will be aligned automatically based on position.
* title_color -> str  
    defalut -> '#000'  
    main title text color.  
* subtitle_color -> str  
    defalut -> '#aaa'  
    subtitle text color.
* title_text_size -> int  
    defalut -> 18  
    main title font size
* subtitle_text_size -> int  
    defalut -> 12  
    subtitle text color.
* background_color -> str  
    defalut -> '#fff'  
    Background color of title, which is transparent by default.  
    Color can be represented in RGB, for example 'rgb(128, 128, 128)'.RGBA can be used when you need alpha channel, for example 'rgba(128, 128, 128, 0.5)'.
    You may also use hexadecimal format, for example '#ccc'.
* is_grid -> bool  
    defalut -> False  
    It specifies whether to use the grid component. Detail [Customize](https://github.com/chenjiandongx/pyecharts/blob/master/document/en-us/documentation.md#Customize)

# Global-options
**Sitting general configuration in```add()```**

xyAxis：x, y axis in cartesian coordinate system(Line, Bar, Scatter, EffectScatter, Kline)

* is_convert -> bool  
    It specifies whether to convert xAxis and yAxis.
* xy_text_size -> int  
    axis name font size
* namegap -> int  
    Gap between axis name and axis line.
* x_axis -> list  
    xAxis data
* xaxis_name -> str  
    Name of xAxis
* xaxis_name_pos -> str  
    Location of xAxis name.It can be 'start'，'middle'，'end'
* xaxis_rotate -> int  
    Rotation degree of xaxis label, which is especially useful when there is no enough space for category axis.Rotation degree is from -90 to 90.
* xaxis_min -> int/float  
    The minimun value of xaxis.
* xaxis_max -> int/float  
    The maximun value of xaxis.
* xaxis_type -> str  
    Type of xaxis
    * 'value': Numerical axis, suitable for continuous data.
    * 'category': Category axis, suitable for discrete category data. Data should only be set via data for this type.
    * 'time': Time axis, suitable for continuous time series data. As compared to value axis,it has a better formatting for time and a different tick calculation method. For example,it decides to use month, week, day or hour for tick based on the range of span.
    * 'log': Log axis, suitable for log data.
* y_axis -> list  
    yAxis data
* yaxis_formatter -> str  
    Formatter of axis label, which supports string template and callback function.example: '{value} kg'
* yaxis_name -> str  
    Name of yAxis
* yaxis_name_pos -> str  
    Location of yAxis name.It can be 'start'，'middle'，'end'
* yaxis_rotate -> int  
    Rotation degree of xaxis label, which is especially useful when there is no enough space for category axis.Rotation degree is from -90 to 90.
* yaxis_min -> int/float  
    The minimun value of yaxis.
* yaxis_max -> int/float  
    The maximun value of yaxis.
* yaxis_type -> str  
    Type of yaxis
    * 'value': Numerical axis, suitable for continuous data.
    * 'category': Category axis, suitable for discrete category data. Data should only be set via data for this type.
    * 'time': Time axis, suitable for continuous time series data. As compared to value axis,it has a better formatting for time and a different tick calculation method. For example,it decides to use month, week, day or hour for tick based on the range of span.
    * 'log': Log axis, suitable for log data.
* interval -> int  
    The display interval of the axis scale label is valid in the category axis.By default, labels are displayed using labels that do not overlap the labels.  
    Set to 0 to force all labels to be displayed and label is one by one if setting as 1; If 2, it will be one label separates from each other, and so on.


dataZoom：dataZoom components for zoom-in and zoom-out. With them, it is possible to magnify a small area, to see the overall picture or to stay away from scattered points(Line, Bar, Scatter, EffectScatter, Kline)

* is_datazoom_show -> bool  
    defalut -> False  
    It specifies whether to use the datazoom component.
* datazoom_type -> str  
    defalut -> 'slider'  
    datazoom type, 'slider' or 'inside'
* datazoom_range -> list  
    defalut -> [50, 100]  
    The range percentage of the window out of the data extent, in the range of 0 ~ 100.
* datazoom_orient -> str  
    Specify whether the layout of dataZoom component is horizontal or vertical.'horizontal' or 'vertical'  
    What's more,it indicates whether the horizontal axis or vertical axis is controlled,by default in catesian coordinate system.


legend：legend component has different symbol, colour and name, and provide the interactive clicking functions to show or hide its associated data series.

* is_legend_show -> bool  
    defalut -> True  
    It specifies whether to show the legend component.
* legend_orient -> str  
    defalut -> 'horizontal'  
    The layout orientation of legend.It can be 'horizontal', 'vertical'
* legend_pos -> str  
    defalut -> 'center'  
    Distance between legend component and the left side of the container.  
    legend_pos value can be instant pixel value like 20;it can also be percentage value relative to container width like '20%';
    and it can also be 'left', 'center', or 'right'.
* legend_top -> str  
    defalut -> 'top'  
    Distance between legend component and the top side of the container.  
    legend_top value can be instant pixel value like 20;it can also be percentage value relative to container width like '20%';
    and it can also be 'top', 'middle', or 'bottom'.
* legend_selectedmode -> str/bool  
    State table of selected legend. 'single' or 'multiple'.or use False to disable it.


label：text string on the chart, for marking the charts with sensible details, such as value, name.

* is_label_show -> bool  
    defalut -> False
    It specifies whether to show laebl in normal status.
* is_emphasis -> bool  
    defalut -> False  
    It specifies whether to show laebl in emphasis status.
* label_pos -> str  
    defalut -> 'top'  
    Label position.It can be 'top', 'left', 'right', 'bottom', 'inside','outside'
* label_text_color -> str  
    defalut -> '#000'  
    Label text color.
* label_text_size -> int  
    defalut -> 12  
    Label font size.
* is_random -> bool  
    defalut -> False  
    It specifies whether to random global color list.
* label_color -> list  
    Customize the label color. It will modify Global color list, and all chart legend colors can be config here. Such as Bar's columnar color, Line's line color, and so on.
* formatter -> list  
    Data label formatter,it can be 'series', 'name', 'value', 'precent'

**Tip：** is_random random disorganize legend colour and list,it's kind of switch style? try it.


lineStyle：line style for Line, Polar, Radar, Graph, Parallel.

* line_width -> int  
    default -> 1
    Line width.
* line_opacity -> float  
    default -> 1  
    Opacity of the component. Supports value from 0 to 1, and the component will not be drawn when set to 0.
* line_curve -> float  
    default -> 0  
    Edge curvature, which supports value from 0 to 1. The larger the value, the greater the curvature. -> Graph
* line_type -> str  
    Line type,it can be 'solid', 'dashed', 'dotted'

grid3D：gird3D components in cartesian coordinate system(Bar3D, Line3D, Scatter3D)

* grid_width -> int  
    Width of grid component. Adaptive by default.
* grid_height -> int  
    Height of grid component. Adaptive by default.
* grid_top -> int/str  
    Distance between grid component and the top side of the container.  
    grid_top value can be instant pixel value like 20;it can also be percentage value relative to container width like '20%';and it can also be 'top', 'middle', or 'bottom'.  
    If the grid_top value is set to be 'top', 'middle', or 'bottom',then the component will be aligned automatically based on position.
* grid_bottom -> int/str  
    Distance between grid component and the bottom side of the container.  
    grid_bottom value can be instant pixel value like 20;it can also be percentage value relative to container width like '20%'.
* grid_left -> int/str  
    Distance between grid component and the left side of the container.  
    grid_left value can be instant pixel value like 20;it can also be percentage value relative to container width like '20%';and it can also be 'left', 'center', or 'right'.  
    If the grid_left value is set to be 'left', 'center', or 'right',then the component will be aligned automatically based on position.
* grid_right -> int/str  
    Distance between grid component and the right side of the container.  
    grid_right value can be instant pixel value like 20;it can also be percentage value relative to container width like '20%'.

visualMap：It is a type of component for visual encoding, which maps the data to visual channels.

* visual_type -> str  
    visual map type, 'color' or 'size'  
    color: For visual channel color, array is used, like: ['#333', '#78ab23', 'blue'],which means a color ribbon is formed based on the three color stops,and dataValues will be mapped to the ribbon.  
    size: For visual channel size, array is used, like: [20, 50],which means a size ribbon is formed based on the two value stops, and dataValues will be mapped to the ribbon.
* visual_range -> list  
    pecify the min and max dataValue for the visualMap component.
* visual_text_color -> str  
    visualMap text color.
* visual_range_text -> list  
    The label text on both ends, such as ['High', 'Low']
* visual_range_size -> list  
    For visual channel size, array is used, like: [20, 50].
* visual_range_color -> list  
    For visual channel color, array is used, like: ['#333', '#78ab23', 'blue'].
* visual_orient -> str  
    How to layout the visualMap component, 'horizontal' or 'vertical'.
* visual_pos -> str  
    Distance between visualMap component and the left side of the container.  
    visual_pos value can be instant pixel value like 20;it can also be percentage value relative to container width like '20%';and it can also be 'left', 'center', or 'right'.
* visual_top -> str  
    Distance between visualMap component and the top side of the container.  
    visual_top value can be instant pixel value like 20;it can also be percentage value relative to container width like '20%';and it can also be 'top', 'middle', or 'bottom'.
* is_calculable -> bool  
    Whether show handles, which can be dragged to adjust "selected range".


# Chart-types

## Bar
> Bar chart shows different data through the height of a bar,which is used in rectangular coordinate with at least 1 category axis.

Bar.add() signatures
```python
add(name, x_axis, y_axis, is_stack=False, **kwargs)
```
* name -> str  
    Series name used for displaying in tooltip and filtering with legend,or updaing data and configuration with setOption.
* x_axis -> list  
    data of xAixs
* y_axis -> list  
    data of yAxis
* is_stack -> bool  
    defalut -> False  
    It specifies whether to stack category axis.

```python
from pyecharts import Bar

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 75, 90]
v2 = [10, 25, 8, 60, 20, 80]
bar = Bar("柱状图数据堆叠示例")
bar.add("商家A", attr, v1, is_stack=True)
bar.add("商家B", attr, v2, is_stack=True)
bar.render()
```
![bar-0](https://github.com/chenjiandongx/pyecharts/blob/master/images/bar-0.gif)
**Tip：**  Global configuration item needs set in the last ```add()``` or the setting will lose efficacy.

```python
from pyecharts import Bar

bar = Bar("标记线和标记点示例")
bar.add("商家A", attr, v1, mark_point=["average"])
bar.add("商家B", attr, v2, mark_line=["min", "max"])
bar.render()
```
![bar-1](https://github.com/chenjiandongx/pyecharts/blob/master/images/bar-1.gif)

* mark_point -> list  
    mark point data, it can be 'min', 'max', 'average'
* mark_line  -> list  
    mark line data, it can be 'min', 'max', 'average'
* mark_point_symbol -> str  
    default -> 'pin'  
    mark symbol, it cna be 'circle', 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow'
* mark_point_symbolsize -> int  
    default -> 50  
    mark symbol size
* mark_point_textcolor -> str  
    default -> '#fff'  
    mark point text color

```python
from pyecharts import Bar

bar = Bar("x 轴和 y 轴交换")
bar.add("商家A", attr, v1)
bar.add("商家B", attr, v2, is_convert=True)
bar.render()
```
![bar-2](https://github.com/chenjiandongx/pyecharts/blob/master/images/bar-2.png)

dataZoom effect，'slider' type
```python
import random

attr = ["{}天".format(i) for i in range(30)]
v1 = [random.randint(1, 30) for _ in range(30)]
bar = Bar("Bar - datazoom - slider 示例")
bar.add("", attr, v1, is_label_show=True, is_datazoom_show=True)
bar.show_config()
bar.render()
```
![bar-4](https://github.com/chenjiandongx/pyecharts/blob/master/images/bar-4.gif)

'inside' type
```python
attr = ["{}天".format(i) for i in range(30)]
v1 = [random.randint(1, 30) for _ in range(30)]
bar = Bar("Bar - datazoom - inside 示例")
bar.add("", attr, v1, is_datazoom_show=True, datazoom_type='inside', datazoom_range=[10, 25])
bar.show_config()
bar.render()
```
![bar-5](https://github.com/chenjiandongx/pyecharts/blob/master/images/bar-5.gif)

**Tip：** Datazoom fits all plane rectangular coordinate system figure,that's(Line, Bar, Scatter, EffectScatter, Kline)
**Tip：** Through label_color to set column's colour,like ['#eee', '#000']，any type of chart's legend colour can revise by label_color .


## Bar3D
Bar3D.add() signatures
```
add(name, x_axis, y_axis, data, grid3D_opacity=1, grid3D_shading='color', **kwargs)
```
* name -> str  
    Series name used for displaying in tooltip and filtering with legend,or updaing data and configuration with setOption.
* x_axis -> list  
    xAxis data
* y_axis -> list  
    yAxis data
* data -> [[], []]
    zAxis data, it is represented by a two-dimension array.
* grid3D_opacity -> float  
    default -> 1  
    opacity of gird3D item
* grid3D_shading -> str  
    3D graphics coloring effect  
    * 'color': Only show color, not affected by lighting and other factors.
    * 'lambert': Through the classic lambert coloring to show the light and shade.
    * 'realistic': Realistic rendering.

```python
from pyecharts import Bar3D

bar3d = Bar3D("3D 柱状图示例", width=1200, height=600)
x_axis = ["12a", "1a", "2a", "3a", "4a", "5a", "6a", "7a", "8a", "9a", "10a", "11a",
          "12p", "1p", "2p", "3p", "4p", "5p", "6p", "7p", "8p", "9p", "10p", "11p"]
y_aixs = ["Saturday", "Friday", "Thursday", "Wednesday", "Tuesday", "Monday", "Sunday"]
data = [[0, 0, 5], [0, 1, 1], [0, 2, 0], [0, 3, 0], [0, 4, 0], [0, 5, 0], [0, 6, 0], [0, 7, 0],
        [0, 8, 0],[0, 9, 0], [0, 10, 0], [0, 11, 2], [0, 12, 4], [0, 13, 1], [0, 14, 1], [0, 15, 3],
        [0, 16, 4], [0, 17, 6], [0, 18, 4], [0, 19, 4], [0, 20, 3], [0, 21, 3], [0, 22, 2], [0, 23, 5],
        [1, 0, 7], [1, 1, 0], [1, 2, 0], [1, 3, 0], [1, 4, 0], [1, 5, 0], [1, 6, 0], [1, 7, 0], [1, 8, 0],
        [1, 9, 0], [1, 10, 5], [1, 11, 2], [1, 12, 2], [1, 13, 6], [1, 14, 9], [1, 15, 11], [1, 16, 6], [1, 17, 7],
        [1, 18, 8], [1, 19, 12], [1, 20, 5], [1, 21, 5], [1, 22, 7], [1, 23, 2], [2, 0, 1], [2, 1, 1],
        [2, 2, 0], [2, 3, 0], [2, 4, 0], [2, 5, 0], [2, 6, 0], [2, 7, 0], [2, 8, 0], [2, 9, 0], [2, 10, 3],
        [2, 11, 2], [2, 12, 1], [2, 13, 9], [2, 14, 8], [2, 15, 10], [2, 16, 6], [2, 17, 5], [2, 18, 5],
        [2, 19, 5], [2, 20, 7], [2, 21, 4], [2, 22, 2], [2, 23, 4], [3, 0, 7], [3, 1, 3], [3, 2, 0], [3, 3, 0],
        [3, 4, 0], [3, 5, 0], [3, 6, 0], [3, 7, 0], [3, 8, 1], [3, 9, 0], [3, 10, 5], [3, 11, 4], [3, 12, 7],
        [3, 13, 14], [3, 14, 13], [3, 15, 12], [3, 16, 9], [3, 17, 5], [3, 18, 5], [3, 19, 10], [3, 20, 6],
        [3, 21, 4], [3, 22, 4], [3, 23, 1], [4, 0, 1], [4, 1, 3], [4, 2, 0], [4, 3, 0], [4, 4, 0], [4, 5, 1],
        [4, 6, 0], [4, 7, 0], [4, 8, 0], [4, 9, 2], [4, 10, 4], [4, 11, 4], [4, 12, 2], [4, 13, 4], [4, 14, 4],
        [4, 15, 14], [4, 16, 12], [4, 17, 1], [4, 18, 8], [4, 19, 5], [4, 20, 3], [4, 21, 7], [4, 22, 3],
        [4, 23, 0], [5, 0, 2], [5, 1, 1], [5, 2, 0], [5, 3, 3], [5, 4, 0], [5, 5, 0], [5, 6, 0], [5, 7, 0],
        [5, 8, 2], [5, 9, 0], [5, 10, 4], [5, 11, 1], [5, 12, 5], [5, 13, 10], [5, 14, 5], [5, 15, 7], [5, 16, 11],
        [5, 17, 6], [5, 18, 0], [5, 19, 5], [5, 20, 3], [5, 21, 4], [5, 22, 2], [5, 23, 0], [6, 0, 1], [6, 1, 0],
        [6, 2, 0], [6, 3, 0], [6, 4, 0], [6, 5, 0], [6, 6, 0], [6, 7, 0], [6, 8, 0], [6, 9, 0], [6, 10, 1],
        [6, 11, 0], [6, 12, 2], [6, 13, 1], [6, 14, 3], [6, 15, 4], [6, 16, 0], [6, 17, 0], [6, 18, 0], [6, 19, 0],
        [6, 20, 1], [6, 21, 2], [6, 22, 2], [6, 23, 6]]
range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
               '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
bar3d.add("", x_axis, y_aixs, [[d[1], d[0], d[2]] for d in data], is_visualmap=True,
          visual_range=[0, 20], visual_range_color=range_color, grid3D_width=200, grid3D_depth=80)
bar3d.show_config()
bar3d.render()
```
![bar3D-0](https://github.com/chenjiandongx/pyecharts/blob/master/images/bar3D-0.gif)

``` grid3D_shading``` could make bar look more real  
```python
bar3d = Bar3D("3D 柱状图示例", width=1200, height=600)
bar3d.add("", x_axis, y_aixs, [[d[1], d[0], d[2]] for d in data], is_visualmap=True,
          visual_range=[0, 20], visual_range_color=range_color, grid3D_width=200, grid3D_depth=80,
          grid3D_shading='lambert')
bar3d.show_config()
bar3d.render()
```
![bar3D-1](https://github.com/chenjiandongx/pyecharts/blob/master/images/bar3D-1.gif)

```is_grid3D_rotate``` could let it rotate automatically
```python
bar3d = Bar3D("3D 柱状图示例", width=1200, height=600)
bar3d.add("", x_axis, y_aixs, [[d[1], d[0], d[2]] for d in data], is_visualmap=True,
          visual_range=[0, 20], visual_range_color=range_color, grid3D_width=200, grid3D_depth=80,
          is_grid3D_rotate=True)
bar3d.show_config()
bar3d.render()
```
![bar3D-2](https://github.com/chenjiandongx/pyecharts/blob/master/images/bar3D-2.gif)

set ``` grid3D_rotate_speed``` to adjust the rotation speed  
```python
bar3d = Bar3D("3D 柱状图示例", width=1200, height=600)
bar3d.add("", x_axis, y_aixs, [[d[1], d[0], d[2]] for d in data], is_visualmap=True,
          visual_range=[0, 20], visual_range_color=range_color, grid3D_width=200, grid3D_depth=80,
          is_grid3D_rotate=True, grid3D_rotate_speed=180)
bar3d.show_config()
bar3d.render()
```
![bar3D-3](https://github.com/chenjiandongx/pyecharts/blob/master/images/bar3D-3.gif)

**Tip：** more details aboutt gird3D，please refer to [Global-options](https://github.com/chenjiandongx/pyecharts/blob/master/document/en-us/documentation.md#Global-options)


## EffectScatter
> The scatter graph with ripple animation. The special animation effect can visually highlights some data.

EffectScatter.add() signatures
```python
add(name, x_value, y_value, symbol_size=10, **kwargs)
```
* name -> str  
    Series name used for displaying in tooltip and filtering with legend,or updaing data and configuration with setOption.
* x_axis -> list  
    data of xAxis
* y_axis -> list  
    data of yAxis  
* symbol_size -> int  
    default -> 10  
    symbol size

```python
from pyecharts import EffectScatter

v1 = [10, 20, 30, 40, 50, 60]
v2 = [25, 20, 15, 10, 60, 33]
es = EffectScatter("动态散点图示例")
es.add("effectScatter", v1, v2)
es.render()
```
![effectscatter-0](https://github.com/chenjiandongx/pyecharts/blob/master/images/effectscatter-0.gif)

```python
es = EffectScatter("动态散点图各种图形示例")
es.add("", [10], [10], symbol_size=20, effect_scale=3.5, effect_period=3, symbol="pin")
es.add("", [20], [20], symbol_size=12, effect_scale=4.5, effect_period=4,symbol="rect")
es.add("", [30], [30], symbol_size=30, effect_scale=5.5, effect_period=5,symbol="roundRect")
es.add("", [40], [40], symbol_size=10, effect_scale=6.5, effect_brushtype='fill',symbol="diamond")
es.add("", [50], [50], symbol_size=16, effect_scale=5.5, effect_period=3,symbol="arrow")
es.add("", [60], [60], symbol_size=6, effect_scale=2.5, effect_period=3,symbol="triangle")
es.render()
```
![effectscatter-1](https://github.com/chenjiandongx/pyecharts/blob/master/images/effectscatter-1.gif)

* symbol -> str  
    symbol shape, it can be 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow'
* effect_brushtype -> str   
    default -> 'stroke'  
    The brush type for ripples. options: 'stroke' and 'fill'.
* effect_scale -> float  
    default -> 2.5  
    The maximum zooming scale of ripples in animation.
* effect_period -> float  
    default -> 4(s)  
    The duration of animation.


## Funnel
Funnel.add() signatures
```python
add(name, attr, value, **kwargs)
```
* name -> str  
    Series name used for displaying in tooltip and filtering with legend,or updaing data and configuration with setOption.
* attr -> list  
    name of attribute
* value -> list  
    value of attribute

```python
from pyecharts import Funnel

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
value = [20, 40, 60, 80, 100, 120]
funnel = Funnel("漏斗图示例")
funnel.add("商品", attr, value, is_label_show=True, label_pos="inside", label_text_color="#fff")
funnel.render()
```
![funnel-0](https://github.com/chenjiandongx/pyecharts/blob/master/images/funnel-0.gif)

```python
funnel = Funnel("漏斗图示例", width=600, height=400, title_pos='center')
funnel.add("商品", attr, value, is_label_show=True, label_pos="outside", legend_orient='vertical',
           legend_pos='left')
funnel.show_config()
funnel.render()
```
![funnel-1](https://github.com/chenjiandongx/pyecharts/blob/master/images/funnel-1.png)


## Gauge
Gauge.add() signatures
```python
add(name, attr, value, scale_range=None, angle_range=None, **kwargs)
```
* name -> str  
    Series name used for displaying in tooltip and filtering with legend,or updaing data and configuration with setOption.
* attr -> list  
    name of attribute
* value -> list  
    value of attribute
* scale_range -> list  
    default -> [0, 100]  
    data range of guage
* angle_range -> list  
    default -> [225, -45]  
    angle range of guage.The direct right side of circle center is 0 degree,the right above it is 90 degree, the direct left side of it is 180 degree.

```python
from pyecharts import Gauge

gauge = Gauge("仪表盘示例")
gauge.add("业务指标", "完成率", 66.66)
gauge.show_config()
gauge.render()
```
![gauge-0](https://github.com/chenjiandongx/pyecharts/blob/master/images/gauge-0.png)

```python
gauge = Gauge("仪表盘示例")
gauge.add("业务指标", "完成率", 166.66, angle_range=[180, 0], scale_range=[0, 200], is_legend_show=False)
gauge.show_config()
gauge.render()
```
![gauge-1](https://github.com/chenjiandongx/pyecharts/blob/master/images/gauge-1.png)


## Geo
> Geographic coorinate system component.Geographic coorinate system component is used to draw maps, which also supports scatter series, and line series.

Geo.add() signatures
```python
add(name, attr, value, type="scatter", maptype='china', symbol_size=12, border_color="#111",
    geo_normal_color="#323c48", geo_emphasis_color="#2a333d", **kwargs)
```
* name -> str  
    Series name used for displaying in tooltip and filtering with legend,or updaing data and configuration with setOption.
* attr -> list  
    name of attribute
* value -> list  
    value of attribute
* type -> str  
    default -> 'scatter'  
    chart type, it can be 'scatter', 'effectscatter', 'heatmap'
* maptype -> str  
    type of map, it only supports 'china' temporarily.
* symbol_size -> int  
    default -> 12  
    symbol size
* border_color -> str  
    default -> '#111'  
    color of map border
* geo_normal_color -> str  
    default -> '#323c48'  
    The color of the map area in normal state
* geo_emphasis_color -> str  
    default -> '#2a333d'  
    The color of the map area in emphasis state

Scatter type
```python
from pyecharts import Geo

data = [
    ("海门", 9),("鄂尔多斯", 12),("招远", 12),("舟山", 12),("齐齐哈尔", 14),("盐城", 15),
    ("赤峰", 16),("青岛", 18),("乳山", 18),("金昌", 19),("泉州", 21),("莱西", 21),
    ("日照", 21),("胶南", 22),("南通", 23),("拉萨", 24),("云浮", 24),("梅州", 25),
    ("文登", 25),("上海", 25),("攀枝花", 25),("威海", 25),("承德", 25),("厦门", 26),
    ("汕尾", 26),("潮州", 26),("丹东", 27),("太仓", 27),("曲靖", 27),("烟台", 28),
    ("福州", 29),("瓦房店", 30),("即墨", 30),("抚顺", 31),("玉溪", 31),("张家口", 31),
    ("阳泉", 31),("莱州", 32),("湖州", 32),("汕头", 32),("昆山", 33),("宁波", 33),
    ("湛江", 33),("揭阳", 34),("荣成", 34),("连云港", 35),("葫芦岛", 35),("常熟", 36),
    ("东莞", 36),("河源", 36),("淮安", 36),("泰州", 36),("南宁", 37),("营口", 37),
    ("惠州", 37),("江阴", 37),("蓬莱", 37),("韶关", 38),("嘉峪关", 38),("广州", 38),
    ("延安", 38),("太原", 39),("清远", 39),("中山", 39),("昆明", 39),("寿光", 40),
    ("盘锦", 40),("长治", 41),("深圳", 41),("珠海", 42),("宿迁", 43),("咸阳", 43),
    ("铜川", 44),("平度", 44),("佛山", 44),("海口", 44),("江门", 45),("章丘", 45),
    ("肇庆", 46),("大连", 47),("临汾", 47),("吴江", 47),("石嘴山", 49),("沈阳", 50),
    ("苏州", 50),("茂名", 50),("嘉兴", 51),("长春", 51),("胶州", 52),("银川", 52),
    ("张家港", 52),("三门峡", 53),("锦州", 54),("南昌", 54),("柳州", 54),("三亚", 54),
    ("自贡", 56),("吉林", 56),("阳江", 57),("泸州", 57),("西宁", 57),("宜宾", 58),
    ("呼和浩特", 58),("成都", 58),("大同", 58),("镇江", 59),("桂林", 59),("张家界", 59),
    ("宜兴", 59),("北海", 60),("西安", 61),("金坛", 62),("东营", 62),("牡丹江", 63),
    ("遵义", 63),("绍兴", 63),("扬州", 64),("常州", 64),("潍坊", 65),("重庆", 66),
    ("台州", 67),("南京", 67),("滨州", 70),("贵阳", 71),("无锡", 71),("本溪", 71),
    ("克拉玛依", 72),("渭南", 72),("马鞍山", 72),("宝鸡", 72),("焦作", 75),("句容", 75),
    ("北京", 79),("徐州", 79),("衡水", 80),("包头", 80),("绵阳", 80),("乌鲁木齐", 84),
    ("枣庄", 84),("杭州", 84),("淄博", 85),("鞍山", 86),("溧阳", 86),("库尔勒", 86),
    ("安阳", 90),("开封", 90),("济南", 92),("德阳", 93),("温州", 95),("九江", 96),
    ("邯郸", 98),("临安", 99),("兰州", 99),("沧州", 100),("临沂", 103),("南充", 104),
    ("天津", 105),("富阳", 106),("泰安", 112),("诸暨", 112),("郑州", 113),("哈尔滨", 114),
    ("聊城", 116),("芜湖", 117),("唐山", 119),("平顶山", 119),("邢台", 119),("德州", 120),
    ("济宁", 120),("荆州", 127),("宜昌", 130),("义乌", 132),("丽水", 133),("洛阳", 134),
    ("秦皇岛", 136),("株洲", 143),("石家庄", 147),("莱芜", 148),("常德", 152),("保定", 153),
    ("湘潭", 154),("金华", 157),("岳阳", 169),("长沙", 175),("衢州", 177),("廊坊", 193),
    ("菏泽", 194),("合肥", 229),("武汉", 273),("大庆", 279)]

geo = Geo("全国主要城市空气质量", "data from pm2.5", title_color="#fff", title_pos="center",
width=1200, height=600, background_color='#404a59')
attr, value = geo.cast(data)
geo.add("", attr, value, visual_range=[0, 200], visual_text_color="#fff", symbol_size=15, is_visualmap=True)
geo.show_config()
geo.render()
```
![geo-0](https://github.com/chenjiandongx/pyecharts/blob/master/images/geo-0.gif)

visualMap：visualMap is a type of component for visual encoding, which maps the data to visual channels
* is_visualmap -> bool  
    It specifies whether to use the datazoom component.
* visual_range -> list  
    default -> [0, 100]  
    pecify the min and max dataValue for the visualMap component.
* visual_text_color -> list  
    visualMap text color.
* visual_range_text -> list  
    The label text on both ends, such as ['High', 'Low']
* visual_range_color -> list  
    default ->  ['#50a3ba', '#eac763', '#d94e5d']  
    For visual channel color, array is used, like: ['#333', '#78ab23', 'blue'],which means a color ribbon is formed based on the three color stops,and dataValues will be mapped to the ribbon.  
    Specifically,the dataValue that equals to visualMap.min will be mapped onto '#333',the dataValue that equals to visualMap.max will be mapped onto 'blue',and other dataValues will be piecewisely interpolated to get the final color.
* visual_orient -> str  
    default -> 'vertical'  
    How to layout the visualMap component, 'horizontal' or 'vertical'.
* visual_pos -> str/int  
    default -> 'left'  
    Distance between visualMap component and the left side of the container.  
    visual_pos value can be instant pixel value like 20;it can also be percentage value relative to container width like '20%';and it can also be 'left', 'center', or 'right'.
* visual_top -> str/int  
    default -> 'top'  
    Distance between visualMap component and the top side of the container.  
    visual_top value can be instant pixel value like 20;it can also be percentage value relative to container width like '20%';and it can also be 'top', 'middle', or 'bottom'.
* is_calculable -> bool  
    default -> True  
    Whether show handles, which can be dragged to adjust "selected range".

HeatMap type
```python
geo = Geo("全国主要城市空气质量", "data from pm2.5", title_color="#fff", title_pos="center", width=1200, height=600,
          background_color='#404a59')
attr, value = geo.cast(data)
geo.add("", attr, value, type="heatmap", is_visualmap=True, visual_range=[0, 300], visual_text_color='#fff')
geo.show_config()
geo.render()
```
![geo-0-1](https://github.com/chenjiandongx/pyecharts/blob/master/images/geo-0-1.gif)

EffectScatter type
```python
from pyecharts import Geo

data = [("海门", 9), ("鄂尔多斯", 12), ("招远", 12), ("舟山", 12), ("齐齐哈尔", 14), ("盐城", 15)]
geo = Geo("全国主要城市空气质量", "data from pm2.5", title_color="#fff", title_pos="center",
          width=1200, height=600, background_color='#404a59')
attr, value = geo.cast(data)
geo.add("", attr, value, type="effectScatter", is_random=True, effect_scale=5)
geo.show_config()
geo.render()
```
![geo-1](https://github.com/chenjiandongx/pyecharts/blob/master/images/geo-1.gif)


## Graph
> Graph is a diagram to represent nodes and the links connecting nodes.

Graph.add() signatures
```python
add(name, nodes, links, categories=None, is_focusnode=True, is_roam=True, is_rotatelabel=False,
    layout="force", edge_length=50, gravity=0.2, repulsion=50, **kwargs)
```
* name -> str  
    Series name used for displaying in tooltip and filtering with legend,or updaing data and configuration with setOption.
* nodes -> dict  
    Relational nodes data
    * name：Name of data item.     # required！！
    * x：x value of node position.
    * y：y value of node position.
    * value：value of data item.
    * category：Index of category which the data item belongs to.
    * symbol：Symbol of node of this category.Includes 'circle', 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow'
    * symbolSize：symbol size
* links -> dict  
    Relational data between nodes
    * source：name of source node on edge      # required！！
    * target：name of target node on edge      # required！！
    * vaule：value of edge,It can be used in the force layout to map to the length of the edge
* categories -> list  
    Name of category, which is used to correspond with legend and the content of tooltip.
* is_focusnode -> bool  
    defalut -> True  
    Whether to focus/highlight the hover node and it's adjacencies.
* is_roam -> bool/str  
    default -> True  
    Whether to enable mouse zooming and translating.  
    If either zooming or translating is wanted,it can be set to 'scale' or 'move'. Otherwise, set it to be true to enable both.
* is_rotatelabel -> bool  
    default -> False  
    Whether to rotate the label automatically.
* layout -> str  
    Graph layout.  
    default -> 'force'  
    * none：No any layout, use x, y provided in node as the position of node.
    * circular：Adopt circular layout, see the example Les Miserables.
    * force：Adopt force-directed layout, see the example Force,the detail about configrations of layout are in graph.force
* edge_length -> int  
    default -> 50  
    The distance between 2 nodes on edge. This distance is also affected by repulsion.  
    It can be an array to represent the range of edge length.In this case edge with larger value will be shorter, which means two nodes are closer. And edge with smaller value will be longer.
* gravity -> int/float  
    default -> 0.2  
    The gravity factor enforcing nodes approach to the center.The nodes will be closer to the center as the value becomes larger.
* repulsion -> int  
    default -> 50  
    The repulsion factor between nodes. The repulsion will be stronger and the distance between 2 nodes becomes further as this value becomes larger.
    It can be an array to represent the range of repulsion.  
    In this case larger value have larger repulsion and smaller value will have smaller repulsion.

```python
from pyecharts import Graph

nodes = [{"name": "结点1", "symbolSize": 10},
         {"name": "结点2", "symbolSize": 20},
         {"name": "结点3", "symbolSize": 30},
         {"name": "结点4", "symbolSize": 40},
         {"name": "结点5", "symbolSize": 50},
         {"name": "结点6", "symbolSize": 40},
         {"name": "结点7", "symbolSize": 30},
         {"name": "结点8", "symbolSize": 20}]
links = []
for i in nodes:
    for j in nodes:
        links.append({"source": i.get('name'), "target": j.get('name')})
graph = Graph("关系图-力引导布局示例")
graph.add("", nodes, links, repulsion=8000)
graph.show_config()
graph.render()

```
![graph-0](https://github.com/chenjiandongx/pyecharts/blob/master/images/graph-0.png)

```python
graph = Graph("关系图-环形布局示例")
graph.add("", nodes, links, is_label_show=True, repulsion=8000, layout='circular', label_text_color=None)
graph.show_config()
graph.render()
```
![graph-1](https://github.com/chenjiandongx/pyecharts/blob/master/images/graph-1.png)

```python
from pyecharts import Graph

import json
with open("..\json\weibo.json", "r", encoding="utf-8") as f:
    j = json.load(f)
    nodes, links, categories, cont, mid, userl = j
graph = Graph("微博转发关系图", width=1200, height=600)
graph.add("", nodes, links, categories, label_pos="right", repulsion=50, is_legend_show=False,
          line_curve=0.2, label_text_color=None)
graph.show_config()
graph.render()
```
![graph-2](https://github.com/chenjiandongx/pyecharts/blob/master/images/graph-2.gif)

**Tip：** **lineStyle** parameter is configurable


# HeatMap
> Heat map mainly use colors to represent values, which must be used along with visualMap component.
> It can be used in either rectangular coordinate or geographic coordinate.But the behaviour on them are quite different. Rectangular coordinate must have two catagories to use it.

HeatMap.add() signatures
```python
add(name, x_axis, y_axis, data, **kwargs)
```
* name -> str  
    Series name used for displaying in tooltip and filtering with legend,or updaing data and configuration with setOption.
* x_axis -> str  
    data of xAxis, it must be catagory axis.
* y_axis -> str  
    data of yAxis, it must be catagory axis.
* data -> [[],[]]  
    data array of series, it is represented by a two-dimension array
```python
import random
from pyecharts import HeatMap

x_axis = ["12a", "1a", "2a", "3a", "4a", "5a", "6a", "7a", "8a", "9a", "10a", "11a",
          "12p", "1p", "2p", "3p", "4p", "5p", "6p", "7p", "8p", "9p", "10p", "11p"]
y_aixs = ["Saturday", "Friday", "Thursday", "Wednesday", "Tuesday", "Monday", "Sunday"]
data = [[i, j, random.randint(0, 50)] for i in range(24) for j in range(7)]
heatmap = HeatMap()
heatmap.add("热力图直角坐标系", x_axis, y_aixs, data, is_visualmap=True,
            visual_text_color="#000", visual_orient='horizontal')
heatmap.show_config()
heatmap.render()
```
![heatmap-0](https://github.com/chenjiandongx/pyecharts/blob/master/images/heatmap-0.gif)

**Tip：** Thermodynamic chart have to cooperate with VisualMap in use.


## Kline
> Kline chart use red to imply increasing with red and decreasing with blue

Kline.add() signatures
```python
add(name, x_axis, y_axis, **kwargs)
```
* name -> str  
    Series name used for displaying in tooltip and filtering with legend,or updaing data and configuration with setOption.
* x_axis -> list  
    data of xAxis
* y_axis -> [[], []]  
    data pf yAxis.Data should be the two-dimensional array shown as follow.  
    Every data item (each line in the example above) represents a box, which contains 4 values. They are: [open, close, lowest, highest]  (namely: [opening value, closing value, lowest value, highest value])
```python
from pyecharts import Kline

v1 = [[2320.26, 2320.26, 2287.3, 2362.94], [2300, 2291.3, 2288.26, 2308.38],
      [2295.35, 2346.5, 2295.35, 2345.92], [2347.22, 2358.98, 2337.35, 2363.8],
      [2360.75, 2382.48, 2347.89, 2383.76], [2383.43, 2385.42, 2371.23, 2391.82],
      [2377.41, 2419.02, 2369.57, 2421.15], [2425.92, 2428.15, 2417.58, 2440.38],
      [2411, 2433.13, 2403.3, 2437.42], [2432.68, 2334.48, 2427.7, 2441.73],
      [2430.69, 2418.53, 2394.22, 2433.89], [2416.62, 2432.4, 2414.4, 2443.03],
      [2441.91, 2421.56, 2418.43, 2444.8], [2420.26, 2382.91, 2373.53, 2427.07],
      [2383.49, 2397.18, 2370.61, 2397.94], [2378.82, 2325.95, 2309.17, 2378.82],
      [2322.94, 2314.16, 2308.76, 2330.88], [2320.62, 2325.82, 2315.01, 2338.78],
      [2313.74, 2293.34, 2289.89, 2340.71], [2297.77, 2313.22, 2292.03, 2324.63],
      [2322.32, 2365.59, 2308.92, 2366.16], [2364.54, 2359.51, 2330.86, 2369.65],
      [2332.08, 2273.4, 2259.25, 2333.54], [2274.81, 2326.31, 2270.1, 2328.14],
      [2333.61, 2347.18, 2321.6, 2351.44], [2340.44, 2324.29, 2304.27, 2352.02],
      [2326.42, 2318.61, 2314.59, 2333.67], [2314.68, 2310.59, 2296.58, 2320.96],
      [2309.16, 2286.6, 2264.83, 2333.29], [2282.17, 2263.97, 2253.25, 2286.33],
      [2255.77, 2270.28, 2253.31, 2276.22]]
kline = Kline("K 线图示例")
kline.add("日K", ["2017/7/{}".format(i + 1) for i in range(31)], v1)
kline.show_config()
kline.render()
```
![kline-0](https://github.com/chenjiandongx/pyecharts/blob/master/images/kline-0.png)

Kline + dataZoom
```python
kline = Kline("K 线图示例")
kline.add("日K", ["2017/7/{}".format(i + 1) for i in range(31)], v1, mark_point=["max"], is_datazoom_show=True)
kline.show_config()
kline.render()
```
![kline-1](https://github.com/chenjiandongx/pyecharts/blob/master/images/kline-1.gif)


## Line
> Broken line chart relates all the data points symbol by broken lines,
> which is used to show the trend of data changing.It could be used in both rectangular coordinate and polar coordinate.

Line.add() signatures
```python
add(name, x_axis, y_axis, is_symbol_show=True, is_smooth=False, is_stack=False,
    is_step=False, is_fill=False, **kwargs)
```
* name -> str  
    Series name used for displaying in tooltip and filtering with legend,or updaing data and configuration with setOption.
* x_axis -> list  
    data of xAxis
* y_axis -> list  
    data of yAxis
* is_symbol_show -> bool  
    default -> True  
    It specifies whether to show the symbol.
* is_smooth -> bool
    default -> False
    Whether to show as smooth curve.
* is_stack -> bool  
    default -> Flase  
    It specifies whether to stack category axis.
* is_step -> bool/str  
    default -> False  
    Whether to show as a step line.It can be true, false. Or 'start', 'middle', 'end'.Which will configure the turn point of step line.
* is_fill -> bool  
    default -> False  
    Whether to fill area.

```python
from pyecharts import Line

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 10, 100]
v2 = [55, 60, 16, 20, 15, 80]
line = Line("折线图示例")
line.add("商家A", attr, v1, mark_point=["average"])
line.add("商家B", attr, v2, is_smooth=True, mark_line=["max", "average"])
line.show_config()
line.render()
```
![line-0](https://github.com/chenjiandongx/pyecharts/blob/master/images/line-0.gif)

* mark_point -> list  
    mark point data, it can be 'min', 'max', 'average'
* mark_line  -> list  
    mark line data, it can be 'min', 'max', 'average'
* mark_point_symbol -> str  
    default -> 'pin'  
    mark symbol, it cna be 'circle', 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow'
* mark_point_symbolsize -> int  
    default -> 50  
    mark symbol size
* mark_point_textcolor -> str  
    default -> '#fff'  
    mark point text color

Other Configurations Of Marker Point
```python
line = Line("折线图示例")
line.add("商家A", attr, v1, mark_point=["average", "max", "min"],
         mark_point_symbol='diamond', mark_point_textcolor='#40ff27')
line.add("商家B", attr, v2, mark_point=["average", "max", "min"],
         mark_point_symbol='arrow', mark_point_symbolsize=40)
line.show_config()
line.render()
```
![line-0-1](https://github.com/chenjiandongx/pyecharts/blob/master/images/line-0-1.png)

```python
line = Line("折线图-数据堆叠示例")
line.add("商家A", attr, v1, is_stack=True, is_label_show=True)
line.add("商家B", attr, v2, is_stack=True, is_label_show=True)
line.show_config()
line.render()
```
![line-1](https://github.com/chenjiandongx/pyecharts/blob/master/images/line-1.gif)

```python
line = Line("折线图-阶梯图示例")
line.add("商家A", attr, v1, is_step=True, is_label_show=True)
line.show_config()
line.render()
```
![line-2](https://github.com/chenjiandongx/pyecharts/blob/master/images/line-2.png)

```python
line = Line("折线图-面积图示例")
line.add("商家A", attr, v1, is_fill=True, line_opacity=0.2, area_opacity=0.4, symbol=None)
line.add("商家B", attr, v2, is_fill=True, area_color='#000', area_opacity=0.3, is_smooth=True)
line.show_config()
line.render()
```
![line-3](https://github.com/chenjiandongx/pyecharts/blob/master/images/line-3.png)

* area_opacity -> float  
    Opacity of the component. Supports value from 0 to 1, and the component will not be drawn when set to 0.
* area_color -> str  
    Fill color.

**Tip：** **lineStyle** Parameter is Configurable
**Tip：** Setting line colour by label_color,like ['#eee', '#000'],all type of chart can revise label colour by label_color.


# Line3D
Line3D.add() signatures
```python
add(name, data, grid3D_opacity=1, **kwargs)
```
* name -> str
    Series name used for displaying in tooltip and filtering with legend,or updaing data and configuration with setOption.
* data -> [[], []]  
    data of line3D
* grid3D_opacity -> float  
    default -> 1  
    opacity of gird3D item

draw a spring
```python
from pyecharts import Line3D

import math
_data = []
for t in range(0, 25000):
    _t = t / 1000
    x = (1 + 0.25 * math.cos(75 * _t)) * math.cos(_t)
    y = (1 + 0.25 * math.cos(75 * _t)) * math.sin(_t)
    z = _t + 2.0 * math.sin(75 * _t)
    _data.append([x, y, z])
range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
               '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
line3d = Line3D("3D 折线图示例", width=1200, height=600)
line3d.add("", _data, is_visualmap=True, visual_range_color=range_color, visual_range=[0, 30],
           grid3D_rotate_sensitivity=5)
line3d.render()
```
![line3D-0](https://github.com/chenjiandongx/pyecharts/blob/master/images/line3D-0.gif)

rotating spring
```python
from pyecharts import Line3D

import math
_data = []
for t in range(0, 25000):
    _t = t / 1000
    x = (1 + 0.25 * math.cos(75 * _t)) * math.cos(_t)
    y = (1 + 0.25 * math.cos(75 * _t)) * math.sin(_t)
    z = _t + 2.0 * math.sin(75 * _t)
    _data.append([x, y, z])
range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
               '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
line3d = Line3D("3D 折线图示例", width=1200, height=600)
line3d.add("", _data, is_visualmap=True, visual_range_color=range_color, visual_range=[0, 30],
           is_grid3D_rotate=True, grid3D_rotate_speed=180)
line3d.render()
```
![line3D-1](https://github.com/chenjiandongx/pyecharts/blob/master/images/line3D-1.gif)

**Tip：** more details aboutt gird3D，please refer to [Global-options](https://github.com/chenjiandongx/pyecharts/blob/master/document/en-us/documentation.md#Global-options)

## Liquid
> Liquid chart is usually used to represent data in percentage.

Liquid.add() signatures
```python
add(name, data, shape='circle', liquid_color=None, is_liquid_animation=True,
    is_liquid_outline_show=True, **kwargs)
```
* name -> str  
    Series name used for displaying in tooltip and filtering with legend,or updaing data and configuration with setOption.
* data -> list  
    data of liquid,[0.6, 0.5, 0.4, 0.3] -> This creates a chart wit waves at position of 60%, 50%, 40%, and 30%.
* shape -> str  
    Shape of water fill chart.It can be one of the default symbols: 'circle', 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow'
* liquid_color -> list  
    default -> ['#294D99', '#156ACF', '#1598ED', '#45BDFF']  
    To set colors for liquid fill chart series, set color to be an array of colors.
* is_liquid_animation -> bool  
    default -> True  
    Whether disable animation.
* is_liquid_outline_show -> bool  
    default -> True  
    whether hide the outline

```python
from pyecharts import Liquid

liquid = Liquid("水球图示例")
liquid.add("Liquid", [0.6])
liquid.show_config()
liquid.render()
```
![liquid-0](https://github.com/chenjiandongx/pyecharts/blob/master/images/liquid-0.gif)

```python
from pyecharts import Liquid

liquid = Liquid("水球图示例")
liquid.add("Liquid", [0.6, 0.5, 0.4, 0.3], is_liquid_outline_show=False)
liquid.show_config()
liquid.render()
```
![liquid-1](https://github.com/chenjiandongx/pyecharts/blob/master/images/liquid-1.gif)

```python
from pyecharts import Liquid

liquid = Liquid("水球图示例")
liquid.add("Liquid", [0.6, 0.5, 0.4, 0.3], is_liquid_animation=False, shape='diamond')
liquid.show_config()
liquid.render()
```
![liquid-2](https://github.com/chenjiandongx/pyecharts/blob/master/images/liquid-2.png)

## Map
> Map is maily used in the visulization of geographic area data,which can be used with visualMap component to visualize the datas such as population distribution density in diffrent areas.

Map.add() signatures
```python
add(name, attr, value, is_roam=True, maptype='china', **kwargs)
```
* name -> str  
    Series name used for displaying in tooltip and filtering with legend,or updaing data and configuration with setOption.
* attr -> list  
    name of attribute
* value -> list  
    value of attribute
* is_roam -> bool/str  
    default -> True  
    Whether to enable mouse zooming and translating.If either zooming or translating is wanted,it can be set to 'scale' or 'move'. Otherwise, set it to be true to enable both.
* maptype -> str  
   type of map, it supports chinese geographical names, such as "安徽, 澳门, 北京, 重庆, 福建, 福建, 甘肃, 广东，广西, 广州, 海南, 河北, 黑龙江, 河南, 湖北, 湖南, 江苏, 江西, 吉林, 辽宁, 内蒙古, 宁夏, 青海, 山东, 上海, 陕西, 四川, 台湾, 天津, 香港, 新疆, 西藏, 云南, 浙江".

```python
from pyecharts import Map

value = [155, 10, 66, 78]
attr = ["福建", "山东", "北京", "上海"]
map = Map("全国地图示例", width=1200, height=600)
map.add("", attr, value, maptype='china')
map.show_config()
map.render()
```
![map-0](https://github.com/chenjiandongx/pyecharts/blob/master/images/map-0.gif)

```python
from pyecharts import Map

value = [155, 10, 66, 78, 33, 80, 190, 53, 49.6]
attr = ["福建", "山东", "北京", "上海", "甘肃", "新疆", "河南", "广西", "西藏"]
map = Map("Map 结合 VisualMap 示例", width=1200, height=600)
map.add("", attr, value, maptype='china', is_visualmap=True, visual_text_color='#000')
map.show_config()
map.render()
```
![map-1](https://github.com/chenjiandongx/pyecharts/blob/master/images/map-1.gif)

**Tip：** Settings can combine with visualMap component.

```python
from pyecharts import Map

value = [20, 190, 253, 77, 65]
attr = ['汕头市', '汕尾市', '揭阳市', '阳江市', '肇庆市']
map = Map("广东地图示例", width=1200, height=600)
map.add("", attr, value, maptype='广东', is_visualmap=True, visual_text_color='#000')
map.show_config()
map.render()
```
![map-2](https://github.com/chenjiandongx/pyecharts/blob/master/images/map-2.gif)

### About Customized Map
Because map contain large area,this program can't cover all the map,but don't worry about it.Echarts officially provide your own custom map [echart-map](http://echarts.baidu.com/download-map.html),this function allow you make map that you need,just download in JS file form.

open file pyecharts/temple.py under the installation directory,add the same line under the corresponding of  _temple variable.
 ```<script type="text/javascript " src="http://echarts.baidu.com/gallery/vendors/echarts/map/js/china.js"></script>```
correspond under Jupyter Notebook add the same lineunder _mapindex variable.
```"北京": "beijing: '//oog4yfyu0.bkt.clouddn.com/beijing'"```
Then use customized map in the program!The way import Js decide by yourself，only if it can be found by the program!


## Parallel
> Parallel Coordinates is a common way of visualizing high-dimensional geometry and analyzing multivariate data.

Parallel.add() signatures
```python
add(name, data, **kwargs)
```
* name -> str  
    Series name used for displaying in tooltip and filtering with legend,or updaing data and configuration with setOption.
* data -> [[],[]]  
    data array of series, it is represented by a two-dimension array.

Parallel.config() signatures
```python
config(schema=None, c_schema=None)
```
* schema  
    Dimension index of coordinate axis.  
    a axis name list, like ['apple', 'orange', 'watermelon']
* c_schema  
    User customize coordinate axis for parallel coordinate.
    * dim -> int  
        Dimension index of coordinate axis.
    * name > str  
        Name of axis.
    * type -> str  
        Type of axis  
        value：Numerical axis, suitable for continuous data.  
        category：Category axis, suitable for discrete category data.Data should only be set via data for this type.
    * min -> int  
        The minimun value of axis.
    * max -> int  
        The maximum value of axis.
    * inverse - bool  
        default -> False  
        Whether axis is inversed.
    * nameLocation -> str  
        Location of axis name. it can be 'start', 'middle', 'end'.

```python
from pyecharts import Parallel

schema = ["data", "AQI", "PM2.5", "PM10", "CO", "NO2"]
data = [
        [1, 91, 45, 125, 0.82, 34],
        [2, 65, 27, 78, 0.86, 45,],
        [3, 83, 60, 84, 1.09, 73],
        [4, 109, 81, 121, 1.28, 68],
        [5, 106, 77, 114, 1.07, 55],
        [6, 109, 81, 121, 1.28, 68],
        [7, 106, 77, 114, 1.07, 55],
        [8, 89, 65, 78, 0.86, 51, 26],
        [9, 53, 33, 47, 0.64, 50, 17],
        [10, 80, 55, 80, 1.01, 75, 24],
        [11, 117, 81, 124, 1.03, 45]
]
parallel = Parallel("平行坐标系-默认指示器")
parallel.config(schema)
parallel.add("parallel", data, is_random=True)
parallel.show_config()
parallel.render()
```
![parallel-0](https://github.com/chenjiandongx/pyecharts/blob/master/images/parallel-0.png)

```python
from pyecharts import Parallel

c_schema = [
    {"dim": 0, "name": "data"},
    {"dim": 1, "name": "AQI"},
    {"dim": 2, "name": "PM2.5"},
    {"dim": 3, "name": "PM10"},
    {"dim": 4, "name": "CO"},
    {"dim": 5, "name": "NO2"},
    {"dim": 6, "name": "CO2"},
    {"dim": 7, "name": "等级",
    "type": "category", "data": ['优', '良', '轻度污染', '中度污染', '重度污染', '严重污染']}
]
data = [
    [1, 91, 45, 125, 0.82, 34, 23, "良"],
    [2, 65, 27, 78, 0.86, 45, 29, "良"],
    [3, 83, 60, 84, 1.09, 73, 27, "良"],
    [4, 109, 81, 121, 1.28, 68, 51, "轻度污染"],
    [5, 106, 77, 114, 1.07, 55, 51, "轻度污染"],
    [6, 109, 81, 121, 1.28, 68, 51, "轻度污染"],
    [7, 106, 77, 114, 1.07, 55, 51, "轻度污染"],
    [8, 89, 65, 78, 0.86, 51, 26, "良"],
    [9, 53, 33, 47, 0.64, 50, 17, "良"],
    [10, 80, 55, 80, 1.01, 75, 24, "良"],
    [11, 117, 81, 124, 1.03, 45, 24, "轻度污染"],
    [12, 99, 71, 142, 1.1, 62, 42, "良"],
    [13, 95, 69, 130, 1.28, 74, 50, "良"],
    [14, 116, 87, 131, 1.47, 84, 40, "轻度污染"]
]
parallel = Parallel("平行坐标系-用户自定义指示器")
parallel.config(c_schema=c_schema)
parallel.add("parallel", data)
parallel.show_config()
parallel.render()
```
![parallel-1](https://github.com/chenjiandongx/pyecharts/blob/master/images/parallel-1.png)

**Tip：** **lineStyle** Parameter is Configurable


## Pie
> The pie chart is mainly used for showing proportion of different categories.Each arc length represents the proportion of data quantity.

Pie.add() signatures
```python
add(name, attr, value, radius=None, center=None, rosetype=None, **kwargs)
```
* name -> str  
    Series name used for displaying in tooltip and filtering with legend,or updaing data and configuration with setOption.
* attr -> list  
    name of attribute
* value -> list  
    value of attribute
* radius -> list  
    default -> [0, 75]  
    Radius of Pie chart, the first of which is inner radius, and the second is outer radius.  
    Percentage is supported. When set in percentage,it's relative to the smaller size between height and width of the container.
* center -> list
    default -> [50, 50]  
    Center position of Pie chart, the first of which is the horizontal position,and the second is the vertical position.  
    Percentage is supported. When set in percentage, the item is relative to the container width,and the second item to the height.
* rosetype -> str  
    default -> 'radius'  
    Whether to show as Nightingale chart, which distinguishs data through radius. There are 2 optional modes:
    * radius：Use central angle to show the percentage of data, radius to show data size.
    * area：All the sectors will share the same central angle, the data size is shown only through radiuses.

```python
from pyecharts import Pie

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [11, 12, 13, 10, 10, 10]
pie = Pie("饼图示例")
pie.add("", attr, v1, is_label_show=True)
pie.show_config()
pie.render()
```
![pie-0](https://github.com/chenjiandongx/pyecharts/blob/master/images/pie-0.gif)

```python
from pyecharts import Pie

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [11, 12, 13, 10, 10, 10]
pie = Pie("饼图-圆环图示例", title_pos='center')
pie.add("", attr, v1, radius=[40, 75], label_text_color=None, is_label_show=True,
        legend_orient='vertical', legend_pos='left')
pie.show_config()
pie.render()
```
![pie-1](https://github.com/chenjiandongx/pyecharts/blob/master/images/pie-1.png)

```python
from pyecharts import Pie

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [11, 12, 13, 10, 10, 10]
v2 = [19, 21, 32, 20, 20, 33]
pie = Pie("饼图-玫瑰图示例", title_pos='center', width=900)
pie.add("商品A", attr, v1, center=[25, 50], is_random=True, radius=[30, 75], rosetype='radius')
pie.add("商品B", attr, v2, center=[75, 50], is_random=True, radius=[30, 75], rosetype='area',
        is_legend_show=False, is_label_show=True)
pie.show_config()
pie.render()
```
![pie-2](https://github.com/chenjiandongx/pyecharts/blob/master/images/pie-2.png)


## Polar
> Polar coordinate can be used in scatter and line chart. Every polar coordinate has an angleAxis and a radiusAxis.

Polar.add() signatures
```python
add(name, data, angle_data=None, radius_data=None, type='line', symbol_size=4, start_angle=90,
    rotate_step=0, boundary_gap=True, clockwise=True, **kwargs)
```
* name -> str  
    Series name used for displaying in tooltip and filtering with legend,or updaing data and configuration with setOption.
* data -> [[],[]]  
    data of polar, [Polar radius, Polar angle,it is represented by a two-dimension array.
* angle_data -> list  
    Category data for angle, available in type: 'category' axis.
* radius_data -> list  
    Category data for radius, available in type: 'category' axis.
* type -> str  
    default -> 'line'  
    chart type，it can be 'scatter', 'effectScatter', 'barAngle', 'barRadius'
* symbol_size -> int  
    default -> 4  
    symbol size
* start_angle -> int  
    default -> 90  
    Starting angle of axis.standing for top position of center.0 degree stands for right position of center.
* rotate_step -> int  
    default -> 0  
    Rotation degree of axis label, which is especially useful when there is no enough space for category axis.
    Rotation degree is from -90 to 90.
* boundary_gap -> bool  
    default -> True  
    The boundary gap on both sides of a coordinate axis.  
    The setting and behavior of category axes and non-category axes are different.  
    The boundaryGap of category axis can be set to either true or false.  
    Default value is set to be true, in which case axisTick is served only as a separation line,and labels and data appear only in the center part of two axis ticks, which is called band.
* clockwise -> bool  
    default -> True  
    Whether the positive position of axis is in clockwise. True for clockwise by default.
* is_stack -> bool  
    It specifies whether to stack category axis.
* axis_range -> list  
    default -> [None, None]  
    axis scale range
* is_angleaxis_show -> bool  
    default -> True  
    whether show angle axis.
* is_radiusaxis_show -> bool  
    default -> True  
    whether show radius axis.

```python
from pyecharts import Polar

import random
data = [(i, random.randint(1, 100)) for i in range(101)]
polar = Polar("极坐标系-散点图示例")
polar.add("", data, boundary_gap=False, type='scatter', is_splitline_show=False,
          area_color=None, is_axisline_show=True)
polar.show_config()
polar.render()
```
![polar-0](https://github.com/chenjiandongx/pyecharts/blob/master/images/polar-0.png)

* is_splitline_show -> bool  
    default -> True  
    It specifies whether to show split line.
* is_axisline_show -> bool  
    default -> True  
    It specifies whether to show axis line.
* area_opacity -> float  
    Opacity of the component. Supports value from 0 to 1, and the component will not be drawn when set to 0.
* area_color -> str  
    Fill color.

**Tip：** **lineStyle** Parameter is Configurable

```python
from pyecharts import Polar

import random
data_1 = [(10, random.randint(1, 100)) for i in range(300)]
data_2 = [(11, random.randint(1, 100)) for i in range(300)]
polar = Polar("极坐标系-散点图示例", width=1200, height=600)
polar.add("", data_1, type='scatter')
polar.add("", data_2, type='scatter')
polar.show_config()
polar.render()
```
![polar-1](https://github.com/chenjiandongx/pyecharts/blob/master/images/polar-1.png)

```python
from pyecharts import Polar

import random
data = [(i, random.randint(1, 100)) for i in range(10)]
polar = Polar("极坐标系-动态散点图示例", width=1200, height=600)
polar.add("", data, type='effectScatter', effect_scale=10, effect_period=5)
polar.show_config()
polar.render()
```
![polar-2](https://github.com/chenjiandongx/pyecharts/blob/master/images/polar-2.gif)

```python
from pyecharts import Polar

radius = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
polar = Polar("极坐标系-堆叠柱状图示例", width=1200, height=600)
polar.add("A", [1, 2, 3, 4, 3, 5, 1], radius_data=radius, type='barRadius', is_stack=True)
polar.add("B", [2, 4, 6, 1, 2, 3, 1], radius_data=radius, type='barRadius', is_stack=True)
polar.add("C", [1, 2, 3, 4, 1, 2, 5], radius_data=radius, type='barRadius', is_stack=True)
polar.show_config()
polar.render()
```
![polar-3](https://github.com/chenjiandongx/pyecharts/blob/master/images/polar-3.gif)

```python
from pyecharts import Polar

radius = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
polar = Polar("极坐标系-堆叠柱状图示例", width=1200, height=600)
polar.add("", [1, 2, 3, 4, 3, 5, 1], radius_data=radius, type='barAngle', is_stack=True)
polar.add("", [2, 4, 6, 1, 2, 3, 1], radius_data=radius, type='barAngle', is_stack=True)
polar.add("", [1, 2, 3, 4, 1, 2, 5], radius_data=radius, type='barAngle', is_stack=True)
polar.show_config()
polar.render()
```
![polar-4](https://github.com/chenjiandongx/pyecharts/blob/master/images/polar-4.png)


## Radar
> Radar chart is mainly used to show multi-variable data,such as the analysis of a football player's varied attributes. It relies radar component.

Radar.add() signatures
```python
add(name, value, item_color=None, **kwargs)
```
* name -> list  
    Series name used for displaying in tooltip and filtering with legend,or updaing data and configuration with setOption.
* value -> [[],[]]  
    data array of series, it is represented by a two-dimension array.
* item_color -> str  
    Specify a single legend color

Radar.config() signatures
```python
config(schema=None, c_schema=None, shape="", rader_text_color="#000", **kwargs):
```
* schema -> list
    The default radar map indicator, used to specify multiple dimensions in the radar map,will process the data into a dictionary of {name: xx, value: xx}
* c_schema -> dict  
    Indicator of radar chart, which is used to assign multiple variables(dimensions) in radar chart.
    * name: Indicator's name.
    * min: The maximum value of indicator. It is an optional configuration, but we recommend to set it manually.
    * max: The maximum value of indicator. It is an optional configuration, but we recommend to set it manually.
* shape -> str  
    Radar render type, in which 'polygon' and 'circle' are supported.
* rader_text_color -> str  
    default -> '#000'  
    Radar chart data item font color

```python
from pyecharts import Radar

schema = [
    ("销售", 6500), ("管理", 16000), ("信息技术", 30000), ("客服", 38000), ("研发", 52000), ("市场", 25000)]
v1 = [[4300, 10000, 28000, 35000, 50000, 19000]]
v2 = [[5000, 14000, 28000, 31000, 42000, 21000]]
radar = Radar()
radar.config(schema)
radar.add("预算分配", v1, is_splitline=True, is_axisline_show=True)
radar.add("实际开销", v2, label_color=["#4e79a7"], is_area_show=False)
radar.show_config()
radar.render()
```
![radar-0](https://github.com/chenjiandongx/pyecharts/blob/master/images/radar-0.gif)

* is_area_show -> bool  
    It specifies whether to show split area.
* area_opacity -> float  
    Opacity of the component. Supports value from 0 to 1, and the component will not be drawn when set to 0.
* area_color -> str  
    Fill color.
* is_splitline_show  -> bool  
    default -> True
    It specifies whether to show split line.
* is_axisline_show -> bool  
    default -> True  
    It specifies whether to show axis line.

**Tip：** **lineStyle** Parameter is Configurable

```python
value_bj = [
    [55, 9, 56, 0.46, 18, 6, 1], [25, 11, 21, 0.65, 34, 9, 2],
    [56, 7, 63, 0.3, 14, 5, 3], [33, 7, 29, 0.33, 16, 6, 4],
    [42, 24, 44, 0.76, 40, 16, 5], [82, 58, 90, 1.77, 68, 33, 6],
    [74, 49, 77, 1.46, 48, 27, 7], [78, 55, 80, 1.29, 59, 29, 8],
    [267, 216, 280, 4.8, 108, 64, 9], [185, 127, 216, 2.52, 61, 27, 10],
    [39, 19, 38, 0.57, 31, 15, 11], [41, 11, 40, 0.43, 21, 7, 12],
    [64, 38, 74, 1.04, 46, 22, 13], [108, 79, 120, 1.7, 75, 41, 14],
    [108, 63, 116, 1.48, 44, 26, 15], [33, 6, 29, 0.34, 13, 5, 16],
    [94, 66, 110, 1.54, 62, 31, 17], [186, 142, 192, 3.88, 93, 79, 18],
    [57, 31, 54, 0.96, 32, 14, 19], [22, 8, 17, 0.48, 23, 10, 20],
    [39, 15, 36, 0.61, 29, 13, 21], [94, 69, 114, 2.08, 73, 39, 22],
    [99, 73, 110, 2.43, 76, 48, 23], [31, 12, 30, 0.5, 32, 16, 24],
    [42, 27, 43, 1, 53, 22, 25], [154, 117, 157, 3.05, 92, 58, 26],
    [234, 185, 230, 4.09, 123, 69, 27],[160, 120, 186, 2.77, 91, 50, 28],
    [134, 96, 165, 2.76, 83, 41, 29], [52, 24, 60, 1.03, 50, 21, 30],
]
value_sh = [
    [91, 45, 125, 0.82, 34, 23, 1], [65, 27, 78, 0.86, 45, 29, 2],
    [83, 60, 84, 1.09, 73, 27, 3], [109, 81, 121, 1.28, 68, 51, 4],
    [106, 77, 114, 1.07, 55, 51, 5], [109, 81, 121, 1.28, 68, 51, 6],
    [106, 77, 114, 1.07, 55, 51, 7], [89, 65, 78, 0.86, 51, 26, 8],
    [53, 33, 47, 0.64, 50, 17, 9], [80, 55, 80, 1.01, 75, 24, 10],
    [117, 81, 124, 1.03, 45, 24, 11], [99, 71, 142, 1.1, 62, 42, 12],
    [95, 69, 130, 1.28, 74, 50, 13], [116, 87, 131, 1.47, 84, 40, 14],
    [108, 80, 121, 1.3, 85, 37, 15], [134, 83, 167, 1.16, 57, 43, 16],
    [79, 43, 107, 1.05, 59, 37, 17], [71, 46, 89, 0.86, 64, 25, 18],
    [97, 71, 113, 1.17, 88, 31, 19], [84, 57, 91, 0.85, 55, 31, 20],
    [87, 63, 101, 0.9, 56, 41, 21], [104, 77, 119, 1.09, 73, 48, 22],
    [87, 62, 100, 1, 72, 28, 23], [168, 128, 172, 1.49, 97, 56, 24],
    [65, 45, 51, 0.74, 39, 17, 25], [39, 24, 38, 0.61, 47, 17, 26],
    [39, 24, 39, 0.59, 50, 19, 27], [93, 68, 96, 1.05, 79, 29, 28],
    [188, 143, 197, 1.66, 99, 51, 29], [174, 131, 174, 1.55, 108, 50, 30],
]
c_schema= [{"name": "AQI", "max": 300, "min": 5},
           {"name": "PM2.5", "max": 250, "min": 20},
           {"name": "PM10", "max": 300, "min": 5},
           {"name": "CO", "max": 5},
           {"name": "NO2", "max": 200},
           {"name": "SO2", "max": 100}]
radar = Radar()
radar.config(c_schema=c_schema, shape='circle')
radar.add("北京", value_bj, item_color="#f9713c", symbol=None)
radar.add("上海", value_sh, item_color="#b3e4a1", symbol=None)
radar.show_config()
radar.render()
```
![radar-1](https://github.com/chenjiandongx/pyecharts/blob/master/images/radar-1.gif)

**Tip：** symblo=None make marked graphic hiden(small circle)


## Scatter
> The scatter chart in rectangular coordinate could be used to present the relation between x and y.
> If data have multiple dimensions, the values of the other dimensions can be visualized through symbol with various sizes and colors, which becomes a bubble chart. These can be done by using with visualMap component.

Scatter.add() signatures
```python
add(name, x_axis, y_axis, symbol_size=10, **kwargs)
```
* name -> str  
    Series name used for displaying in tooltip and filtering with legend,or updaing data and configuration with setOption.
* x_axis -> list  
    data of xAxis
* y_axis -> list  
    data of yAxis
* symbol_size -> int  
    default -> 10  
    symbol size

```python
from pyecharts import Scatter

v1 = [10, 20, 30, 40, 50, 60]
v2 = [10, 20, 30, 40, 50, 60]
scatter = Scatter("散点图示例")
scatter.add("A", v1, v2)
scatter.add("B", v1[::-1], v2)
scatter.show_config()
scatter.render()
```
![scatter-0](https://github.com/chenjiandongx/pyecharts/blob/master/images/scatter-0.png)

Scatter also built-in draw method.
```python
draw(path, color=None)
```
convert pixels on the image into array ,when colour is （255,255,255）only retain non white pixels' coordinate information. output two k_lst, v_lst list can just as the data item of scatter plot.

```
* path -> str  
    path of Image that want to draw
* color -> str  
    select a color to exclude, (225, 225, 225) means Keep only white pixel information.

First of all ,you need to prepare a picture,like

![pyecharts-0](https://github.com/chenjiandongx/pyecharts/blob/master/images/pyecharts-0.png)

```python
from pyecharts import Scatter

scatter = Scatter("散点图示例")
v1, v2 = scatter.draw("../images/pyecharts-0.png")
scatter.add("pyecharts", v1, v2, is_random=True)
scatter.show_config()
scatter.render()
```
![pyecharts-1](https://github.com/chenjiandongx/pyecharts/blob/master/images/pyecharts-1.png)


# Scatter3D
Scatter3D.add() signatures
```python
add(name, data, grid3D_opacity=1, **kwargs)
```
* name -> str
    Series name used for displaying in tooltip and filtering with legend,or updaing data and configuration with setOption.
* data -> [[], []]  
    data of line3D
* grid3D_opacity -> float  
    default -> 1  
    opacity of gird3D item

```python
from pyecharts import Scatter3D

import random
data = [[random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)] for _ in range(80)]
range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
               '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
scatter3D = Scatter3D("3D 散点图示例", width=1200, height=600)
scatter3D.add("", data, is_visualmap=True, visual_range_color=range_color)
scatter3D.render()
```
![scatter3D-0](https://github.com/chenjiandongx/pyecharts/blob/master/images/scatter3D-0.gif)

**Tip：** more details aboutt gird3D，please refer to [Global-options](https://github.com/chenjiandongx/pyecharts/blob/master/document/en-us/documentation.md#Global-options)

## WordCloud
WordCloud.add() signatures
```python
add(name, attr, value, shape="circle", word_gap=20, word_size_range=None, rotate_step=45)
```
* name -> str  
    Series name used for displaying in tooltip and filtering with legend,or updaing data and configuration with setOption.
* attr -> list  
    name of attribute
* value -> list  
    value of attribute
* shape -> list  
    shape of wordcloud.It can be 'circle', 'cardioid', 'diamond', 'triangle-forward', 'triangle', 'pentagon', 'star'
* word_gap -> int  
    default -> 20  
    Gap of word.size of the grid in pixels for marking the availability of the canvas,the larger the grid size, the bigger the gap between words.
* word_size_range -> list  
    default -> [12, 60]  
    Text size range which the value in data will be mapped to.
* rotate_step -> int  
    default -> 45  
    Text rotation range and step in degree. Text will be rotated randomly in range [-90, 90].

```python
from pyecharts import WordCloud

name = ['Sam S Club', 'Macys', 'Amy Schumer', 'Jurassic World', 'Charter Communications',
        'Chick Fil A', 'Planet Fitness', 'Pitch Perfect', 'Express', 'Home', 'Johnny Depp',
        'Lena Dunham', 'Lewis Hamilton', 'KXAN', 'Mary Ellen Mark', 'Farrah Abraham',
        'Rita Ora', 'Serena Williams', 'NCAA baseball tournament', 'Point Break']
value = [10000, 6181, 4386, 4055, 2467, 2244, 1898, 1484, 1112, 965, 847, 582, 555,
         550, 462, 366, 360, 282, 273, 265]
wordcloud = WordCloud(width=1300, height=620)
wordcloud.add("", name, value, word_size_range=[20, 100])
wordcloud.show_config()
wordcloud.render()
```
![wordcloud-0](https://github.com/chenjiandongx/pyecharts/blob/master/images/wordcloud-0.png)

```python
wordcloud = WordCloud(width=1300, height=620)
wordcloud.add("", name, value, word_size_range=[30, 100], shape='diamond')
wordcloud.show_config()
wordcloud.render()
```
![wordcloud-1](https://github.com/chenjiandongx/pyecharts/blob/master/images/wordcloud-1.png)

**Tip：** if and only if shape is default'circle' the rotate_step parameter will take effect.


# User Custom

## Combination different types of chart and draw they on same picture.
User Can Combination Custom Line/Bar/Kline, Scatter/EffectScatter chart,draw different types of chart on one image.Using the first chart as basement,data after that will draw on the first chart.
Need use the method ```get_series()``` and ```custom()```.

```python
get_series()
""" Get chart's series data """
```
```python
custom(series)
''' Add to custom chart type '''
```
* series -> dict
    add to chart type series data

irst use ```get_series()``` to get the data,then use ```custom()``` combine the charts together

Line + Bar
```python
from pyecharts import Bar, Line

attr = ['A', 'B', 'C', 'D', 'E', 'F']
v1 = [10, 20, 30, 40, 50, 60]
v2 = [15, 25, 35, 45, 55, 65]
v3 = [38, 28, 58, 48, 78, 68]
bar = Bar("Line - Bar 示例")
bar.add("bar", attr, v1)
line = Line()
line.add("line", v2, v3)
bar.custom(line.get_series())
bar.show_config()
bar.render()
```
![custom-0](https://github.com/chenjiandongx/pyecharts/blob/master/images/custom-0.gif)

Specific procedure are as follows:
1. initialize the chart,add normal configuration item.
2. call the first chart's custom(type.get_series()) method and one by one.
3. call the first chart's render() method.

**Tip：** ```bar.custom(line.get_series())``` this one have to be careful,use the first one chart as basement.remember do not write ```bar.custom(bar.get_series())``` or the program will get into endless self call state,infinite recursion,finally may cause your computer to crash.

Scatter + EffectScatter
```python
from pyecharts import Scatter, EffectScatter

v1 = [10, 20, 30, 40, 50, 60]
v2 = [30, 30, 30, 30, 30, 30]
v3 = [50, 50, 50, 50, 50, 50]
v4 = [10, 10, 10, 10, 10, 10]
es = EffectScatter("Scatter - EffectScatter 示例")
es.add("es", v1, v2)
scatter = Scatter()
scatter.add("scatter", v1, v3)
es.custom(scatter.get_series())
es_1 = EffectScatter()
es_1.add("es_1", v1, v4, symbol='pin', effect_scale=5)
es.custom(es_1.get_series())
es.show_config()
es.render()
```
![custom-1](https://github.com/chenjiandongx/pyecharts/blob/master/images/custom-1.gif)

Kline + Line
```python
import random
from pyecharts import Line, Kline

v1 = [[2320.26, 2320.26, 2287.3, 2362.94], [2300, 2291.3, 2288.26, 2308.38],
      [2295.35, 2346.5, 2295.35, 2345.92], [2347.22, 2358.98, 2337.35, 2363.8],
      [2360.75, 2382.48, 2347.89, 2383.76], [2383.43, 2385.42, 2371.23, 2391.82],
      [2377.41, 2419.02, 2369.57, 2421.15], [2425.92, 2428.15, 2417.58, 2440.38],
      [2411, 2433.13, 2403.3, 2437.42], [2432.68, 2334.48, 2427.7, 2441.73],
      [2430.69, 2418.53, 2394.22, 2433.89], [2416.62, 2432.4, 2414.4, 2443.03],
      [2441.91, 2421.56, 2418.43, 2444.8], [2420.26, 2382.91, 2373.53, 2427.07],
      [2383.49, 2397.18, 2370.61, 2397.94], [2378.82, 2325.95, 2309.17, 2378.82],
      [2322.94, 2314.16, 2308.76, 2330.88], [2320.62, 2325.82, 2315.01, 2338.78],
      [2313.74, 2293.34, 2289.89, 2340.71], [2297.77, 2313.22, 2292.03, 2324.63],
      [2322.32, 2365.59, 2308.92, 2366.16], [2364.54, 2359.51, 2330.86, 2369.65],
      [2332.08, 2273.4, 2259.25, 2333.54], [2274.81, 2326.31, 2270.1, 2328.14],
      [2333.61, 2347.18, 2321.6, 2351.44], [2340.44, 2324.29, 2304.27, 2352.02],
      [2326.42, 2318.61, 2314.59, 2333.67], [2314.68, 2310.59, 2296.58, 2320.96],
      [2309.16, 2286.6, 2264.83, 2333.29], [2282.17, 2263.97, 2253.25, 2286.33],
      [2255.77, 2270.28, 2253.31, 2276.22]]
attr = ["2017/7/{}".format(i + 1) for i in range(31)]
kline = Kline("Kline - Line 示例")
kline.add("日K", attr, v1)
line_1 = Line()
line_1.add("line-1", attr, [random.randint(2400, 2500) for _ in range(31)])
line_2 = Line()
line_2.add("line-2", attr, [random.randint(2400, 2500) for _ in range(31)])
kline.custom(line_1.get_series())
kline.custom(line_2.get_series())
kline.show_config()
kline.render()
```
![custom-2](https://github.com/chenjiandongx/pyecharts/blob/master/images/custom-2.png)

## Combination different types of chart and draw on multiple picture,the chart parallel disply.
User Can Combination Custom  Line/Bar/Kline/Scatter/EffectScatter/Pie/HeatMap chart,draw different types of chart on multiple image.Using the first chart as basement
Need use the method ```get_series()``` and ```grid()```.

```python
get_series()
""" get chart's series data """
```
```python
grid(series，grid_width, grid_height, grid_top, grid_bottom, grid_left, grid_right)
''' Concurrently show charts '''
```
* series -> dict  
    other chart series data
* grid_width -> str/int  
    Width of grid component. Adaptive by default.
* grid_height -> str/int  
    Height of grid component. Adaptive by default.
* grid_top -> str/int  
    Distance between grid component and the top side of the container.  
    grid_top value can be instant pixel value like 20;it can also be percentage value relative to container width like '20%';and it can also be 'top', 'middle', or 'bottom'.  
    If the grid_top value is set to be 'top', 'middle', or 'bottom',then the component will be aligned automatically based on position.
* grid_bottom -> str/int  
    Distance between grid component and the bottom side of the container.  
    grid_bottom value can be instant pixel value like 20;it can also be percentage value relative to container width like '20%'.
* grid_left -> str/int  
    Distance between grid component and the left side of the container.  
    grid_left value can be instant pixel value like 20;it can also be percentage value relative to container width like '20%';and it can also be 'left', 'center', or 'right'.  
    If the grid_left value is set to be 'left', 'center', or 'right',then the component will be aligned automatically based on position.
* grid_right -> str/int  
    Distance between grid component and the right side of the container.  
    grid_right value can be instant pixel value like 20;it can also be percentage value relative to container width like '20%'.

irst use ```get_series()``` get data，then use ```grid()``` combine the charts

up and down type,Bar + Line
```python
from pyecharts import Bar, Line

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 75, 90]
v2 = [10, 25, 8, 60, 20, 80]
bar = Bar("柱状图示例", height=720, is_grid=True)
bar.add("商家A", attr, v1, is_stack=True, grid_bottom="60%")
bar.add("商家B", attr, v2, is_stack=True, grid_bottom="60%")
line = Line("折线图示例", title_top="50%")
attr = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
line.add("最高气温", attr, [11, 11, 15, 13, 12, 13, 10], mark_point=["max", "min"], mark_line=["average"])
line.add("最低气温", attr, [1, -2, 2, 5, 3, 2, 0], mark_point=["max", "min"],
         mark_line=["average"], legend_top="50%")
bar.grid(line.get_series(), grid_top="60%")
bar.show_config()
bar.render()
```
![grid-0](https://github.com/chenjiandongx/pyecharts/blob/master/images/grid-0.gif)

**once more Tip：** ```bar.grid(line.get_series(), grid_top="60%")``` do not write ```bar.grid(bar.get_series())``` or get into edless recursion

The specific process is as follows：
1. Make is_grid=True when the first chart initialize,declare using grid assembly.
2. The first form's add() method have to make grid_* parameter，it has to be done,because grid_* default value is None,and won't add to configuration item.Appoint one at least.
3. Initialize other type（so do the same type）,not need appoint grid_* parameter.
4. Call the first chart's grid() method and add one by one,and set grid_* parameter，it has to be done，at least one.
5. Call the first chart's render() method.

left and right type，Scatter + EffectScatter
```python
from pyecharts import Scatter, EffectScatter

v1 = [5, 20, 36, 10, 75, 90]
v2 = [10, 25, 8, 60, 20, 80]
scatter = Scatter(width=1200, is_grid=True)
scatter.add("散点图示例", v1, v2, grid_left="60%", legend_pos="70%")
es = EffectScatter()
es.add("动态散点图示例", [11, 11, 15, 13, 12, 13, 10], [1, -2, 2, 5, 3, 2, 0],
       effect_scale=6, legend_pos="20%")
scatter.grid(es.get_series(), grid_right="60%")
scatter.show_config()
scatter.render()
```
![grid-1](https://github.com/chenjiandongx/pyecharts/blob/master/images/grid-1.gif)

up,down,left and right type,Bar + Line + Scatter + EffectScatter
```python
from pyecharts import Bar, Line, Scatter, EffectScatter

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 75, 90]
v2 = [10, 25, 8, 60, 20, 80]
bar = Bar("柱状图示例", height=720, width=1200, title_pos="65%", is_grid=True)
bar.add("商家A", attr, v1, is_stack=True, grid_bottom="60%", grid_left="60%")
bar.add("商家B", attr, v2, is_stack=True, grid_bottom="60%", grid_left="60%", legend_pos="80%")
line = Line("折线图示例")
attr = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
line.add("最高气温", attr, [11, 11, 15, 13, 12, 13, 10], mark_point=["max", "min"], mark_line=["average"])
line.add("最低气温", attr, [1, -2, 2, 5, 3, 2, 0], mark_point=["max", "min"],
         mark_line=["average"], legend_pos="20%")
v1 = [5, 20, 36, 10, 75, 90]
v2 = [10, 25, 8, 60, 20, 80]
scatter = Scatter("散点图示例", title_top="50%", title_pos="65%")
scatter.add("scatter", v1, v2, legend_top="50%", legend_pos="80%")
es = EffectScatter("动态散点图示例", title_top="50%")
es.add("es", [11, 11, 15, 13, 12, 13, 10], [1, -2, 2, 5, 3, 2, 0], effect_scale=6,
       legend_top="50%", legend_pos="20%")
bar.grid(line.get_series(), grid_bottom="60%", grid_right="60%")
bar.grid(scatter.get_series(), grid_top="60%", grid_left="60%")
bar.grid(es.get_series(), grid_top="60%", grid_right="60%")
bar.show_config()
bar.render()
```
![grid-2](https://github.com/chenjiandongx/pyecharts/blob/master/images/grid-2.gif)

Line +  Pie
```python
from pyecharts import Line, Pie

line = Line("折线图示例", width=1200, is_grid=True)
attr = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
line.add("最高气温", attr, [11, 11, 15, 13, 12, 13, 10], mark_point=["max", "min"],
         mark_line=["average"], grid_right="65%")
line.add("最低气温", attr, [1, -2, 2, 5, 3, 2, 0], mark_point=["max", "min"],
         mark_line=["average"], legend_pos="20%")
attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [11, 12, 13, 10, 10, 10]
pie = Pie("饼图示例", title_pos="45%")
pie.add("", attr, v1, radius=[30, 55], legend_pos="65%", legend_orient='vertical')
line.grid(pie.get_series(), grid_left="60%")
line.show_config()
line.render()
```
![grid-3](https://github.com/chenjiandongx/pyecharts/blob/master/images/grid-3.png)

Line + Kline
```python
from pyecharts import Line, Kline

line = Line("折线图示例", width=1200, is_grid=True)
attr = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
line.add("最高气温", attr, [11, 11, 15, 13, 12, 13, 10], mark_point=["max", "min"],
         mark_line=["average"], grid_right="60%")
line.add("最低气温", attr, [1, -2, 2, 5, 3, 2, 0], mark_point=["max", "min"],
         mark_line=["average"], legend_pos="20%", grid_right="60%")
attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
value = [20, 40, 60, 80, 100, 120]
v1 = [[2320.26, 2320.26, 2287.3, 2362.94], [2300, 2291.3, 2288.26, 2308.38],
      [2295.35, 2346.5, 2295.35, 2345.92], [2347.22, 2358.98, 2337.35, 2363.8],
      [2360.75, 2382.48, 2347.89, 2383.76], [2383.43, 2385.42, 2371.23, 2391.82],
      [2377.41, 2419.02, 2369.57, 2421.15], [2425.92, 2428.15, 2417.58, 2440.38],
      [2411, 2433.13, 2403.3, 2437.42], [2432.68, 2334.48, 2427.7, 2441.73],
      [2430.69, 2418.53, 2394.22, 2433.89], [2416.62, 2432.4, 2414.4, 2443.03],
      [2441.91, 2421.56, 2418.43, 2444.8], [2420.26, 2382.91, 2373.53, 2427.07],
      [2383.49, 2397.18, 2370.61, 2397.94], [2378.82, 2325.95, 2309.17, 2378.82],
      [2322.94, 2314.16, 2308.76, 2330.88], [2320.62, 2325.82, 2315.01, 2338.78],
      [2313.74, 2293.34, 2289.89, 2340.71], [2297.77, 2313.22, 2292.03, 2324.63],
      [2322.32, 2365.59, 2308.92, 2366.16], [2364.54, 2359.51, 2330.86, 2369.65],
      [2332.08, 2273.4, 2259.25, 2333.54], [2274.81, 2326.31, 2270.1, 2328.14],
      [2333.61, 2347.18, 2321.6, 2351.44], [2340.44, 2324.29, 2304.27, 2352.02],
      [2326.42, 2318.61, 2314.59, 2333.67], [2314.68, 2310.59, 2296.58, 2320.96],
      [2309.16, 2286.6, 2264.83, 2333.29], [2282.17, 2263.97, 2253.25, 2286.33],
      [2255.77, 2270.28, 2253.31, 2276.22]]
kline = Kline("K 线图示例", title_pos="60%")
kline.add("日K", ["2017/7/{}".format(i + 1) for i in range(31)], v1, legend_pos="80%")
line.grid(kline.get_series(), grid_left="55%")
line.show_config()
line.render()
```
![grid-4](https://github.com/chenjiandongx/pyecharts/blob/master/images/grid-4.png)

HeatMap + Bar
```python
import random

from pyecharts import HeatMap, Bar

x_axis = ["12a", "1a", "2a", "3a", "4a", "5a", "6a", "7a", "8a", "9a", "10a", "11a",
          "12p", "1p", "2p", "3p", "4p", "5p", "6p", "7p", "8p", "9p", "10p", "11p"]
y_aixs = ["Saturday", "Friday", "Thursday", "Wednesday", "Tuesday", "Monday", "Sunday"]
data = [[i, j, random.randint(0, 50)] for i in range(24) for j in range(7)]
heatmap = HeatMap("热力图示例", height=700, is_grid=True)
heatmap.add("热力图直角坐标系", x_axis, y_aixs, data, is_visualmap=True, visual_top="45%",
            visual_text_color="#000", visual_orient='horizontal', grid_bottom="60%")
attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 75, 90]
v2 = [10, 25, 8, 60, 20, 80]
bar = Bar("柱状图示例", title_top="52%")
bar.add("商家A", attr, v1, is_stack=True)
bar.add("商家B", attr, v2, is_stack=True, legend_top="50%")
heatmap.grid(bar.get_series(), grid_top="60%")
heatmap.show_config()
heatmap.render()
```
![grid-5](https://github.com/chenjiandongx/pyecharts/blob/master/images/grid-5.gif)
Bar will influenced by HeatMap,it's funy.

# Multiple charts in one html page

You will need use `Page` class and its api is simple, call `add()` charts to and then call `render()` in
the end. However, wordcloud and liquid charts cannot be mixed in.


Here is an example code::

```python
#coding=utf-8
from __future__ import unicode_literals

from pyecharts import Bar, Scatter3D
from pyecharts import Page


page = Page()  # step 1

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 75, 90]
v2 = [10, 25, 8, 60, 20, 80]
bar = Bar("柱状图数据堆叠示例")
bar.add("商家A", attr, v1, is_stack=True)
bar.add("商家B", attr, v2, is_stack=True)
page.add(bar)   # step 2

# scatter3D_0
import random
data = [[random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)] for _ in range(80)]
range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
               '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
scatter3D = Scatter3D("3D 散点图示例", width=1200, height=600)
scatter3D.add("", data, is_visualmap=True, visual_range_color=range_color)
page.add(scatter3D)  # step 2

page.render()  # step 3
```

After executing above code, you will find two charts in render.html:

![multiple-charts-0](https://github.com/chenjiandongx/pyecharts/blob/master/images/multiple-charts-0.gif)

# Flask and Django Integration Documentation

* [pyecharts + Flask](https://github.com/chenjiandongx/pyecharts/blob/master/document/en-us/doc_flask.md)
* [pyecharts + Django](https://github.com/chenjiandongx/pyecharts/blob/master/document/en-us/doc_django.md)


# More Examples

* More examples refer to [example.md](https://github.com/chenjiandongx/pyecharts/blob/master/example.md)
* Welcome to provide more examples.

# About The Project

* Enjoy pyecharts!
* If you have any question or want to improve this repository, welcome to create an issue or pull requests .
* If you want to discuss with me alone, use the emali -> chenjiandongx@qq.com
* Show solicitude for [changelog.md](https://github.com/chenjiandongx/pyecharts/blob/master/changelog.md)
