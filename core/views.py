from django.http import JsonResponse

def api_home(request):
    endpoints = {
        "Admin": "/admin/",
        "Products API": "/api/products/",
        "Users API": "/api/users/",
        "JWT Token Obtain": "/api/token/",
        "JWT Token Refresh": "/api/token/refresh/",
        "Swagger Docs": "/swagger/",
        "ReDoc Docs": "/redoc/",
    }
    return JsonResponse({
        "message": "Welcome to the E-Commerce Backend API!",
        "available_endpoints": endpoints
    })
