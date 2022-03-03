from django import forms
from users.models import Member
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


# 장고의 ModelForm을 상속 받아서 사용
class LoginForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['username', 'password']

        labels = {
            'username': '사용자이름',
            'password': '비밀번호'
        }

        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '사용자 이름을 입력 하세요'
                }
            ),

            'password': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '비밀번호를 입력 하세요'
                }
            )
        }

#
# class SignupForm(forms.Form):
#     class Meta:
#         model = Member
#         fields = ['username', 'password','nickname']
#
#         labels = {
#             'username': '사용자이름',
#             'password': '비밀번호',
#             'nickname': '닉네임'
#         }
#
#         widgets = {
#             'username': forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': '사용할 아이디를 입력 하세요'
#                 }
#             ),
#
#             'password': forms.PasswordInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': '비밀번호를 입력 하세요'
#                 }
#             ),
#
#             'nickname': forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': '닉네임을 입력하세요'
#                 }
#             )
#         }


    #
    # email = forms.EmailField(
    #     error_messages={'required': "이메일을 입력하세요."},
    #     max_length=64, label="이메일"
    # )
    # password = forms.CharField(
    #     error_messages={'required': "비밀번호를 입력하세요"},
    #     widget=forms.PasswordInput, label="비밀번호"
    # )
    # re_password = forms.CharField(
    #     error_messages={'required': "비밀번호를 입력하세요"},
    #     widget=forms.PasswordInput, label="비밀번호 재입력"
    # )

    #
    # def clean(self):
    #     cleaned_data = super().clean()
    #     email = cleaned_data.get('email')
    #     password = cleaned_data.get('password')
    #     re_password = cleaned_data.get('re_password')
    #
    #     if password and re_password:
    #         if password != re_password:
    #             self.add_error('password', '비밀번호가 서로 다릅니다.')


from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        models = get_user_model()
        fields = UserCreationForm.Meta.fields


class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")

    class Meta(UserCreationForm.Meta):
        model = Member
        fields = ("username", "password1", "password2", "email")
