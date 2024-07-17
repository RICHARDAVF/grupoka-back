from fastapi import FastAPI
from conexion import CAQ
app = FastAPI()

@app.get("/")
def get_data():
    data = []
    try:
        sql = "SELECT aux_clave,aux_docum FROM t_auxiliar"
        params = ()
        res = CAQ.query(sql,params)
        data = [
            {
                'id':index,
                "codigo":value[0].strip(),
                "documento":value[1].strip()
            } for index,value in enumerate(res)
        ]
    except Exception as e:
        data = {"error":str(e)}
    
    return data