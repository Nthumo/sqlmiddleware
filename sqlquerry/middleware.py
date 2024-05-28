from django.db import connection
from sqlparse import format
from django.conf import settings
from decimal import Decimal

def my_middleware (get_response):

    def middleware(request):

        response = get_response(request)

        if settings.DEBUG:
            check_duplicates = set()
            num_queries = len(connection.queries)
            total_execution_time = Decimal()

            for query in connection.queries:
                check_duplicates.add(query["sql"])
                total_execution_time += Decimal(query["time"])

                sqlformatted = format(str(query["sql"]), reindent = True)
                print(sqlformatted)

        print("[SQL STATS]")
        print("=========="'\n')
        print(f"{num_queries} Total Queries")
        print(f"{num_queries - len(check_duplicates)} Duplicates")
        print(f"{total_execution_time}", 'Execution Time')
        print('\n'"==========")

        '''q = list(connection.queries)
        for qs in q:
            sqlformatted = format(str(qs["sql"]), reindent = True)  
            print(sqlformatted)'''
        return response

    return middleware