import pymysql

pw = ''
def call_content():
    secretjuju_db = pymysql.connect(
        user='root',
        passwd = pw,
        host = 'database.dsm-cms.com',
        db='secret_juju',
        charset='utf8'
    )
    try:
        with secretjuju_db.cursor() as cursor:
            sql = """SELECT id, content FROM news WHERE company_id is NULL
                 """
            cursor.execute(sql)
            content = cursor.fetchall()

            return content
    finally:
        secretjuju_db.close()

def insert_industry(industry):
    secretjuju_db = pymysql.connect(
        user='root',
        passwd = pw,
        host = 'database.dsm-cms.com',
        db='secret_juju',
        charset='utf8'
    )

    try:
        with secretjuju_db.cursor() as cursor:
            sql = """insert ignore into industry(name)
             values (%s)"""
            cursor.execute(sql, industry)
        secretjuju_db.commit()

    finally:
        secretjuju_db.close()

def insert_company(code, name):
    secretjuju_db = pymysql.connect(
        user='root',
        passwd = pw,
        host = 'database.dsm-cms.com',
        db='secret_juju',
        charset='utf8'
    )

    try:
        with secretjuju_db.cursor() as cursor:
            sql = """INSERT IGNORE INTO company (ticker_symbol, name)
                    VALUES (%s, %s)
                    """
            cursor.execute(sql, (code, name))
        secretjuju_db.commit()

    finally:
        secretjuju_db.close()

def insert_positivity(ratio, contents, company_id):
    secretjuju_db = pymysql.connect(
        user='root',
        passwd = pw,
        host = 'database.dsm-cms.com',
        db='secret_juju',
        charset='utf8'
    )

    try:
        with secretjuju_db.cursor() as cursor:
            #             sql = """update news
            #                     SET positivity = %s WHERE content = %s
            #                 """
            sql = """insert into news (content, positivity, company_id)
                        values(%s, %s, %s)
            """
            cursor.execute(sql, (contents, ratio, company_id))
        secretjuju_db.commit()

    finally:
        secretjuju_db.close()

def insert_companyid(code):
    secretjuju_db = pymysql.connect(
        user='root',
        passwd = pw,
        host = 'database.dsm-cms.com',
        db='secret_juju',
        charset='utf8'
    )

    try:
        with secretjuju_db.cursor() as cursor:
            sql = """insert into news (company_id)
                        SELECT id FROM company WHERE ticker_symbol = %s
                """
            #             sql = """update news
            #                     SET company_id = (SELECT id FROM company WHERE ticker_symbol = %s)

            #             """
            cursor.execute(sql, (code))
        secretjuju_db.commit()

    finally:
        secretjuju_db.close()

def insert_company_industry_id(company_id, industry):
    secretjuju_db = pymysql.connect(
        user='root',
        passwd = pw,
        host = 'database.dsm-cms.com',
        db='secret_juju',
        charset='utf8'
    )

    try:
        with secretjuju_db.cursor() as cursor:
            sql = """insert ignore into company_industry_affiliation (company_id, industry_id)
                        values((SELECT id FROM company WHERE ticker_symbol = %s), (SELECT id FROM industry WHERE name = %s))
            """
            cursor.execute(sql, (company_id, industry))
        secretjuju_db.commit()

    finally:
        secretjuju_db.close()

def delete_org_content(idx):
    secretjuju_db = pymysql.connect(
        user='root',
        passwd = pw,
        host = 'database.dsm-cms.com',
        db='secret_juju',
        charset='utf8'
    )

    try:
        with secretjuju_db.cursor() as cursor:
            sql = """DELETE FROM news
                        WHERE id = %s
                """
            cursor.execute(sql, (idx))
        secretjuju_db.commit()

    finally:
        secretjuju_db.close()