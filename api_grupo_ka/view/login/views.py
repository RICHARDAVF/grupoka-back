from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from api_grupo_ka.conexion import CAQ
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
class LoginView(GenericAPIView):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    def post(self,request,*args,**kwargs):
        data = {}
        try:
            datos = request.data
  
            sql = """SELECT 
                        AUX_DOCUM,
                        AUX_RAZON,
                        aux_clave,
                        aux_user_i,
                        aux_pass_i,aux_clave 
                    FROM t_auxiliar
                    WHERE   
                        aux_user_i = ?
                        AND aux_pass_i = ?
                        AND aux_docum=?
                        AND MAA_CODIGO='CL'
                        """
            params = (datos['username'],datos['password'],datos['documento'])
            result = CAQ.query(sql,params,0)
       
            if result is None:
                raise Exception ("Documento,nombre de usuario o contraseña incorrecta")
            data = {"razon_social":result[1].strip(),"documento":result[0].strip(),"codigo":result[2].strip(),"password":result[4].strip(),"username":result[3].strip()}
    
        except Exception as e:
            data['error'] = str(e)
        return Response(data)