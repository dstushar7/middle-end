import cx_Oracle
import frontEnd as SI

class OracleOperations:
    def __init__(self, dbCredPath, oracleClientDir) -> None:
        self.dbCredPath = dbCredPath
        self.oracleClientDir = oracleClientDir


    def db_oracle_connect(self):
        oracle_client_dir = self.oracleClientDir
        jsonCred = self.dbCredPath
        
        cx_Oracle.init_oracle_client(
        lib_dir=oracle_client_dir)

        dsn, username, password = SI.take_data_from_json(jsonCred,'dsn','username','password')
        con = cx_Oracle.connect(user=username, password=password,
                                    dsn=dsn,
                                    encoding="UTF-8")
        return con


    def execute_query(con,query):
        cur = con.cursor()
        cur.execute(query)
        con.commit()
        cur.close()

