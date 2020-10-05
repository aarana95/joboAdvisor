import sqlite3

#Creamos una BBDD para almacenar los espectaculos que hemos avisado
#sqlite3.connect('espectaculos.db')

conn = sqlite3.connect('espectaculos.db')
c = conn.cursor()

# Create table - CLIENTS
c.execute('''CREATE TABLE ESPECTACULOS
             ([Titulo] text, [Dia] text, [Hora] text, [Sitio] text)
             '''
          )
conn.commit()