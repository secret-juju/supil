import pymysql

def call_content():
    secretjuju_db = pymysql.connect(
        user='root',
        passwd = '',
        host = 'database.dsm-cms.com',
        db='secret_juju',
        charset='utf8'
    )
    cursor = secretjuju_db.cursor()

    cursor.execute("SELECT content FROM news")
    content = cursor.fetchall()

    return content

def insert_industry(industry):
    secretjuju_db = pymysql.connect(
        user='root',
        passwd = '',
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
        passwd = '',
        host = 'database.dsm-cms.com',
        db='secret_juju',
        charset='utf8'
    )

    try:
        with secretjuju_db.cursor() as cursor:
            #             sql = """INSERT INTO company (ticker_symbol, name)
            #                      VALUES (%s, %s)
            #                      WHERE NOT EXISTS(SELECT ticker_symbol, name FROM company WHERE ticker_symbol = %s AND company = %s)
            #                      """

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
        passwd = '',
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
        passwd = '',
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
        passwd = '',
        host = 'database.dsm-cms.com',
        db='secret_juju',
        charset='utf8'
    )

    try:
        with secretjuju_db.cursor() as cursor:
            #             sql = """update news
            #                     SET positivity = %s WHERE content = %s
            #                 """
            sql = """insert into company_industry_affiliation (company_id, industry_id)
                        values((SELECT id FROM company WHERE ticker_symbol = %s), (SELECT id FROM industry WHERE name = %s))
            """
            cursor.execute(sql, (company_id, industry))
        secretjuju_db.commit()

    finally:
        secretjuju_db.close()