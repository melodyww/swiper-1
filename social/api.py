from lib.http import render_json
from social import logics


def get_rcmd_users(request):
    users = logics.rcmd_users(request.user)
    data = [user.to_dict() for user in users]  # 封装要返回的数据
    return render_json(data)


def like(request):
    return render_json(None)


def superlike(request):
    return render_json(None)


def dislike(request):
    return render_json(None)


def rewind(request):
    return render_json(None)


def show_liked_me(request):
    return render_json(None)
