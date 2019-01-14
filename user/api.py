from lib.http import render_json
from lib.sms import send_sms


def submit_phone(request):
    '''提交手机号，发送验证码'''
    phone = request.POST.get('phone')
    send_sms(phone)
    return render_json(data)


def submit_vcode(request):
    '''提交短信验证码，登录'''
    return JsonResponse({'code': 0, 'data': None})


def get_profile(request):
    '''获取个人资料'''
    return JsonResponse({'code': 0, 'data': None})


def set_profile(request):
    '''修改个人资料'''
    return


def upload_avatar(request):
    '''头像上传'''
    return
