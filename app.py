#!/usr/bin/env python
# coding: utf-8

# In[1]:


import dash
import dash_bootstrap_components as dbc
from dash import html
from dash.exceptions import PreventUpdate
import pandas as pd
from dash.dependencies import Input, Output
import plotly.express as px
import random
from dash import dash_table
from dash import dcc


# In[2]:


past = pd.read_csv('dj_past_history.csv')
present = pd.read_csv('dj_present_data.csv')


# In[3]:


def pastdata(entered_year):
    past = pd.read_csv('dj_past_history.csv')
    
    if(entered_year=='2007-2021'):
        past=past.copy()
        
    else:
        past = past[past['year']==int(entered_year)].copy()
     
   
    
    df4=past[['months','Number of Drinks']]
    month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep','Oct', 'Nov', 'Dec']
    df4.months=pd.Categorical(df4.months,categories=month,ordered=True)
    df4.reset_index(inplace=True)
    df4 =df4.groupby(['months'])[['Number of Drinks']].sum().reset_index() 
    
    
    
    df1 = past[['months','Number of Nitroson10 Tablet ']]
    month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep','Oct', 'Nov', 'Dec']
    df1.months=pd.Categorical(df1.months,categories=month,ordered=True)
    df1.reset_index(inplace=True)
    df1 =df1.groupby(['months'])[['Number of Nitroson10 Tablet ']].sum().reset_index()
    
    
    
    df2 = past[['months','Sulfadocxine-Pyrimethamine']]
    month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep','Oct', 'Nov', 'Dec']
    df2.months=pd.Categorical(df2.months,categories=month,ordered=True)
    df2.reset_index(inplace=True)
    df2 =df2.groupby(['months'])[['Sulfadocxine-Pyrimethamine']].sum().reset_index()
    
    return [df4,df1,df2]


# In[4]:


def drawfigpast(entered_year):
    [df4,df1,df2]=pastdata(entered_year)
    if(entered_year=='2018-2021'):
        fig1=px.bar(df4,x='months', y= 'Number of Drinks',color='months',color_discrete_sequence=['black','blue','red','pink','green','Gray','orange','purple','brown','cyan','olive','lime'],title='Total number of drinks in  a month')
        
        fig1.update_layout(
            autosize=False,
            width=1500,
            height=1000,
            margin=dict(
                l=70,
                r=50,
                b=100,
                t=100,
                pad=4))     
        
        fig2=px.bar(df1,x='months',y='Number of Nitroson10 Tablet ',color='months',color_discrete_sequence=['black','blue','red','pink','green','Gray','orange','purple','brown','cyan','olive','lime'],
        title='Total number n10 use in month')
        fig2.update_layout(
            autosize=False,
            width=600,
            height=600,
            margin=dict(
                l=70,
                r=50,
                b=100,
                t=100,
                pad=4))     
        
        fig3= px.bar(df2,x='months',y='Sulfadocxine-Pyrimethamine',color='months',color_discrete_sequence=['black','blue','red','pink','green','Gray','orange','purple','brown','cyan','olive','lime'],
        title='Number of Sp drugs use in month')
        fig3.update_layout(
            autosize=False,
            width=600,
            height=600,
            margin=dict(
                l=70,
                r=50,
                b=100,
                t=100,
                pad=4))     
        
        
    else:
        fig1=px.bar(df4,x='months', y= 'Number of Drinks',color='months',color_discrete_sequence=['black','blue','red','pink','green','Gray','orange','purple','brown','cyan','olive','lime'],
        title='Total number of drinks in  a month')
        fig1.update_layout(
            autosize=False,
            width=600,
            height=600,
            margin=dict(
                l=70,
                r=50,
                b=100,
                t=100,
                pad=4))     
        
        fig2=px.bar(df1,x='months',y='Number of Nitroson10 Tablet ',color='months',color_discrete_sequence=['black','blue','red','pink','green','Gray','orange','purple','brown','cyan','olive','lime'],
        title='Total number n10 use in month')
        fig2.update_layout(
            autosize=False,
            width=600,
            height=600,
            margin=dict(
                l=70,
                r=50,
                b=100,
                t=100,
                pad=4))     
        
        fig3= px.bar(df2,x='months',y='Sulfadocxine-Pyrimethamine',color='months',color_discrete_sequence=['black','blue','red','pink','green','Gray','orange','purple','brown','cyan','olive','lime'],
        title='Number of Sp drugs use in month')
        fig3.update_layout(
            autosize=False,
            width=600,
            height=600,
            margin=dict(
                l=70,
                r=50,
                b=100,
                t=100,
                pad=4))     
        
      
    return[fig1,fig2,fig3]


