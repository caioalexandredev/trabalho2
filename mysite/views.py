from django.http import JsonResponse
from .services import GalileuAPIService
from .services import WordFileGenerator
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

def procedimento_pericial(request, id):
    if request.method == 'GET':
        service = GalileuAPIService()
        response_data = service.get_procedimento_pericial(id)

        if 'error' in response_data:
            return JsonResponse({'status': 'error', 'message': response_data['error']}, status=500)
        
        return JsonResponse({'status': 'success', 'data': response_data})
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    
def gerar_arquivo_word_teste(request):
    
    data = {
        'title': 'Laudo Exemplo',
        'sections': {
            'Seção 1': 'Texto da seção 1.',
            'Seção 2': 'Texto da seção 2.',
        },
    }

    file_buffer = WordFileGenerator.generate_word_file_test(data)

    response = HttpResponse(
        file_buffer,
        content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    )
    response['Content-Disposition'] = 'attachment; filename="relatorio.docx"'

    return response

def minha_pagina(request):
    return render(request, 'modelo.html')

from django.shortcuts import render, redirect
from django.contrib import messages

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == 'admin' and password == '123':
            request.session['logged_in'] = True
            request.session['login'] = request.POST.get('username')
            return redirect('/')
        else:
            messages.error(request, "Usuário ou senha incorretos.")

    return render(request, 'login.html')
