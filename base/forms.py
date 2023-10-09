from django.forms import ModelForm
from .models import Room, User
from django.contrib.auth.forms import UserCreationForm

# Here we creating a ModelForm
'''
В Django ModelForm представляет собой удобный способ создания форм, связанных с моделями (models) базы данных. 
Он позволяет автоматически создать форму на основе определенной модели, что сильно упрощает процесс создания, 
валидации и сохранения данных в базу данных.

ModelForm определен в модуле django.forms.models, и для его использования необходимо унаследовать вашу форму 
от ModelForm и указать модель, с которой эта форма должна быть связана. Django самостоятельно сгенерирует поля 
формы, соответствующие полям модели, а также обеспечит валидацию данных на основе определенных ограничений 
модели.
'''

# making form from model, later we will send all info we colect here to make a form for creating rooms


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']


class RoomForm(ModelForm):
    class Meta:  # в формах используется для определения метаданных, связанных с формой, таких как модель, поля, помощники шаблонов и т. д. Это позволяет изменять поведение формы без изменения самих полей формы
        model = Room  # связываем модель с формой
        fields = '__all__'  # указывает, какие поля модели будут включены в форму
        exclude = ['host', 'participants']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'name', 'username', 'email', 'bio']
