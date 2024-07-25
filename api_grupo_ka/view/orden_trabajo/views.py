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
            WHERE 
                tec_avance{params}100
                AND a.elimini=0 
                AND a.mov_codaux=? 
            ORDER BY a.mov_compro DESC
            """
        data = {}
        try:
            params = (datos['codigo'],)
            res = CAQ.query(sql,params)
            
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
class StateView(GenericAPIView):
    def post(self,request,*args,**kwargs):
        data = {}
        try:
            datos = request.data
            sql = f"""
                SELECT 
                    tec_actare,
                    tec_revire,
                    tec_proyec,
                    tec_asigna,
                    tec_posici,
                    tec_aproba,
                    tec_disefa,
                    tec_contca,
                    tec_equipa,
                    tec_montem,
                    tec_inelec,
                    tec_inacce,
                    tec_pdi,
                    tec_pruefu,
                    tec_contc2,
                    tec_docume,
                    tec_actaen,
                    tec_firmaa,
                    tec_factur,
                    tec_soppv,
                    tec_avance 
                FROM cabetecnico
                WHERE 
                    MOV_COMPRO=?
                    AND mov_cotiza=?
    """
            params = (datos['numero_ot'],datos['numero_cotizacion'])
            res = CAQ.query(sql,params,0)
            data = {
                "acta_recepcion":res[0]==1,
                "revision":res[1]==1,
                "proyecto":res[2]==1,
                "asignacion":res[3]==1,
                "posiciones":res[4]==1,
                "aprobacion":res[5]==1,
                "disain":res[6]==1,
                "calidad1":res[7]==1,
                "equipamiento":res[8]==1,
                "montaje":res[9]==1,
                "instalacion_electrica":res[10]==1,
                "instalacion_accesorio":res[11]==1,
                "pdi":res[12]==1,
                "pruebas":res[13]==1,
                "calidad2":res[14]==1,
                "documentacion":res[15]==1,
                "acta_entrega":res[16]==1,
                "firma_aceptacion":res[17]==1,
                "facturacion":res[18]==1,
                "soporte":res[19]==1,
                "avance":res[20],
                "estado":self.avance(res)              
            }
           
        except Exception as e:
            data['error'] = str(e)
        return Response(data)
    def avance(self,data):
        date = {
            "recepcion_vehiculo":0,
            "produccion_em":0,
            "equipamiento_vehiculo":0,
            "pruebas_verificacion":0,
            "entrega_vehiculo":0,
            "total_avance":0
        }
        cont = 0
        total = 0
        for i in range(0,len(data),4):
            if cont==0:
                res = sum(data[i:i+4])
                total+=res
                date['recepcion_vehiculo'] = int(res*100/4)
            elif cont==1:
                res = sum(data[i:i+4])
                total+=res
                date['produccion_em'] = int(res*100/4)
            elif cont==2:
                res = sum(data[i:i+4])
                total+=res
                date['equipamiento_vehiculo'] = int(res*100/4)
            elif cont ==3:
                res = sum(data[i:i+4])
                total+=res
                date['pruebas_verificacion'] = int(res*100/4)
            elif cont==4:
                res = sum(data[i:i+4])
                total+=res
                date['entrega_vehiculo'] = int(res*100/4)
            cont+=1

        date['avance_total'] = int(total*100/20)
        return date
      

