from django.shortcuts import render, redirect

from apps.usuarios.forms import LoginForms, CadastroForms

from django.contrib.auth.models import User

from django.contrib import auth

from django.contrib import messages

def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
        # verfica se o formulário é válido ( campos preenchidos e corretamente preenchidos )
            nome = form['nome_login'].value()
            senha = form['senha'].value()
            # atribui valores a variáveis para facilitar a comparação com o models do prórpi Django

        usuario = auth.authenticate(
            request,
            username=nome,
            password=senha
        )
        # Autentica de acordo com o recebido no formulário preenchido com os dados armazenados no próprio User fornecido pelo django
        
        if usuario is not None:
        # certifica que a autenticação foi um sucesso
        
            auth.login(request, usuario)
            messages.success(request, f'{nome} logado com sucesso!')
            return redirect('index')
            # login autorizado
            
        else:
            messages.error(request, 'Erro ao efetuar login')
            return redirect('login')
            #login não autorizado

    return render(request, 'usuarios/login.html', {'form': form})

def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)

        if form.is_valid():
            nome=form['nome_cadastro'].value()
            email=form['email'].value()
            senha=form['senha_1'].value()

            if User.objects.filter(username=nome).exists():
                messages.error(request, 'Usuário já existente')
                return redirect('cadastro')
            # filtra para saber se o usuário já é existente ultilizando os próprios dados fornecido pelas propriedades do django

            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()
            messages.success(request, 'Cadastro efetuado com sucesso!')
            return redirect('login')
            # nesse caso partimos para a criação desse usuário, na igualamos os dados com os devidos nomes reconhecidos pelo Django
            # Damos um save para guardar as informações, mensagem de sucesso e redirecionamos a página de login

    return render(request, 'usuarios/cadastro.html', {'form': form})

def logout(request):
    
    auth.logout(request)
    # comando já pré definido pelo próprio django

    messages.success(request, 'Logout efetuado com sucesso!')
    return redirect('login')