from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse

# logout 이름이 겹치기 때문에 모듈 이름을 다르게 가져옴
from django.contrib.auth import logout as django_logout
from django.contrib.auth import login as django_login
from users.models import Member

# 만든 loginForm 불러오기
from users.forms import LoginForm


# Create your views here.
# 함수명과 장고가 제공해주는 모듈이름이 겹침 주의
# render : templates을 불러옴
# redirect : URL로 이동 => 이동하는 URL에 맞는 view가 다시 실행되고, render할지/redirect할지 결정
def login(request):
    login_form = LoginForm()
    context = {
        "my_form": login_form
    }
    return render(request, 'users/login.html', context)


def logout(request):
    # 장고가 제공해주는 logout기능 사용
    django_logout(request)
    return redirect('home')


def login_process(request):
    # 사용자가 request를 보내는데, 그 방식이 POST 방식이라면
    if request.method == 'POST':
        # 사용자가 보낸 request안에 POST 형식으로 보낸 정보가 들어감
        login_form = LoginForm(request.POST)
        username = login_form.data['username']
        password = login_form.data['password']

        # 로그인 인증처리
        user = authenticate(username=username,
                            password=password)

        # 유저 객체가 있다면
        if user is not None:
            django_login(request, user)  # 로그인 처리
            return redirect('home')  # 하고 홈으로 보냄

        # 유저 객체가 없다면
        elif user is None:
            messages.warning(request, "아이디 또는 비밀번호가 일치하지 않습니다. :D")
            return redirect('users:login')
    else:
        return render(request, 'users/login.html')


# 회원가입
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
'''


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


def do_duplicate_check(request):
    print('아이디 중복 체크')
    username = request.GET.get('username')
    try:
        # 중복 검사 실패
        user_id = Member.objects.get(username=username)

    except:
        # 중복 검사 성공
        user_id = None
    if user_id is None:
        duplicate = "pass"
    else:
        duplicate = "fail"
    context = {'duplicate': duplicate}
    return JsonResponse(context)
