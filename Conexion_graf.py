from dash import Dash, html, dcc
import plotly.express as px
import psycopg2
try:
    connection = psycopg2.connect(
        host = 'localhost',
        user = 'postgres',
        password = '123456789',
        database = 'pr4'
    )
    print("conexion Exitosa")
    cursor = connection.cursor()

    #Ciudad
    cursor.execute("select * from ciudad")
    rows=cursor.fetchall()
    for row in rows:
        print(row)
    app = Dash(__name__)
    fig = px.pie(rows, values=1, names=0, color_discrete_sequence=["#c0ffee"])
    
    #Centro de eventos
    cursor.execute("select * from centro_de_eventos")
    rows1=cursor.fetchall()
    for row in rows1:
        print(row)
    app = Dash(__name__)
    fig = px.pie(rows, values=1, names=0, color_discrete_sequence=["#c0ffee"])

    #Evento
    cursor.execute("select * from evento")
    rows=cursor.fetchall()
    for row in rows:
        print(row)
    app = Dash(__name__)
    fig = px.pie(rows, values=1, names=0, color_discrete_sequence=["#c0ffee"])

    #Patrocina
    cursor.execute("select * from patrocina")
    rows=cursor.fetchall()
    for row in rows:
        print(row)
    app = Dash(__name__)
    fig = px.pie(rows, values=1, names=0, color_discrete_sequence=["#c0ffee"])
    
    #Asiste
    cursor.execute("select * from asiste")
    rows=cursor.fetchall()
    for row in rows:
        print(row)
    app = Dash(__name__)
    fig = px.pie(rows, values=1, names=0, color_discrete_sequence=["#c0ffee"])

    #Artista
    cursor.execute("select * from artista")
    rows=cursor.fetchall()
    for row in rows:
        print(row)
    app = Dash(__name__)
    fig = px.pie(rows, values=1, names=0, color_discrete_sequence=["#c0ffee"])
    
    #Boleteria
    cursor.execute("select * from boleteria")
    rows=cursor.fetchall()
    for row in rows:
        print(row)
    app = Dash(__name__)
    fig = px.pie(rows, values=1, names=0, color_discrete_sequence=["#c0ffee"])
    
    
    cursor = connection.cursor()
    cursor.execute('''select c.nombre , count(e.codigo_centro_de_eventos) as ct_eventos from centro_de_eventos as c inner join evento as e on c.codigo = e.codigo_centro_de_eventos
    group by c.nombre;''')
    rows = cursor.fetchall()
    app = Dash(__name__)
    
    fig11 = px.bar(rows, x=0, y=1, title="Uso de centro de eventos", labels={'x': 'X-axis', 'y': 'Y-axis'}, height=600, width=1000)
    fig12 = px.pie(rows, values=1, names=0, title="Ingresos por año", labels={'x': 'X-axis', 'y': 'Y-axis'}, height=600, width=700)


    cursor = connection.cursor()
    cursor.execute('''select ar.nombre , count(t.ID_evento) as ct_eventos from artista as ar inner join asiste as t on ar.ID = t.Id_artista
    group by ar.nombre;''')
    rows2 = cursor.fetchall()
    app = Dash(__name__)
    
    fig21 = px.bar(rows2, x=0, y=1, title="Asistencia de artistas a eventos", labels={'x': 'X-axis', 'y': 'Y-axis'}, height=800, width=2000)

    cursor = connection.cursor()
    cursor.execute('''select e.nombre , count(p.ID_patrocinador) as ct_patrocinadores from patrocina as p inner join evento as e on p.ID_evento = e.ID
    group by e.nombre;''')
    rows3 = cursor.fetchall()
    app = Dash(__name__)
    
    fig31 = px.bar(rows3, x=0, y=1, title="Eventos patrocinados", labels={'x': 'X-axis', 'y': 'Y-axis'}, height=800, width=2000)


    cursor = connection.cursor()
    cursor.execute('''select e.nombre , count(b.ID_evento) as ct_boleteria from empresa_promotora as e inner join boleteria as b on e.ID = b.codigo_boleteria
    group by e.nombre;''')
    rows4 = cursor.fetchall()
    app = Dash(__name__)
    
    fig41 = px.bar(rows4, x=0, y=1, title="Boleteria", labels={'x': 'X-axis', 'y': 'Y-axis'}, height=800, width=2000)
    
    app.layout = html.Div(children=[
        html.H1(children='Conciertos/Eventos Colombia 2023', style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center', 'fontSize': 50}),
        html.H1(children='aaaaaaaa', style={'fontSize': 30, 'color': 'white'}),
        html.H2(children='A lo largo del año 2023 se han realizado diversos conciertos/eventos en Colombia que cuentan con una gran cantidad de artistas y con esto una gran cantidad de audiencia, lo cual da un buen indicio para la economia del pais asi como un indicador de una próspera escena musical. Por otro lado, el albergar una gran cantidad de eventos ocasiona que se necesite una infraestructura adecuada que pueda dar un espacio agradable para los espectadores y los artistas, por lo que podemos observar una gran cantidad de centro de eventos en las diversas ciudades del pais que albergaron dichos eventos'),
        #html.Div(children='Diagrama de barras:', style={'fontSize': 20}),
        html.Div(style={'display': 'flex', 'justify-content': 'left', 'align-items': 'left'},
            children=dcc.Graph(
            id='Barras-Cat',
            figure=fig11
            )
        ),
        html.Div(children='Diagrama de pie:', style={'fontSize': 20}),
        html.Div(style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center'},
            children=dcc.Graph(
            id='Pie-An',
            figure=fig12
        )),
        html.Div(style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center'},
            children=dcc.Graph(
            id='Barras-Cat',
            figure=fig21
        )),
        html.Div(style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center'},
            children=dcc.Graph(
            id='Barras-Cat',
            figure=fig31
        )),
        html.Div(style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center'},
            children=dcc.Graph(
            id='Barras-Cat',
            figure=fig41
        )),
        html.H1(children='Seccion de discusion'),
        html.H2(children='Santiago: '),
        html.H1(children='Seccion de conclusiones'),
        html.H2(children='Santiago: ')
    ])
    if __name__ == '__main__':
        app.run_server(debug = False)
except Exception as ex:
    print(ex)
finally:
    connection.close()
    print("conexion finalizada")
