import sqlite3
import os
import insertar
dir = str(os.path.dirname(os.path.abspath(__file__)))
conn = sqlite3.connect(dir+'/db.sqlite3')

id = '29'
c = conn.cursor()
c.execute("SELECT * from basedatos_bienesyservicios WHERE idreg_id=?", (id,))
rows = c.fetchall()

for cv in rows:

  insertar.in_datos_productos(cv[2],cv[3],cv[4],cv[5],cv[6],cv[7],cv[8],cv[1],'unidad',1)
  pass