# In[5]:


def presenttdata(entered_year):
    present = pd.read_csv('dj_present_data.csv')
    
    if(entered_year=='2022'):
        present=present.copy()
        
    else:
        present = present[present['year']==int(entered_year)].copy()
     
   
    
    d1 =present.groupby(['Number of working hour'])[['Time DJ sleep']].sum().reset_index()
    d1.reset_index(inplace = True)
    
    
    
    
    d2 =present.groupby(['Number of working hour'])[['Time Dj woke up']].count().reset_index()
    d2.reset_index(inplace = True)
    
    
    d3 = present.groupby(['items']).sum()[['time spend']]
    d3.reset_index(inplace = True)
    d3
    return[d1,d2,d3]


# In[6]:


def drawfigpresent(entered_year):
    [d1,d2,d3]=presenttdata(entered_year)
    if(entered_year=='2022'):
        fig1=px.bar(d1,x='Number of working hour', y= 'Time DJ sleep',color='Number of working hour',title='Working hour affect Dj sleeping')
        fig1.update_layout(
            autosize=False,
            width=600,
            height=600,
            margin=dict(
                l=70,
                r=50,
                b=100,
                t=100,
                pad=4))  
        
        fig2=px.bar(d2,x='Number of working hour',y='Time Dj woke up',color='Number of working hour',title='Number working hour affect to wake up DJ')
        fig2.update_layout(
            autosize=False,
            width=600,
            height=600,
            margin=dict(
                l=70,
                r=50,
                b=100,
                t=100,
                pad=4))  
        
        fig3=px.pie(d3,values='time spend',names='items',color='items',title='Total time spend for the present year')
        fig3.update_layout(
            autosize=False,
            width=600,
            height=600,
            margin=dict(
                l=70,
                r=50,
                b=100,
                t=100,
                pad=4)) 
        
        
    else:
        fig1=px.bar(d1,x='Number of working hour', y= 'Time DJ sleep',color='Number of working hour',title='Working hour affect Dj sleeping')
        fig1.update_layout(
            autosize=False,
            width=600,
            height=600,
            margin=dict(
                l=70,
                r=50,
                b=100,
                t=100,
                pad=4))
        
        fig2=px.bar(d2,x='Number of working hour',y='Time Dj woke up',color='Number of working hour',title='Number working hour affect to wake up DJ')
        fig2.update_layout(
            autosize=False,
            width=600,
            height=600,
            margin=dict(
                l=70,
                r=50,
                b=100,
                t=100,
                pad=4))
        
        fig3=px.pie(d3,values='time spend',names='items',color='items',title='Total time spend for the present year')
        fig3.update_layout(
            autosize=False,
            width=600,
            height=600,
            margin=dict(
                l=70,
                r=50,
                b=100,
                t=100,
                pad=4))
        
        
      
    return[fig1,fig2,fig3]


# In[7]:


app = dash.Dash(external_stylesheets=[dbc.themes.DARKLY, dbc.icons.FONT_AWESOME])
app.title = "Dj History Data"
server = app.server


# In[8]:


