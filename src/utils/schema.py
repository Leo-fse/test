from bokeh.plotting import figure
from pydantic import BaseModel, Field


class Graph(BaseModel):
    title: str = Field(..., title="Title of the graph")
    x_axis_label: str = Field(..., title="Label of the x-axis")
    y_axis_label: str = Field(..., title="Label of the y-axis")
    x: list = Field(..., title="Values of the x-axis")
    y: list = Field(..., title="Values of the y-axis")

    def plot(self):
        p = figure(title=self.title, x_axis_label=self.x_axis_label, y_axis_label=self.y_axis_label)
        renderer = self.renderer(p, self.x, self.y)
        return p

    def renderer(self, p, x, y):
        renderer = p.line(x, y)
        return renderer


class Tab(BaseModel):
    title: str = Field(..., title="Title of the tab")
    graphs: list = Field(..., title="List of graphs")

    def plot(self):
        return [graph.plot() for graph in self.graphs]


g = Graph()
print(g)
