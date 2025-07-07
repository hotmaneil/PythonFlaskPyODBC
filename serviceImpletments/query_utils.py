from typing import Type, List, Any
from dataclasses import fields

def query(conn, sql: str, model: Type[Any], params: tuple = ()) -> List[Any]:
    '''工具函式-SQL查詢'''
    cursor = conn.cursor()
    cursor.execute(sql, params)
    col_names = [desc[0] for desc in cursor.description]
    results = []
    for row in cursor.fetchall():
        data = dict(zip(col_names, row))
        model_fields = {f.name for f in fields(model)}
        filtered_data = {k: v for k, v in data.items() if k in model_fields}
        results.append(model(**filtered_data))
    return results

def insertRecord(conn, table, data: dict):
    '''工具函式-SQL新增資料'''
    columns = ', '.join(data.keys())
    placeholders = ', '.join(['?' for _ in data])
    values = list(data.values())

    sql = f"INSERT INTO [{table}] ({columns}) VALUES ({placeholders})"
    cursor = conn.cursor()
    cursor.execute(sql, values)
    conn.commit()

