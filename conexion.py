import pyodbc
import os
from dotenv import load_dotenv
load_dotenv()
class CAQ:

    def connect(self):
        return pyodbc.connect(
            "DRIVER={SQL Server};"
            +
            f"SERVER={os.getenv('HOSTNAME')};"
            +
            f"DATABASE={os.getenv('DATABASE')};"
            +
            f"UID={os.getenv('UID')};"
            +
            f"PWD={os.getenv('PWD')}"
        )
        
    @classmethod
    def query(cls,sql,params,tipe = 1):
        """
        tipe 0 or 1, mode fetchone or fetchall
        """
        instance = cls()
        conn = instance.connect()
        cursor = conn.cursor()
        cursor.execute(sql,params)
        data = []
        try:
            if tipe == 1:
                data = cursor.fetchall()
            elif tipe == 0:
                data = cursor.fetchone()
            else:
                data = None
            conn.close()
        except Exception as e:
            data = None
        return data