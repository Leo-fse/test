from bokeh.models import ColumnDataSource

from src.utils import log_decorator, logger


@log_decorator(logger)
def main():
    logger.debug("設定ファイルを読み込みます！")
    figure_setting = dict(
        title="Example Bokeh plot",
        x_axis_label="x",
        y_axis_label="y",
    )

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

    renderer_settings = (
        {
            "y": dict(
                x="x",
                y="y",
                line_width=2,
            ),
            "y2": dict(
                x="x",
                y="y2",
                line_width=2,
            ),
            "y3": dict(
                x="x",
                y="y3",
                line_width=2,
            ),
        },
    )

    setting_info = dict(
        figure_setting=figure_setting, sources=sources, renderer_settings=renderer_settings
    )
    return setting_info


main()
