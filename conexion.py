from dash import Dash, html, dcc
import plotly.express as px
import psycopg2
try:
    connection = psycopg2.connect(
        host = 'localhost',
        user = 'postgres',
        password = 'Y0ongi#23',
        database = 'postgres'
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
    
    app.layout = html.Div(children=[
        html.H1(children='Gráfico Edición Cantidad'),
        html.Div(children='''
            Dash: Aplicación para graficar datos
        '''),
        dcc.Graph(
            id = 'example-graph',
            figure = fig
        )
    ])
    if __name__ == '__main__':
        app.run_server(debug = False)
except Exception as ex:
    print(ex)
finally:
    connection.close()
    print("conexion finalizada")
