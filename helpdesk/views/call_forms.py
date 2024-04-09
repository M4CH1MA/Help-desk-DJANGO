from django.shortcuts import render, get_object_or_404, redirect
from helpdesk.models import Call
from django import forms
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required

class CallForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({
            'class':'form-control'
        })

        self.fields['category'].widget.attrs.update({
            'class':'form-control'
        })

        self.fields['description'].widget.attrs.update({
            'class':'form-control'
        })

    class Meta:
        model = Call
        fields = 'title', 'category', 'description',
        

# Create your views here.
@login_required(login_url='helpdesk:login')
def create(request):

    form_action = reverse('helpdesk:create')

    

    if request.method == 'POST':
        form = CallForm(request.POST)
        context = {
            'titulo': 'Novo Chamado',
            'form': form,
            'form_action':form_action
        }

        if form.is_valid():
            call = form.save(commit=False)
            call.owner = request.user
            call.save()
            return redirect('helpdesk:update', call_id=call.id)
            

        #return render(request, 'helpdesk/create.html', context)

    context = {
            'titulo': 'Novo Chamado',
            'form': CallForm(),
            'form_action':form_action,
        }

    return render(request, 'helpdesk/create.html', context)

@login_required(login_url='helpdesk:login')
def update(request, call_id):

    call = get_object_or_404(Call, pk=call_id, show=True, owner=request.user)

    form_action = reverse('helpdesk:update', args=(call_id,))

    

    if request.method == 'POST':
        form = CallForm(request.POST, instance=call)
        context = {
            'titulo': 'Editar Chamado',
            'form': form,
            'form_action':form_action,
        }

        if form.is_valid():
            call = form.save()
            #return redirect('helpdesk:update', call_id=call.id)
            return redirect('helpdesk:index')
            

        #return render(request, 'helpdesk/create.html', context)

    context = {
            'titulo': 'Novo Chamado',
            'form': CallForm( instance=call),
            'form_action':form_action,
        }

    return render(request, 'helpdesk/create.html', context)

@login_required(login_url='helpdesk:login')
def delete(request, call_id):

    call = get_object_or_404(Call, pk=call_id, show=True, owner=request.user)

    call.delete()

    return redirect('helpdesk:index')

def finalizar(request, call_id):

    call = get_object_or_404(Call, pk=call_id, show=True)

    call.show = False
    call.save()

    return redirect('helpdesk:index')

class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update({
            'class':'form-control'
        })

        self.fields['last_name'].widget.attrs.update({
            'class':'form-control'
        })

        self.fields['email'].widget.attrs.update({
            'class':'form-control'
        })

        self.fields['username'].widget.attrs.update({
            'class':'form-control'
        })

        self.fields['password1'].widget.attrs.update({
            'class':'form-control'
        })

        self.fields['password2'].widget.attrs.update({
            'class':'form-control'
        })
        

    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'email', 'username', 'password1', 'password2'

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error('email', ValueError('Ja existe esse email', code='invalide') )

        return email
    
class AutenticacaoForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class':'form-control'
        })

        self.fields['password'].widget.attrs.update({
            'class':'form-control'
        })




class RegisterUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['email'].widget.attrs.update({
            'class':'form-control'
        })



    first_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={"class":"form-control"}),
        error_messages={
            'min_length': 'Please, add more than 2 letters.'
        }
    )

    last_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={"class":"form-control"}),
    )

    username = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={"class":"form-control"}),
    )

    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "class":"form-control"}),
        help_text=password_validation.password_validators_help_text_html(),
        required=False,
    )

    password2 = forms.CharField(
        label="Password 2",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "class":"form-control"}),
        help_text='Use the same password as before.',
        required=False,
    )

    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'email', 'username', 

    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        user = super().save(commit=False)
        password = cleaned_data.get('password1')

        if password:
            user.set_password(password)

        if commit:
            user.save()

        return user

    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 or password2:
            if password1 != password2:
                self.add_error(
                    'password2',
                    ValidationError('Senhas não batem')
                )

        return super().clean()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        current_email = self.instance.email

        if current_email != email:
            if User.objects.filter(email=email).exists():
                self.add_error(
                    'email',
                    ValidationError('Já existe este e-mail', code='invalid')
                )

        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if password1:
            try:
                password_validation.validate_password(password1)
            except ValidationError as errors:
                self.add_error(
                    'password1',
                    ValidationError(errors)
                )

        return password1


