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
        html.Div(style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center', 'position': 'relative'},
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
        html.H2(children='Alisson Daza: En las dos primeras graficas podemos observar que la mayoría de los eventos fueron realizados tanto en el Movistar Arena como en el Teatro de la universidad de Medellín, y también podemos notar que en muchos de los centros solo se ha realizado un evento. A mi parecer creo que esta mejor usar la gráfica de pastel ya que además de estar organizada por porcentajes, la diferencia de colores también ayuda a encontrar de mejor forma el centro de eventos que se esté buscando. ', style={'fontSize': 20, 'position': 'relative','left': '11%', 'width': '78%'}),    
        html.H2(children='David Vargas: La gráfica de barras nos da un buen acercamiento a cuantos eventos se realizaron en cada uno de los centros de eventos, permitiéndonos determinar cuál de los centros de eventos fue el más usado. Por otro lado, el diagrama circular nos permite también observar de manera clara cuál de los centros de eventos fue el más usado durante el primer semestre del 2023, además de proporcionarnos cual es el porcentaje de eventos que se presentaron en cada uno. ', style={'fontSize': 20, 'position': 'relative','left': '11%', 'width': '78%'}),    
        html.H1(children='aaaaaaaa', style={'fontSize': 90, 'color': 'white'}),
        html.H2(children='Asistencia de artistas a eventos', style={'text-align': 'left', 'fontSize': 30, 'position': 'relative','left': '6%'}),   
        html.H2(children='El siguiente grafico muestra los diversos artistas que tuvieron presentaciones en el primer semestre del 2023 y la cantidad de eventos en los que participaron.', style={'fontSize': 20, 'position': 'relative','left': '11%'}),    
        html.Div(style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center', },
            children=dcc.Graph(
            id='Barras-Cat',
            figure=fig21
        )),
        html.H2(children='Valeria Pillimue: Aquí se visualiza de manera clara la asistencia de artista y es fácil la comparación entre ellos, las barras nos muestran de manera concreta la cantidad y el artista. La desventaja principal de esta grafica es que dependiendo la cantidad de artistas la visualización puede dificultarse y volverse desordenada, como se puede ver la cantidad de artistas es bastante.', style={'fontSize': 20, 'position': 'relative','left': '11%', 'width': '78%'}),    
        html.H2(children='Alisson Daza: En esta grafica podemos afirmar que todos los artistas menos 3 se presentaron solo una vez en un evento, aunque podemos considerar como una desventaja el tipo de gráfica y la cantidad de artistas que se presentaron ya que es difícil de ver a primera vez sin confundirse, también teniendo en cuenta que todas las barras de artista tienen el mismo color lo que la hace más complicada de analizar.', style={'fontSize': 20, 'position': 'relative','left': '11%', 'width': '78%'}),    
        html.H2(children='David Vargas: Esta grafica nos permite observar de una manera muy clara cuales fueron los artistas que se presentaron a más eventos durante el primer semestre del año 2023, además de mostrárnoslo de una forma que no es difícil de entender. Por otro lado, debido a la gran cantidad de artistas, la gráfica no queda de una forma muy agradable para los espectadores, pues se presenta una gran cantidad de datos acumulados, lo cual nos deja con la idea de que hubiera sido optimo utilizar otro gráfico.', style={'fontSize': 20, 'position': 'relative','left': '11%', 'width': '78%'}),    
        html.H1(children='aaaaaaaa', style={'fontSize': 90, 'color': 'white'}),
        html.H2(children='Eventos patrocinados', style={'text-align': 'left', 'fontSize': 30, 'position': 'relative','left': '6%'}),   
        html.H2(children='El siguiente grafico muestra los eventos que fueron patrocinados, y la cantidad de patrocinadores que los financiaron.', style={'fontSize': 20, 'position': 'relative','left': '11%'}),    
        html.Div(style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center'},
            children=dcc.Graph(
            id='Barras-Cat',
            figure=fig31
        )),
        html.H2(children='Valeria Pillimue: La comparación de los eventos patrocinados es sencilla pues las barras muestran la cantidad exacta de los eventos patrocinados, y la grafica puede ayudar a intuir, por ejemplo, la moda, la cantidad máxima y mínima, entre otros. ', style={'fontSize': 20, 'position': 'relative','left': '11%', 'width': '78%'}),    
        html.H2(children='Alisson Daza: Esta grafica es simple al ser muy pocos los eventos por lo tanto el tipo de gráfica que utilizamos es la adecuada, ya que a simple vista podemos ver la cantidad de patrocinadores que tuvo cada uno de los eventos, que en este caso eran solo festivales.', style={'fontSize': 20, 'position': 'relative','left': '11%', 'width': '78%'}),    
        html.H2(children='David Vargas: Debido a que los datos que se utilizan para este escenario no son demasiados, el uso del grafico de barras nos permite comparar de una forma sencilla cuál de los eventos tuvo una mayor cantidad de patrocinadores. Además de que debido a la poca cantidad eventos patrocinados con los que contamos, la grafica se observa de una manera más organizada y agradable.', style={'fontSize': 20, 'position': 'relative','left': '11%', 'width': '78%'}),    
        html.H1(children='aaaaaaaa', style={'fontSize': 90, 'color': 'white'}),
        html.H2(children='Boleteria presentes en eventos', style={'text-align': 'left', 'fontSize': 30, 'position': 'relative','left': '6%'}),   
        html.H2(children='El siguiente grafico muestra las diversas empresas de boleteria y cual fue la mas solicitada para la comercialización de los tiquetes para los eventos', style={'fontSize': 20, 'position': 'relative','left': '11%'}),    
        html.Div(style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center'},
            children=dcc.Graph(
            id='Barras-Cat',
            figure=fig41
        )),
        html.H2(children='Valeria Pillimue: Como desventaja principal de esta grafica podemos ver como Tu Boleta tiene a la mayoría de los eventos y las otras empresas quedan bastante abajo lo que dificulta ver la cantidad exacta de eventos con los que trabajan. La comparación en esta grafica es sencilla y muestra bastante las preferencias y los eventos para contratar boletería. ', style={'fontSize': 20, 'position': 'relative','left': '11%', 'width': '78%'}),    
        html.H2(children='Alisson Daza: Teniendo en cuenta que la escala sobre la cual trabaja la gráfica creo que esta cuenta como una desventaja debido a que no se tiene un registro exacto de cuantos eventos tuvo cada boletería, la ventaja que tiene esta es que al ser tan pocas empresas de boletería, no es inextricable visualizar la diferencia entre ellas.', style={'fontSize': 20, 'position': 'relative','left': '11%', 'width': '78%'}),    
        html.H2(children='David Vargas: El grafico que se nos presenta nos muestra cual de las empresas de boletería fue la que más se solicitó para los diversos eventos, lo cual se puede apreciar de una forma sencilla y versátil ya que no son muchas empresas de boletería. Por otro lado, la principal desventaja de usar dicha grafica es la escala en la que nos da la cantidad de eventos, pues no se puede determinar de forma exacta cuantos eventos solicitaron cada una de las empresas de boletería. ', style={'fontSize': 20, 'position': 'relative','left': '11%', 'width': '78%'}),    
        html.H1(children='aaaaaaaa', style={'fontSize': 90, 'color': 'white'}),
        html.H2(children='Cantidad de eventos durante los primeros meses', style={'text-align': 'left', 'fontSize': 30, 'position': 'relative','left': '6%'}),   
        html.H2(children='El siguiente grafico muestra la cantidad de eventos que se han realizado durante los primeros meses(eje x) del 2023.', style={'fontSize': 20, 'position': 'relative','left': '11%'}),    
        html.Div(style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center'},
            children=dcc.Graph(
            id='lineas-Cat',
            figure=fig51
        )),
        html.H2(children='Valeria Pillimue: Esta grafica facilita ver el crecimiento y decrecimiento de los eventos que se realizan dependiendo de los meses en el año, para estrategias de negocios es importante ver la cantidad de eventos que se desarrollan al mes para decidir si es factible o no realizar otro, otra ventaja es que entre mayor sea la cantidad de meses será más fácil intuir el comportamiento de la gráfica. Como desventaja tenemos que si la cantidad de eventos varía mucho la visualización de estos números puede dificultarse.', style={'fontSize': 20, 'position': 'relative','left': '11%', 'width': '78%'}),    
        html.H2(children='Alisson Daza: Considero que esta grafica es una gran desventaja debido a que no es claro el número de eventos por día o por mes, tampoco se sabe con precisión el intervalo de tiempo sobre el que estamos trabajando, ni la escala de cantidad de eventos porque sucede algo muy parecido a lo que pasó con la gráfica de boletería.', style={'fontSize': 20, 'position': 'relative','left': '11%', 'width': '78%'}),    
        html.H2(children='David Vargas: Este grafico nos muestra, de cierta forma, como es que a medida que avanzan los meses la cantidad de eventos que se van realizando va aumentando hasta Marzo (3) pues a partir de este punto vuelven a disminuir los eventos. La principal desventaja, es que este grafico no resulto muy bien planteado puesto que el eje x no esta muy bien especificado dado que este representa los meses; con respecto al eje y, la cantidad de eventos si se ve reflejada de una buena manera. ', style={'fontSize': 20, 'position': 'relative','left': '11%', 'width': '78%'}),    
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
        html.H2(children='Alisson Daza: Primero al decidir el tema, queríamos usar un tema que no fuera tan monótono, así que escogimos este de los conciertos y festivales. Luego, al no encontrar bases de datos elegimos hacer la nuestra, fue un poco difícil debido a que teníamos que buscar en muchas fuentes para poder llenarla con datos reales a fecha con la información completa. Después de esto, la creación de las tablas en PgAdmin ya fue fácil debido a que ya sabíamos cómo funcionaba, al igual que como lo representamos en nuestro diagrama relacional hecho en PgModeler, el primer “problema” que tuvimos fue al momento de la conexión de los datos desde nuestra base en Excel a las tablas que ya habíamos creado en Postgres, Posterior a solucionar dicho “problema” pasamos al otro, que fue crear el vínculo entre las tablas ya llenas en PgAdmin con el módulo Dash en Python ya que estos se encontraban frecuentemente con fallos desde las máquinas de la sala. Y ya por último solucionados nuestras dificultades para la finalización del proyecto, logramos realizar la conexión y visualización de las gráficas que habíamos generado como respuestas a las preguntas que habíamos hecho para demostrar la eficiencia y funcionalidad de nuestra base de datos.', style={'fontSize': 20, 'position': 'relative','left': '5%', 'width': '90%'}),    
        html.H2(children='David Vargas: El desarrollo del actual proyecto fue un trabajo algo extenso pues desde un principio tuvimos que desarrollar nuestra propia base de datos recopilando información de diversas fuentes a cerca de los eventos que se realizaron en Colombia en 2023. Después de esto tuvimos que normalizar la base de datos, y con esto realizado desarrollar el diagrama ER para después pasarlo al PgModeler y construir el diagrama relacional; durante todo este proceso lo más frustrante fue que al no normalizar bien la base de datos tuvimos que corregir después nuestro modelo relacional. Una parte algo sencilla, pero que se no se trabajo con la disciplina necesaria fue la carga de datos pues, aunque no era un trabajo muy complicado en un comienzo, no lo realizamos de manera completa. Luego, después de organizar bien las tablas y los datos a subir, siguió otro proceso que no nos demoró mucho y fue la conexión con la base de datos pues ya contábamos con un modelo realizado durante la clase. El trabajo con dash fue un poco más complicado de lo que pensábamos pues, aunque ya habíamos trabajado algo durante la clase, fue necesario investigar algunas cosas más por nuestra cuenta para poder organizar de una manera más presentable la página web, y aunque no obtuvimos el mejor resultado con la pagina web, pudimos obtener unos resultados organizados y que podíamos comprender.', style={'fontSize': 20, 'position': 'relative','left': '5%', 'width': '90%'}),    
            
    ])
    if __name__ == '__main__':
        app.run_server(debug = False)
except Exception as ex:
    print(ex)
finally:
    connection.close()
    print("conexion finalizada")
