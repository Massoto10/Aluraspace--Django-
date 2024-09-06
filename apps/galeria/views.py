from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from apps.galeria.models import Fotografia
from apps.galeria.forms import FotografiaForms

# As páginas de Views respondem os requisitos das páginas de urls

def index(request):
    if not request.user.is_authenticated:
    # Faz requisição aos usuários que não estão atenticados ( sem login )
        
        messages.error(request, 'Usuário não logado')
        return redirect('login')
        # redirect = redireciona
        
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    # Puxo do meu models, as fotografias assim cadastradas, ordeno pela data_fotografia, também detalhada
    # no models e aplico o filtro quanto o bool plublicada, também consta no models
    
    return render(request, 'galeria/index.html', {"cards": fotografias})
    # eu retorno dentro dos cards ( classe do meu index.html ) os dados que minha variável "fotografias"
    # consultou no models

def imagem(request, foto_id):
# nesse caso o request, faz com que o id da foto seja puxado da url, que puxa a mesma informação do models

    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    # get_object_or_404: caso objeto não seja encontrado, retorna um 404
    
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

def buscar(request):
    
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')

    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)

    if "buscar" in request.GET:
    # verifica se tem alguma busca na requisição
    
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)
            # se tiver o nomne da requisição dentre as fotografias, filtra e rtorna os valores compativeis
            
    # aqui existe uma requisição do nome buscar na url e buscar a algo
    # logo se tiver um nome a buscar dentro das fotografias mostradas será estipulado um filtro com o nome a buscar
    # e serão mostrado apenas as imagens que tenham esse nome citado em seu título

    return render(request, "galeria/index.html", {"cards": fotografias})
    # aqui retorna de forma precisa dentro do meu index.html os cards que consta as minhas fotografias já ordenadas
    # pela data e, se tiver filtro de busca, já com o mesmo aplicado

def nova_imagem(request):
    
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')

    form = FotografiaForms
    # puxa o formulário do forms
    
    if request.method == 'POST':
        # verifica se é do método POST no qual é usado em requisição de HTTP para enviar dados
        # usado nesse caso por se tratar de uma grande quantidade de dados
        
        form = FotografiaForms(request.POST, request.FILES)
        # o formulário aqui puxou tanto as informações textuais trazidas pelo POST quanto a imagem
        # trazida pelo FILES
        
        if form.is_valid():
        # se realmente for válido e sem erros
        
            form.save()
            messages.success(request, 'Nova fotografia cadastrada!')
            return redirect('index')
            # salvamos, comunicamos e redirecionamos ao index

    return render(request, 'galeria/nova_imagem.html', {'form': form})
    # caso desvincule dos IF's retornaremos para a página de nova imagem e será refeito o preenchimento

def editar_imagem(request, foto_id):
    
    fotografia = Fotografia.objects.get(id=foto_id)
    # estipulo aqui uma busca feito no meu dicionário Fotografia onde 
    # minha chave é o ID e o meu valor está incluso como foto_id
    
    form = FotografiaForms(instance=fotografia)
    # o instance facilita eu carregar dados já existentes para a edição
    

    if request.method == 'POST':
        # para segurança para o programa não quebrar, se faz o filtro para verificar
        # se a imagem é elegivel e se possui informações a serem editadas
        
        form = FotografiaForms(request.POST, request.FILES, instance=fotografia)
        # remodelo o meu forma fazendo novos requests tanto da escrita quanto do arquivo de imagem
        
        if form.is_valid():
        # Confirmo e valido as novas informações
        
            form.save()
            messages.success(request, 'Fotografia editada com sucesso!')
            return redirect('index')
            # salvo, envio a mensagem de concluído e redireciono

    return render(request, 'galeria/editar_imagem.html', {'form': form, 'foto_id': foto_id})

def deletar_imagem(request, foto_id):
    
    fotografia = Fotografia.objects.get(id=foto_id)
    fotografia.delete()
    # com esse simples comando eu delero a imagem desejada
    
    messages.success(request, 'Deleção feita com sucesso!')
    return redirect('index')

def filtro(request, categoria):
    
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True, categoria=categoria)
    # quando aplicado o filtro no site em si, de acordo com as categorias, certificamos que a imagem 
    # esteja publicada e seleciona a categoria desejada 

    return render(request, 'galeria/index.html', {"cards": fotografias})