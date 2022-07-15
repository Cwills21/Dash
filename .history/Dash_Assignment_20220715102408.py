import os
from dash import Dash, html, dcc, callback, Input, Output,State
import plotly.express as px
import pandas as pd
import numpy as np
app = Dash(__name__)

path=os.path.join("NewSuperstores","NewSuperstores.csv")
myfile=pd.read_csv(path)
list=['best_selling_and_most_profitable_category','best_selling_and_most_profitable_sub_category','top-selling_sub_category','most_profitable_customer_segment','prefered_ship_mode','most_profitable_region','city_with_highiest_no_sales','try','try2']
app.layout = html.Div(children=[
    html.H1(children='DBC26.1 Python Assignment by Collins'),   
    # html.H3(style={"font-weight": "bold", "color":"blue"},children='''
    #     Best Selling and most profitable catgory = Technology   
    # '''),
    dcc.Dropdown(
        id='opt', 
        options=[{'label':i, 'value':i} for i in list],
        placeholder="Select a Option",       
    ),

    dcc.Graph(
         id='bar-graph',
        # figure=fig
    ),
   
])

@app.callback(
    Output('bar-graph', 'figure'),
    Input('opt','value'),    
)

def display_graph(opt):
    if opt == 'best_selling_and_most_profitable_category':        
        graphindex = "Category"        
        mydf=myfile.groupby(graphindex).Profit_Margin.sum()
        mydf = pd.DataFrame(mydf).sort_values(by='Profit_Margin',ascending=False) #total_profit/total_sales*100
        mydf.reset_index()
        fig = px.bar(mydf, x=mydf.index, y=mydf.Profit_Margin, color=mydf.index, barmode="group",title="Best Selling and most profitable catgory")
    elif opt=='best_selling_and_most_profitable_sub_category':        
        graphindex = "Sub_Category"
        mydf=myfile.groupby(graphindex).Profit_Margin.sum()
        mydf = pd.DataFrame(mydf).sort_values(by='Profit_Margin',ascending=False)
        mydf.reset_index()
        fig = px.bar(mydf, x=mydf.index, y=mydf.Profit_Margin, color=mydf.index, barmode="group",title="Best Selling and most profitable Sub catgory")
    elif opt=='top-selling_sub_category':
        title="Top Selling and most profitable catgory"
        graphindex = "Sub_Category"
        mydf=myfile.groupby(graphindex).Quantity.sum()
        mydf = pd.DataFrame(mydf).sort_values(by='Quantity',ascending=False)
        mydf.reset_index()
        fig = px.bar(mydf, x=mydf.index, y=mydf.Quantity, color=mydf.index, barmode="group")
    elif opt=='most_profitable_customer_segment':
        graphindex = "Segment"
        mydf=myfile.groupby(graphindex).Profit_Margin.sum()
        mydf = pd.DataFrame(mydf).sort_values(by='Profit_Margin',ascending=False)
        mydf.reset_index()
        fig = px.bar(mydf, x=mydf.index, y=mydf.Profit_Margin, color=mydf.index, barmode="group",title="Most Profitable Customer Segment")
    elif opt=='prefered_ship_mode': 
        graphindex = "Ship_Mode"
        mydf=myfile.groupby(graphindex).Sales.count()
        mydf = pd.DataFrame(mydf).sort_values(by='Sales',ascending=False)
        mydf.reset_index()
        fig = px.bar(mydf, x=mydf.index, y=mydf.Sales, color=mydf.index, barmode="group",title="Prefered Ship mode")
    elif opt=='most_profitable_region':  
        graphindex = "Region"
        mydf=myfile.groupby(graphindex).Profit_Margin.sum()
        mydf = pd.DataFrame(mydf).sort_values(by='Profit_Margin',ascending=False)
        mydf.reset_index()
        fig = px.bar(mydf, x=mydf.index, y=mydf.Profit_Margin, color=mydf.index, barmode="group",title="Most Profitable Region")
    elif opt=='city_with_highiest_no_sales':  
        graphindex = "City"
        mydf=myfile.groupby(graphindex).Sales.count()
        mydf = pd.DataFrame(mydf).sort_values(by='Sales',ascending=False).head(10)
        mydf.reset_index()
        fig = px.bar(mydf, x=mydf.index, y=mydf.Sales, color=mydf.index, barmode="group",title="City with highiest number of sales")
    else:        
        graphindex = "Category"        
        mydf=myfile.groupby(graphindex).Profit_Margin.sum()
        mydf = pd.DataFrame(mydf).sort_values(by='Profit_Margin',ascending=False)
        mydf.reset_index()
        fig = px.bar(mydf, x=mydf.index, y=mydf.Profit_Margin, color=mydf.index, barmode="group",title="Best Selling and most profitable catgory")
    return fig
html.H3('Collins\' Dash App' '{title}')
if __name__ == '__main__':
    app.run_server(debug=True)