year= ['2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022','2007-2021']
app.layout = dbc.Container([
    
     html.Div(
    [
        dbc.Spinner(color="#F0F8FF"),
        dbc.Spinner(color="#FF7F50"),
        dbc.Spinner(color="#B22222"),
        dbc.Spinner(color="#FF69B4"),
        dbc.Spinner(color="#FFFACD"),
        dbc.Spinner(color="#0000FF"),
        dbc.Spinner(color="#000000"),
        dbc.Spinner(color="#FFFFFF"),
    ]
),
    
    html.H1("DJ PAST AND PRESENT STORY DATA",style={'textAlign':'center','color':'#FFFFFF','fontsize':50}),
    
    
    html.Div([
        
       dbc.Card(
        [
            dbc.CardImg(src="https://scontent.fpbh1-1.fna.fbcdn.net/v/t39.30808-6/274988959_401490171653373_690321612480513129_n.jpg?_nc_cat=106&ccb=1-5&_nc_sid=09cbfe&_nc_ohc=cmC3MWOb9a8AX9jlMpE&tn=W5SX6pWYbelhl792&_nc_ht=scontent.fpbh1-1.fna&oh=00_AT-JQ3k_aDytn4fxbmZMb9G5Z_e5FmF0MsgJTdantK-XwA&oe=622DAAD7", top=True),
            dbc.CardBody(
                [
                    html.H4("All About Karma Wangchuk(DJ)", className="Viewdj"),
                    html.P(
                        "Some details about karma wangchuk"
                        "How i was before",
                        className="card-text",
                    ),
                    dbc.Button("Veiw dj details", color="primary"),
                ]),

      ],style={"width": "18rem"}),
              
    
    html.Div(
    [
        dbc.Alert("Drinking is injuries to Health", color="#FF7F50"),
        dbc.Alert("Abuseing drugs will lead to death and fight", color="#B22222"),
        dbc.Alert("More you work harder you will leran and lead your own", color="#0000FF"),
        
    ],style={' margin-bottom': '15px'}),
    ],style={'display':'flex'}),


    dbc.Tabs([
            dbc.Tab(label="Past data", tab_id="before"),
            dbc.Tab(label="Present data", tab_id="now"),
            ], id="tabs", active_tab="before",
        ),
    html.Div([
        html.Div([
            html.H2('Select_Year',style={'textAlign':'left','color':'blue','fontsize':40}),
            dcc.Dropdown(id='year_list',value='2007-2021',clearable=False,
                    options=[{'label':i,'value':i} for i in year ],
                    placeholder='' 
                    ),
        ],id='dd',style={'width':'40%','color':'red','padding':'3px','fontsize':40}),
        
    ],id='dd_plus_value',style={'display':'flex'}),
    
    html.Br(),
       
    # output graph
    html.Div([
        # output graphic (plot1)
        dcc.Graph(id='plot1')
             ],style={ 'marginLeft': 5, 'marginRight': 11, 'marginTop': 6, 'marginBottom': 6,
           'backgroundColor':'#F7FBFE',
           'border': 'thin lightgrey dashed', 'padding': '6px 0px 0px 8px'}),
    html.Div([dcc.Graph(id='plot3'),
             dcc.Graph(id='plot2')],style = {'display': 'flex','marginLeft': 5, 'marginRight': 11, 'marginTop': 6, 'marginBottom': 6,
           'backgroundColor':'#F7FBFE',
           'border': 'thin lightgrey dashed', 'padding': '6px 0px 0px 8px'}),
    
    html.Br(),
    
    dbc.Tabs([
            dbc.Tab(label="DJ_Past data", tab_id="past_data"),
            dbc.Tab(label="DJ_Present data", tab_id="present_data"),
            ], id="tabs1", active_tab="past_data"),
    
    html.Div(id="table"),
        
])


# In[9]:


@app.callback(
    Output("table", "children"),
    Input('tabs1','active_tab'),
)

def make_table(a):
        
    if(a == 'past_data'):
        df = pd.read_csv('dj_past_history.csv')
        
    elif(a == 'present_data'):
        df = pd.read_csv('dj_present_data.csv')
        
    else:
        df = pd.read_csv('dj_past_history.csv')
        
    return dbc.Table.from_dataframe(df, striped=True, bordered=True, color = "primary", hover=True)


# In[10]:


@app.callback([
    
    Output('plot1','figure'),
    Output('plot2','figure'),
    Output('plot3','figure')
    
],[Input('year_list','value'),
  Input('tabs','active_tab')])

def draw_graph(entered_year,tabs):
    if entered_year is None or tabs is None:
        raise PreventUpdate
    else:
        if (tabs=='before'):
            [fig1,fig2,fig3]=drawfigpast(entered_year)
        elif(tabs=='now'):
            
            [fig1,fig2,fig3]=drawfigpresent(entered_year)   
        else:
            [fig1,fig2,fig3]=drawfigpast(entered_year)

    return [fig1,fig2,fig3]


# In[ ]:


if __name__ == '__main__':
    port = 5000 + random.randint(0, 999)    
    url = "http://127.0.0.1:{0}".format(port)    
    app.run_server(use_reloader=False, debug=True, port=port)

