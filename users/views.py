from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from users.forms import CustomUserCreationForm

# logout 이름이 겹치기 때문에 모듈 이름을 다르게 가져옴
from django.contrib.auth import logout as django_logout
from django.contrib.auth import login as django_login
from users.models import Member

# 만든 loginForm 불러오기
from users.forms import LoginForm
# from users.forms import SignupForm
from users.forms import UserForm

from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password

# 함수 선언
# alert_js ='''
# function new_post() {
#     alert('실패했습니다!');
# }
# '''


# Create your views here.
# 함수명과 장고가 제공해주는 모듈이름이 겹침 주의
# render : templates을 불러옴
# redirect : URL로 이동 => 이동하는 URL에 맞는 view가 다시 실행되고, render할지/redirect할지 결정
def login(request):
    if request.method == 'GET':
        login_form = LoginForm()
        context = {
            "my_form": login_form
        }
        return render(request, 'users/login.html', context)

    elif request.method == 'POST':
        # 사용자가 보낸 request안에 POST 형식으로 보낸 정보가 들어감
        login_form = LoginForm(request.POST)
        username = login_form.data['username']
        password = login_form.data['password']

        # if not (username and password):
        #     messages.warning(request, "모든 값을 입력하세요!")
        # else:
        #     member = Member.objects.get(username=username)
        #     if check_password(password, member.password):
        #         request.session['user'] = member.id

        # 로그인 인증처리
        user = authenticate(username=username,
                            password=password)

        member = Member.objects.get(username=username)

        # 유저 객체가 있다면
        if user is not None:
            django_login(request, user)  # 로그인 처리
            request.session['user'] = member.id
            return redirect('users:test')  # 하고 홈으로 보냄

        # 유저 객체가 없다면
        elif user is None:
            messages.warning(request, "아이디 또는 비밀번호가 일치하지 않습니다. :D")
            return redirect('users:login')
    else:
        return render(request, 'users/login.html')


def logout(request):
    # 장고가 제공해주는 logout기능 사용
    django_logout(request)
    return redirect('home')


def home(request):
    user_id = request.session.get('user')

    if user_id:
        member = Member.objects.get(pk=user_id)
        context = {
            'member': member
        }
        # return HttpResponse(member.nickname)
        return redirect('home')

    return HttpResponse('Home!')


# def login_process(request):
#     # 사용자가 request를 보내는데, 그 방식이 POST 방식이라면
#     if request.method == 'POST':
#         # 사용자가 보낸 request안에 POST 형식으로 보낸 정보가 들어감
#         login_form = LoginForm(request.POST)
#         username = login_form.data['username']
#         password = login_form.data['password']
#
#         # if not (username and password):
#         #     messages.warning(request, "모든 값을 입력하세요!")
#         # else:
#         #     member = Member.objects.get(username=username)
#         #     if check_password(password, member.password):
#         #         request.session['user'] = member.id
#
#         # 로그인 인증처리
#         user = authenticate(username=username,
#                             password=password)
#
#         member = Member.objects.get(username=username)
#
#         # 유저 객체가 있다면
#         if user is not None:
#             django_login(request, user)  # 로그인 처리
#             request.session['user'] = member.id
#             return redirect('users:test')  # 하고 홈으로 보냄
#
#         # 유저 객체가 없다면
#         elif user is None:
#             messages.warning(request, "아이디 또는 비밀번호가 일치하지 않습니다. :D")
#             return redirect('users:login')
#     else:
#         return render(request, 'users/login.html')


# 회원가입
'''
def signup(request):
    form = SignupForm()
    return render(request, 'users/signup.html', {'form': form})
    # if request.method == 'POST':
    #     if request.POST['password1'] == request.POST['password2']:
    #         user = User.objects.create_user(
    #             username=request.POST['username'],
    #             password=request.POST['password1'],
    #             email=request.POST['email'],
    #             profile_img=request.POST['profile_img'])
    #         auth.login(request, user)
    #         return redirect('/')
    #     return render(request, 'users/signup.html')
    # return render(request, 'users/signup.html')
'''

'''
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'users/signup.html', {'form': form})
'''

'''
def signup(request):
    if request.method == 'POST':
        signup_form = CustomUserCreationForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            Member.objects.create(user=user)
            django_login(request, user)
            return redirect('home')
    else:
        signup_form = CustomUserCreationForm()
        context = {
            'form': signup_form
        }
        return render(request, 'users/signup.html', context)
'''

'''
def signup(request):
    if request.method == 'POST':
        signup_form = CustomUserCreationForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            Member.objects.create(user=user)
            django_login(request, user)
            return redirect('home')
    else:
        signup_form = CustomUserCreationForm()
        context = {
            'form': signup_form
        }
        return render(request, 'users/signup.html', context)
'''


def signup(request):
    if request.method == "POST":
        print(request.POST)
        if request.POST['password1'] == request.POST['password2']:
            user = Member.objects.create_user(
                username=request.POST["username"],
                nickname=request.POST["nickname"],
                password=request.POST["password1"],
                image=request.FILES["image"]
            )
            user.save()
        return redirect("users:login")
    return render(request, "users/signup_test.html")


def signup2(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST.get('username')
        nickname = request.POST.get('nickname')
        password = request.POST.get('password1')
        password2 = request.POST.get('password2')
        image = request.FILES.get('image')
        print(password != password2)

        if not (username and nickname and password and password2):
            messages.warning(request, "프로필 사진을 제외한 모든 칸을 채워주세용!")
            return redirect('users:signup')

        elif password != password2:
            messages.warning(request, "비밀번호가 일치하지 않습니다")
            return redirect('users:signup')

        else:
            user = Member.objects.create_user(
                username=username,
                nickname=nickname,
                password=password,
                image=image
            )
            user.save()
        return redirect('users:login')
    return render(request, "users/signup.html")
