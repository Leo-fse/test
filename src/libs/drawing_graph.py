from bokeh.plotting import figure, show

from src.const import colors, markers
from src.utils import log_decorator, logger


class GraphSetting:
    def __init__(self, figure_setting, sources, renderer_settings):
        self.figure_setting = figure_setting
        self.sources = sources
        self.renderer_settings = renderer_settings


@log_decorator(logger)
def create_fig_and_renderers(figure_setting, sources, renderer_settings):
    fig = figure(**figure_setting)
    renderers = []
    for soruce_key, source in sources.items():
        for key, renderer_setting in renderer_settings[0].items():
            logger.debug(f"soruce_key: {soruce_key}, value: {source}")
            logger.debug(f"key: {key}, renderer_setting: {renderer_setting}")
            legend_label = f"{soruce_key}_{key}"
            logger.debug(f"legend_label: {legend_label}")
            renderer = fig.scatter(
                name=f"{soruce_key}<|>{key}",
                **renderer_setting,
                source=source["source"],
            )
            renderers.append(renderer)

    return fig, renderers


@log_decorator(logger)
def legend_label(renderers):
    """凡例の作成
    凡例の分け方：
    1. renderer, sourceそれぞれで分ける
    2. sourceで分ける
    3. rendererで分ける
    # rendererのnameからデータ名、パラメータ名を取得
    """
    # rendererのnameは<|>で区切られているので区切り文字の前後をそれぞれ取得
    for renderer in renderers:
        data_name = renderer.name.split("<|>")[0]
        param_name = renderer.name.split("<|>")[1]

        renderer.glyph.line_color = colors.pop(0)
        renderer.glyph.fill_color = colors.pop(0)
        renderer.glyph.marker = markers.pop(0)

        logger.debug(f"data_name: {data_name}, param_name: {param_name}")
        # renderer.legend_label = f"{data_name}_{param_name}"


@log_decorator(logger)
def main(setting_info):
    logger.info("グラフを描画開始！")

    figure_setting = setting_info["figure_setting"]
    sources = setting_info["sources"]
    renderer_settings = setting_info["renderer_settings"]

    fig, renderers = create_fig_and_renderers(figure_setting, sources, renderer_settings)
    legend_label(renderers)

    show(fig)

    logger.info("グラフの描画が完了しました！")
