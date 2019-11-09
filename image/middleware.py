class MyMiddlewareOPTIONS:
    def __init__(self, options_response):
        self.options_response = options_response

    def __call__(self, request):
        response = self.options_response(request)
        response['Access-Control-Allow-Origin'] = "localhost:3000, 84.201.160.117:8000, example.com"
        response['Access-Control-Allow-Methods'] = "GET, POST, OPTIONS, PUT, DELETE"
        response['Access-Control-Allow-Headers'] = "*"
        return response
    
   

class MyMiddlewareGET:
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response['Access-Control-Allow-Origin'] = "localhost:3000, 84.201.160.117:8000, example.com"
        response['Access-Control-Allow-Methods'] = "GET, POST, OPTIONS, PUT, DELETE"
        response['Access-Control-Allow-Headers'] = "*"
        return response