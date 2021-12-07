from django.http import HttpResponse
import json

# import pdb; pdb.set_trace()

def ordenar(request):
    number = [int(i) for i in request.GET['numeros'].split(',')]
    numerosOrdenados = sorted(number)
    data={
        'status': 'ok',
        'numeros':numerosOrdenados,
        'message': 'Numeros ordenados'
    }
    return HttpResponse(json.dumps(data),content_type='application/json')


def hola(request,name,age):
    if age < 10:
        message = 'Lo siento {}, no puedes ver la pagina'.format(name)
    else:
        message = 'Hola {}'.format(name)

    return HttpResponse(message)