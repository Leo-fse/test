from bokeh.models import ColumnDataSource

renderer_settings = {
    "graph1": {
        "y1": dict(x="x", y="y1", line_width=2, color="red"),
        "y2": dict(x="x", y="y2", line_width=2, color="green"),
        "y3": dict(x="x", y="y3", line_width=2, color="blue"),
    },
    "graph2": {
        "y4": dict(x="x", y="y5", line_width=2, color="red"),
        "y5": dict(x="x", y="y6", line_width=2, color="green"),
        "y6": dict(x="x", y="y7", line_width=2, color="blue"),
    },
}
figure_setting = {
    "figure1": dict(
        title="Example Bokeh plot figure1",
        x_axis_label="x",
        y_axis_label="y",
        x_axis_type="linear",
    ),
    "figure2": dict(
        title="Example Bokeh plot figure2",
        x_axis_label="x",
        y_axis_label="y",
        x_axis_type="linear",
    ),
}
sources = {
    "source1": {
        "source": ColumnDataSource(
            data=dict(
                x=[1, 2, 3, 4, 5],
                y=[5, 4, 3, 2, 1],
                y2=[10, 20, 30, 40, 50],
                y3=[-10, -20, -30, -40, -50],
            )
        )
    },
    "source2": {
        "source": ColumnDataSource(
            data=dict(
                x=[1, 2, 3, 4, 5],
                y=[1, 2, 3, 4, 5],
                y2=[50, 40, 30, 20, 10],
                y3=[-50, -40, -30, -20, -10],
            )
        )
    },
}
