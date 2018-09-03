# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

from django.conf import settings
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader, Template
from django.views.decorators.csrf import requires_csrf_token, csrf_exempt
from django.template.context_processors import csrf
from django.utils._os import safe_join
from django.utils import timezone



from sql.model.testModel import Post
from django.contrib.auth.models import User
from forms import PostForm, testForm

from sql.mapper import testMapper
from stats.sql.model.testModel import Post


# print settings.TEMPLATES[0]['DIRS'][0]
cureentApp = 'stats/'

def get_page_or_404(name):
    """Return page content as a Django template or raise 404 error."""
    try:
        file_path = safe_join(settings.BASE_DIR+'/templates/', name)
        print 'file_path: ', file_path
    except ValueError:
        raise Http404('Page Not Found')
    else:
        if not os.path.exists(file_path): raise Http404('Page Not Found')

    with open(file_path, 'r') as f:
        page = Template(f.read())

    return page


def index(request, slug='index'):
    file_name = cureentApp + '{}.html'.format(slug)
    page = get_page_or_404(file_name)
    print 'request path : ', request.path
    context = {
        'slug': slug,
        'STATIC_URL' : settings.STATIC_URL
    }
    return render(request, file_name, context)

    # template = loader.get_template(cureentApp + 'index.html')
    # context = {
    #     'con_test' : 'con_test_value',
    #     'STATIC_URL' : settings.STATIC_URL
    # }
    # return HttpResponse(template.render(context), content_type="text/html; charset=UTF-8")

def sub(request):
    template = loader.get_template(cureentApp+'sub.html')
    context = {
        'con_test' : 'con_test_value',
        'STATIC_URL' : settings.STATIC_URL
    }
    return HttpResponse(template.render(context), content_type="text/html; charset=UTF-8")

# ----------------------------   django form test start   -------------------------------------------

def post(request) :
    template = loader.get_template(cureentApp+'post.html')
    # postItem = Post.objects.filter(author_id=1)
    postItem = Post.objects.all()
    context = {
        'STATIC_URL' : settings.STATIC_URL,
        'postList' : postItem
    }
    return HttpResponse(template.render(context), content_type="text/html; charset=UTF-8")

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    template = loader.get_template(cureentApp+'post_detail.html')
    context = {
        'STATIC_URL' : settings.STATIC_URL,
        'post': post
    }
    return HttpResponse(template.render(context), content_type="text/html; charset=UTF-8")

# @csrf_exempt
# def post_new(request) :
#     if request.method == 'POST' :
#         postFormInstance = PostForm(request.POST)
#         if form.is_valid():
#             # 유효성 검사에 통과하면 PostForm의 인스턴스 객체인 postFormInstance에서 save() 메서드 호출
#             # DB에 저장하지 않고 인스턴스만 생성하기 위해 commit=False옵션 지정
#             post = form.save(commit=False)
#             # PostForm에 지정되지 않았으나 필수요소인 author와 published_date 속성을 지정
#             post.author = request.user
#             post.published_date = timezone.now()
#             #DB에 저장
#             post.save()
#             return HttpResponseRedirect("/post/{}/".format(post.pk))
#
#             # """
#             # 저장방법1) - 가장 일반적인 방법
#             # post = Post()
#             # post.title = form.cleaned_data['title']
#             # post.content = form.cleaned_data['content']
#             # post.save()
#             #
#             # 저장방법2)
#             # post = Post(title = form.cleaned_data['title'], content = form.cleaned_data['content'])
#             # post.save()
#             #
#             # 저장방법3)
#             # post = Post.objects.create(title = form.cleaned_data['title'], content = form.cleaned_data['content'])
#             #
#             # 저장방법4)
#             # post = Post.objects.create(**form.cleaned_data) # unpack 을 통해 방법3과 같이 저장
#             # """
#
#         else :
#             # validator 통과 못했으니 에러 메세지 보여주기
#             print 'fail success'
#     else:
#         form = PostForm()
#         template = loader.get_template(cureentApp+'post_edit.html')
#         context = {
#             'STATIC_URL' : settings.STATIC_URL,
#             'form': form,
#         }
#         return HttpResponse(template.render(context), content_type="text/html; charset=UTF-8")

@csrf_exempt
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return HttpResponseRedirect("/post/{}/".format(post.pk))
    else:
        form = PostForm(instance=post)
        template = loader.get_template(cureentApp+'post_edit.html')
        context = {
            'STATIC_URL' : settings.STATIC_URL,
            'form': form
        }
        return HttpResponse(template.render(context), content_type="text/html; charset=UTF-8")

def test_form(request) :
    if request.method == 'POST' :
        form = testForm(request.POST)
        if form.is_valid() :
            # do nothing, just trigger the validation
            pass
    else :
        form = testForm()
        template = loader.get_template(cureentApp+'testForm.html')
        context = {
            'form': form
        }
        return HttpResponse(template.render(context), content_type="text/html; charset=UTF-8")

