from dash import Dash, html, dcc
import plotly.express as px
import psycopg2
try:
    connection = psycopg2.connect(
        host = 'localhost',
        user = 'postgres',
        password = '123456789',
        database = 'Proyecto'
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
    
    fig11 = px.bar(rows, x=0, y=1, title="", labels={'x': 'X-axis', 'y': 'Y-axis'}, height=600, width=1000)
    fig12 = px.pie(rows, values=1, names=0, title="", labels={'x': 'X-axis', 'y': 'Y-axis'}, height=600, width=700)


    cursor = connection.cursor()
    cursor.execute('''select ar.nombre , count(t.ID_evento) as ct_eventos from artista as ar inner join asiste as t on ar.ID = t.Id_artista
    group by ar.nombre;''')
    rows2 = cursor.fetchall()
    app = Dash(__name__)
    
    fig21 = px.bar(rows2, x=0, y=1, title="", labels={'x': 'X-axis', 'y': 'Y-axis'}, height=800, width=1400)

    cursor = connection.cursor()
    cursor.execute('''select e.nombre , count(p.ID_patrocinador) as ct_patrocinadores from patrocina as p inner join evento as e on p.ID_evento = e.ID
    group by e.nombre;''')
    rows3 = cursor.fetchall()
    app = Dash(__name__)
    
    fig31 = px.bar(rows3, x=0, y=1, title="", labels={'x': 'X-axis', 'y': 'Y-axis'}, height=600, width=1000)


    cursor = connection.cursor()
    cursor.execute('''select e.nombre , count(b.ID_evento) as ct_boleteria from empresa_promotora as e inner join boleteria as b on e.ID = b.codigo_boleteria
    group by e.nombre;''')
    rows4 = cursor.fetchall()
    app = Dash(__name__)
    
    fig41 = px.bar(rows4, x=0, y=1, title="", labels={'x': 'X-axis', 'y': 'Y-axis'}, height=600, width=1000)
 
    
 
    cursor = connection.cursor()
    cursor.execute('''select EXTRACT(MONTH FROM fecha_inicio) as mes, count(ID) from evento 
                   group by mes 
                   order by mes asc;''')
    rows5 = cursor.fetchall()
    app = Dash(__name__)
    
    fig51 = px.line(rows5, x=0, y=1, title="", labels={'x': 'X-axis', 'y': 'Y-axis'}, height=600, width=1000)



    cursor = connection.cursor()
    cursor.execute('''select e.nombre, (b.cantidad * b.precio_max) as ganancias from evento as e inner join boleteria as b on e.ID = b.ID_evento;''')
    rows6 = cursor.fetchall()
    app = Dash(__name__)
    
    fig61 = px.bar(rows6, x=0, y=1, title="Ganancias Aproximadas", labels={'x': 'X-axis', 'y': 'Y-axis'}, height=700, width=1500)


    app.layout = html.Div(children=[
        html.H1(children='Conciertos/Eventos Colombia 2023', style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center', 'fontSize': 50}),
        html.H1(children='aaaaaaaa', style={'fontSize': 30, 'color': 'white'}),
        html.H2(children='A lo largo del año 2023 se han realizado diversos conciertos/eventos en Colombia que cuentan con una gran cantidad de artistas y con esto una gran cantidad de audiencia, lo cual da un buen indicio para la economía del país, así como un indicador de una próspera escena musical. Por otro lado, el albergar una gran cantidad de eventos ocasiona que se necesite una infraestructura adecuada que pueda dar un espacio agradable para los espectadores y los artistas, por lo que podemos observar una gran cantidad de centro de eventos en las diversas ciudades del país que los albergaron. ', style={'position': 'relative', 'width': '85%','left': '7.5%', 'justify-content': 'center', 'text-align':'center'}),
        html.H2(children='A partir de esto, decidimos reunir la información de los diversos eventos y realizamos ciertos análisis frente a los datos obtenidos, teniendo lo siguiente: ', style={'position': 'relative', 'width': '85%','left': '7.5%', 'justify-content': 'center', 'text-align':'center'}), 
        html.H1(children='aaaaaaaa', style={'fontSize': 50, 'color': 'white'}),
        html.H2(children='Uso de centro de eventos', style={'text-align': 'left', 'fontSize': 30, 'position': 'relative','left': '6%'}),    
        html.H2(children='El siguiente grafico muestra los diversos centros de eventos y cuantos eventos han sido realizados en estos a lo largo del primer semestre del año.', style={'fontSize': 20, 'position': 'relative','left': '11%'}),    
        html.Div(style={'display': 'flex', 'justify-content': 'left', 'align-items': 'center', 'position': 'relative', 'widht':'1000px', 'left': '6%'},
            children=dcc.Graph(
            id='Barras-Cat',
            figure=fig11
            )
        ),
        html.Div(style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center', 'position': 'relative', 'top': '10%','rigth': '50%'},
            children=dcc.Graph(
            id='Pie-An',
            figure=fig12
        )),
        html.H2(children='Valeria Pillimue: La grafica muestra de manera clara los porcentajes y la cantidad de eventos que hubo en estos centros de eventos, es fácil ver la diferencia entre ellos y la preferencia de los eventos en el Movistar Arena y en el Teatro de la Universidad de Medellín, la grafica nos facilita la comparación entre centros de ventos y la cantidad de ellos. ', style={'fontSize': 20, 'position': 'relative','left': '11%', 'width': '78%'}),    
        html.H1(children='aaaaaaaa', style={'fontSize': 90, 'color': 'white'}),
        html.H2(children='Asistencia de artistas a eventos', style={'text-align': 'left', 'fontSize': 30, 'position': 'relative','left': '6%'}),   
        html.H2(children='El siguiente grafico muestra los diversos artistas que tuvieron presentaciones en el primer semestre del 2023 y la cantidad de eventos en los que participaron.', style={'fontSize': 20, 'position': 'relative','left': '11%'}),    
        html.Div(style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center', },
            children=dcc.Graph(
            id='Barras-Cat',
            figure=fig21
        )),
        html.H2(children='Valeria Pillimue: Aquí se visualiza de manera clara la asistencia de artista y es fácil la comparación entre ellos, las barras nos muestran de manera concreta la cantidad y el artista. La desventaja principal de esta grafica es que dependiendo la cantidad de artistas la visualización puede dificultarse y volverse desordenada, como se puede ver la cantidad de artistas es bastante.', style={'fontSize': 20, 'position': 'relative','left': '11%', 'width': '78%'}),    
        html.H1(children='aaaaaaaa', style={'fontSize': 90, 'color': 'white'}),
        html.H2(children='Eventos patrocinados', style={'text-align': 'left', 'fontSize': 30, 'position': 'relative','left': '6%'}),   
        html.H2(children='El siguiente grafico muestra los eventos que fueron patrocinados, y la cantidad de patrocinadores que los financiaron.', style={'fontSize': 20, 'position': 'relative','left': '11%'}),    
        html.Div(style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center'},
            children=dcc.Graph(
            id='Barras-Cat',
            figure=fig31
        )),
        html.H2(children='Valeria Pillimue: La comparación de los eventos patrocinados es sencilla pues las barras muestran la cantidad exacta de los eventos patrocinados, y la grafica puede ayudar a intuir, por ejemplo, la moda, la cantidad máxima y mínima, entre otros. ', style={'fontSize': 20, 'position': 'relative','left': '11%', 'width': '78%'}),    
        html.H1(children='aaaaaaaa', style={'fontSize': 90, 'color': 'white'}),
        html.H2(children='Boleteria presentes en eventos', style={'text-align': 'left', 'fontSize': 30, 'position': 'relative','left': '6%'}),   
        html.H2(children='El siguiente grafico muestra las diversas empresas de boleteria y cual fue la mas solicitada para la comercialización de los tiquetes para los eventos', style={'fontSize': 20, 'position': 'relative','left': '11%'}),    
        html.Div(style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center'},
            children=dcc.Graph(
            id='Barras-Cat',
            figure=fig41
        )),
        html.H2(children='Valeria Pillimue: Como desventaja principal de esta grafica podemos ver como Tu Boleta tiene a la mayoría de los eventos y las otras empresas quedan bastante abajo lo que dificulta ver la cantidad exacta de eventos con los que trabajan. La comparación en esta grafica es sencilla y muestra bastante las preferencias y los eventos para contratar boletería. ', style={'fontSize': 20, 'position': 'relative','left': '11%', 'width': '78%'}),    
        html.H1(children='aaaaaaaa', style={'fontSize': 90, 'color': 'white'}),
        html.H2(children='Cantidad de eventos durante los primeros meses', style={'text-align': 'left', 'fontSize': 30, 'position': 'relative','left': '6%'}),   
        html.H2(children='El siguiente grafico muestra la cantidad de eventos que se han realizado durante los primeros meses(eje x) del 2023.', style={'fontSize': 20, 'position': 'relative','left': '11%'}),    
        html.Div(style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center'},
            children=dcc.Graph(
            id='lineas-Cat',
            figure=fig51
        )),
        html.H2(children='Valeria Pillimue: Esta grafica facilita ver el crecimiento y decrecimiento de los eventos que se realizan dependiendo de los meses en el año, para estrategias de negocios es importante ver la cantidad de eventos que se desarrollan al mes para decidir si es factible o no realizar otro, otra ventaja es que entre mayor sea la cantidad de meses será más fácil intuir el comportamiento de la gráfica. Como desventaja tenemos que si la cantidad de eventos varía mucho la visualización de estos números puede dificultarse.', style={'fontSize': 20, 'position': 'relative','left': '11%', 'width': '78%'}),    
        html.H1(children='aaaaaaaa', style={'fontSize': 90, 'color': 'white'}),
        # html.H2(children='Eventos durante los primeros meses del año', style={'text-align': 'left', 'fontSize': 25, 'position': 'relative','left': '6%'}),   
        # html.H2(children='El siguiente grafico muestra los diversos centros de eventos y cuantos eventos han sido realizados en estos a lo largo del primer semestre del año.', style={'fontSize': 20, 'position': 'relative','left': '11%'}),    
        # html.Div(style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center'},
        #     children=dcc.Graph(
        #     id='Barras-Vod',
        #     figure=fig61
        # )),
        # html.H2(children='Valeria Pillimue: La grafica muestra de manera clara los porcentajes y la cantidad de eventos que hubo en estos centros de eventos, es fácil ver la diferencia entre ellos y la preferencia de los eventos en el Movistar Arena y en el Teatro de la Universidad de Medellín, la grafica nos facilita la comparación entre centros de ventos y la cantidad de ellos. ', style={'fontSize': 20, 'position': 'relative','left': '11%'}),    
        # html.H1(children='aaaaaaaa', style={'fontSize': 90, 'color': 'white'}),
        html.H1(children='Sección de conclusiones'),
        html.H2(children='Valeria Pillimue: Decidimos crear nuestra propia base de datos, esto dificultó la realización del proyecto pues tuvimos que buscar en varias fuentes y demoró el proceso, sin embargo, gracias a esto pudimos conocer y apropiarnos de la base de datos, sabíamos cómo conectar cada dato que habíamos recolectado y así el diseño de la base de datos se organizó de tal manera que nos facilitara la creación de las tablas. En la carga de datos se obtuvo resultados eficaces pues facilitó la carga en PgAdmin y lograr organizar la base de datos con sus respectivas tablas en PostgreSQL, además con las visualizaciones anteriores que habíamos realizado en el modelo relacional y la tablas en PgModeler, la realización del código en SQL se nos facilitó. Las dificultades estuvieron al momento del desarrollo de conexiones de bases de datos con Python donde el código muchas veces no funcionaba y las máquinas virtuales tampoco nos permitían avanzar mucho en el proceso. Python y la realización de la página fueron los procesos más arduos pero que se concluyeron, organizando los códigos y apropiándolos a nuestra base de datos y a lo que queríamos mostrar en nuestro proyecto se realizó la visualización de nuestra base de datos en las gráficas y la organización que tuvimos en todo el proceso.', style={'fontSize': 20, 'position': 'relative','left': '5%', 'width': '90%'}),    
        
    ])
    if __name__ == '__main__':
        app.run_server(debug = False)
except Exception as ex:
    print(ex)
finally:
    connection.close()
    print("conexion finalizada")
