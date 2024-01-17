from django.http import HttpResponse

def saludo(request):
    return HttpResponse("¡Hola!")

def saludo2(request):
    nombre = input('Ingresa tu nombre')
    return HttpResponse(f'Tu nombre es {nombre}')

def nombre(request, nombre, apellido):
    return HttpResponse(f"{nombre}, {apellido}")

def tirar_dados(request):

    import random
    numero = random.randint(1,6)

    if numero == 6:
        return HttpResponse('Felicitaciones obtuviste el numero 6')
    else: 
        return HttpResponse(f'{numero} Vuelve a intentar')