# def comment_create(request, post_pk):
#     # 요청 메서드가 POST방식 일 때만 처리
#     if request.method == 'POST':
#         # Post인스턴스를 가져오거나 404 Response를 돌려줌
#         post = get_object_or_404(Post, pk=post_pk)
#         # request.POST데이터를 이용한 Bounded Form생성
#         comment_form = CommentForm(request.POST)
#         # 올바른 데이터가 Form인스턴스에 바인딩 되어있는지 유효성 검사
#         if comment_form.is_valid():
#             # 유효성 검사에 통과하면 ModelForm의 save()호출로 인스턴스 생성
#             # DB에 저장하지 않고 인스턴스만 생성하기 위해 commit=False옵션 지정
#             comment = comment_form.save(commit=False)
#             # CommentForm에 지정되지 않았으나 필수요소인 author와 post속성을 지정
#             comment.post = post
#             comment.author = request.user
#             # DB에 저장
#             comment.save()
#
#             # 성공 메시지를 다음 request의 결과로 전달하도록 지정
#             messages.success(request, '댓글이 등록되었습니다')
#         else:
#             # 유효성 검사에 실패한 경우
#             # 에러 목록을 순회하며 에러메시지를 작성, messages의 error레벨로 추가
#             error_msg = '댓글 등록에 실패했습니다\n{}'.format(
#                 '\n'.join(
#                     [f'- {error}'
#                      for key, value in comment_form.errors.items()
#                      for error in value]))
#             messages.error(request, error_msg)
#
#         # comment_form이 valid하건 하지않건
#         # 'post'네임스페이스를 가진 url의 'post_list'이름에 해당하는 뷰로 이동
#         return redirect('post:post_list')

# ----------------------------   django form test end   -------------------------------------------

# ----------------------------   mysql-connector test start   -------------------------------------------
def test_db(request):
    selectList = testMapper.DB_connect('query_with_fetchone')
    print ( 'selectList is : ', selectList )
    context = {
        'STATIC_URL' : settings.STATIC_URL,
        'selectList' : selectList
    }
    template = loader.get_template(cureentApp+'testDB.html')
    return HttpResponse(template.render(context), content_type="text/html; charset=UTF-8")
# ----------------------------   mysql-connector test end   -------------------------------------------


# ----------------------------   django orm test start   -------------------------------------------
def orm_select(request) :
    # test1
    # selectedList = testMapper.DB_connect('post_select_test')

    # test2
    # querySet은 list로 변환 가능
    # selectedList = list(Post.objects.all())
    # print ( type(Post.objects.all()) ) --> <class 'django.db.models.query.QuerySet'> --> list로 type변환 가능

    # test3
    # selectedList = Post.objects.get(title='redirect test')   #return object
    # print ( type(Post.objects.get(title='redirect test')) ) --> <class 'stats.sql.model.testModel.Post'> --> list로 type변환 불가능
    # 아래 접근 가능
    # print(selectedList.id)
    # print(selectedList.title)
    # print(selectedList.text)
    # print(selectedList.created_date)
    # print dir(selectedList)
    # contents = [selectedList.__dict__[key] for key in selectedList.__dict__.iterkeys()]
    # print  contents
    # for key in selectedList.__dict__.iterkeys() :
    #     print 'key is : ' , key , ', and value is : ' , selectedList.__dict__[key]
    #     print selectedList[str(key)] --> 안됨 --> TypeError: 'Post' object has no attribute '__getitem__'

    # test4
    # select using values_list
    # title, text 필드의 값들만 뽑아냄
    # selectedList = list(Post.objects.values_list('title', 'text'))
    # if ( len(selectedList) ) :
    #     for i in range(len(selectedList)) :
    #         print 'title 속성은 : ', selectedList[i][0], ', and text 내용은 : ', selectedList[i][1]

    context = {
        'STATIC_URL' : settings.STATIC_URL,
        'selectedList' : selectedList
    }
    template = loader.get_template(cureentApp+'ormSelect.html')
    return HttpResponse(template.render(context), content_type="text/html; charset=UTF-8")

def orm_filter(request) :
    queryset = Post.objects.all()
    # queryset = Post.objects.all()[:5:10] -> 순서대로 5 ~ 10번까지
    # queryset = Post.objects.all()[:10:2] -> 순서대로 10번까지 2단계 단위로 뽑아냄

    # test1
    # selectedList = queryset.filter(title__icontains='typ').filter(text__contains='con').values()
    selectedList = queryset.filter(title__icontains='typ').filter(text__contains='con').values('title', 'text')
    print selectedList

    # test2
    # print [item.text for item in queryset]
    # print list(item.text for item in queryset)



    context = {
        'STATIC_URL' : settings.STATIC_URL,
        'selectedList' : selectedList
    }
    template = loader.get_template(cureentApp+'ormFilter.html')
    return HttpResponse(template.render(context), content_type="text/html; charset=UTF-8")

