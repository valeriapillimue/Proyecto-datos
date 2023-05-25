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
    
    fig11 = px.bar(rows, x=0, y=1, title="Uso de centro de eventos", labels={'x': 'X-axis', 'y': 'Y-axis'}, height=800, width=2000)


    cursor = connection.cursor()
    cursor.execute('''select ar.nombre , count(t.ID_evento) as ct_eventos from artista as ar inner join asiste as t on ar.ID = t.Id_artista
    group by ar.nombre;''')
    rows = cursor.fetchall()
    app = Dash(__name__)
    
    fig12 = px.bar(rows, x=0, y=1, title="Asistencia de artistas a eventos", labels={'x': 'X-axis', 'y': 'Y-axis'}, height=800, width=2000)

       
    app.layout = html.Div(children=[
        html.H1(children='Gráfico Edición Cantidad'),
        html.Div(children='''
            Dash: Aplicación para graficar datos
        '''),
        html.Div(children='Diagrama de barras:', style={'fontSize': 20}),
        html.Div(style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center'},
            children=dcc.Graph(
            id='Barras-Cat',
            figure=fig11
        )),
        html.Div(style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center'},
            children=dcc.Graph(
            id='Barras-Cat',
            figure=fig12
        ))
    ])
    if __name__ == '__main__':
        app.run_server(debug = False)
except Exception as ex:
    print(ex)
finally:
    connection.close()
    print("conexion finalizada")

