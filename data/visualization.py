# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

df = pd.read_csv('daily_sales_data_full.csv')

app = Dash()

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

fig = px.line(df, x="date", y="sales")

app.layout = html.Div(children=[
    html.H1(children='Daily sales visualizer'),

    html.Div(children='''
        We can see an increase in sales starting from 14-01-2021
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])


if __name__ == "__main__":
    app.run(debug=True)
