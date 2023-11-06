def getToken(request):
    return request.headers['Authorization'].split()[1]