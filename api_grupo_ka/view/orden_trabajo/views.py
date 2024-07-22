from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from api_grupo_ka.conexion import CAQ
class ListOT(GenericAPIView):
    def post(self,request,*args,**kwargs):
        datos = request.data
        option = datos['option']
        if option == 'open':
            params = '<'
        elif option == 'close':
            params = '=' 
        sql = f"""
            SELECT 
                a.mov_compro,
                a.mov_cotiza,
                ISNULL(b.aux_razon,''),
                a.cot_placa,
                a.cot_chasis,
                tec_avance 
            FROM cabetecnico AS a 
            LEFT JOIN t_auxiliar b ON a.mov_codaux=b.aux_clave 
            WHERE tec_avance{params}100
            """
        part = """ WHERE a.elimini=0 AND a.mov_codaux='' 
                AND a.mov_fecha>=''
                AND a.mov_fecha<='' 
                AND a.mov_compro=''"""
        data = {}
        try:
            
            res = CAQ.query(sql,())
            data = [
                {
                'index':index,
                'numero_ot':value[0].strip(),
                'numero_cotizacion':value[1].strip(),
                'cliente':value[2].strip(),
                "placa":value[3].strip(),
                'chasis':value[4].strip(),
                "avance":value[5]

            } for index,value in enumerate(res)]
        except Exception as e:
            data['error'] = str(e)
        return Response(data)