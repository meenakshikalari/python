# dashboard
import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Create sample data
df = pd.DataFrame({
    "Fruits": ["Apples", "Bananas", "Cherries", "Dates"],
    "Quantity": [10, 15, 7, 5]
})

# Create a Plotly figure
fig = px.bar(df, x="Fruits", y="Quantity", title="Fruit Quantity")

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the dashboard
app.layout = html.Div([
    html.H1("Simple Dashboard"),
    dcc.Graph(figure=fig)
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
