from django import forms

class LoginForms(forms.Form):
    
    nome_login=forms.CharField(
    # defino o espaço do formulário como Char
    
        label='Nome de Login', 
        required=True, 
        max_length=100,
        # Label, renomeio o titulo do campo para a aplicação. coloco através do required
        # que o preenchimento é obrigatório e o max_length limito a quantidade
        # de caracteres presentes no campo
        
        widget=forms.TextInput(
        # defino o espaço do formulário como Text 
            
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: João Silva',
            }
            # possuo aqui atributos diretamente relacionados ao html a class
            # e o placeholder (Ultilizado como exemplo dentro dos campos)
        )
    )
    
    senha=forms.CharField(
        
        label='Senha', 
        required=True, 
        max_length=70,
        
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a sua senha',
            }
        )
    )
    

class CadastroForms(forms.Form):
    
    nome_cadastro=forms.CharField(
        label='Nome de Cadastro', 
        required=True, 
        max_length=100,
        
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: João Silva',
            }
        )
    )
    
    email=forms.EmailField(
        label='Email',
        required=True,
        max_length=100,
        
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: joaosilva@xpto.com',
            }
        )
    )
    
    senha_1=forms.CharField(
        
        label='Senha', 
        required=True, 
        max_length=70,
        
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a sua senha',
            }
        ),
    )
    
    senha_2=forms.CharField(
    
        label='Confirme a sua senha', 
        required=True, 
        max_length=70,
    
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a sua senha novamente',
            }
        ),
    )

    
    def clean_nome_cadastro(self):
    
        nome = self.cleaned_data.get('nome_cadastro')
        # sel.cleaned_data é o local já preparado pelo Django para armazenar dados
        # processados pelos formulários

        if nome:
    
            nome = nome.strip()
    
            if ' ' in nome:
                raise forms.ValidationError('Espaços não são permitidos nesse campo')
            else:
                return nome

    def clean_senha_2(self):
    
        senha_1 = self.cleaned_data.get('senha_1')
        senha_2 = self.cleaned_data.get('senha_2')

        if senha_1 and senha_2:
    
            if senha_1 != senha_2:
    
                raise forms.ValidationError('Senhas não são iguais')
            else:
                return senha_2