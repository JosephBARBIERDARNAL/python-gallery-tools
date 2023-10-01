

def get_chart_types(family):
    chart_types_dict = {'distribution': ['violin', 'density', 'histogram', 'boxplot', 'ridgeline', 'beeswarm'],
                   'correlation': ['scatter', 'heatmap', 'correlogram', 'bubble', 'connectedScatter', 'density2d'],
                   'ranking': ['barplot', 'radar', 'wordcloud', 'parallel', 'lollipop', 'circularBarplot'],
                   'partOfAWhole': ['venn', 'treemap', 'donut', 'pie', 'dendogram', 'circularPacking', 'waffle'],
                   'evolution': ['line', 'area', 'stackedArea', 'stream', 'timeseries', 'candlestick'],
                   'map': ['map', 'hebin', 'cartogram', 'connection', 'bubbleMap'],
                   'flow': ['chordDiagram', 'network', 'sankey', 'arc', 'edgeBundling'],
                   'general': ['colors', 'plotly', 'animation', 'cheatSheets', 'caveats', '3d', 'statistics']
                   }
    return chart_types_dict[family]