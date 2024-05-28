def my_middleware (get_response):

    def middleware(request):

        print ('Before accessing a view''\n')

        response = get_response(request)

        print('\n''After accessing a view''\n')

        return response

    return middleware