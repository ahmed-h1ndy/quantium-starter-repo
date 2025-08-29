import pytest
from visualization import app

def test_graph_exists(dash_duo):
    dash_duo.start_server(app)
    graph = dash_duo.find_element("#example-graph")
    assert graph is not None
    assert graph.is_displayed()