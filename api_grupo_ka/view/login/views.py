from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from api_grupo_ka.conexion import CAQ
from api_grupo_ka.hash import HasPassword
class LoginView(GenericAPIView):
    def post(self,request,*args,**kwargs):
        data = {}
        try:
            datos = request.data
            sql = """SELECT AUX_DOCUM,AUX_RAZON,
                        aux_user_i,
                        aux_pass_i FROM t_auxiliar"""
            params = (datos['documento'],datos['username'],HasPassword().hash(datos['password']))
            result = CAQ.query(sql,params,0)
            if result is None:
                raise Exception ("Documento,nombre de usuario o contraseña incorrecta")
            data = {"razon_social":result[1],"documento":result[0]}
        except Exception as e:
            data['error'] = str(e)
        return Response(data)