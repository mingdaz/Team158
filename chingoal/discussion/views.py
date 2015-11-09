from django.shortcuts import render, redirect

from django.core.urlresolvers import reverse

from django.contrib.auth.decorators import login_required

from django.http import HttpResponse, Http404

from django.db import transaction

from forms import *
from models import *


@login_required
# @transaction.atomic
def post_question(request):
    return render(request, 'discussion/discussion_board.html', {})


@login_required
# @transaction.atomic
def reply_question(request):
    return render(request, 'discussion/discussion_reply.html', {})


@login_required
# @transaction.atomic
def delete_post(request):
    return render(request, 'discussion/discussion_board.html', {})


@login_required
def discussion_home(request):
    posts = Post.objects.all().order_by('-post_time')
    post_replies = [];
    for post in posts:
        number_replies = len(Reply.objects.filter(reply_to = post))
        post_replies.append({'post':post, 'number_replies' : number_replies})
    context = {'username' : request.user.username, 'posts' : post_replies}
    return render(request, 'discussion/discussion_board.html', context)


@login_required
def discussion_reply(request, post_id):
    post = Post.objects.get(id = post_id)
    post_user = post.author
    replies = Reply.objects.filter(reply_to__id = post_id)
    max_reply_id = replies.aggregate(Max('id'))['id__max'] or 0
    return render(request, 'discussion/discussion_reply.html', \
        {'post': post, 'replies' : replies, 'post_user': post_user, 'max_reply_id' : max_reply_id,\
            'username' : request.user.username})


@login_required
def get_posts(request):
    all_posts = Post.objects.all().order_by('-post_time')
    post_replies = []
    for post in all_posts:
        replies = Reply.objects.filter(reply_to__id = post.id).order_by('post_time')
        context_temp = {'post' : post, 'replies' : replies}
        post_replies.append(context_temp)
    context = {'post_replies' : post_replies}
    return render(request, 'discussion/posts.json', context, content_type = 'application/json')


@login_required
@transaction.atomic
def post_post(request):
    form = PostFormForm(request.POST)
    if not form.is_valid():
        print 'form not valid'
        return render(request, 'discussion/post.json', {}, content_type='application/json')
    
    new_post = Post(title = form.cleaned_data['title'],\
        text = form.cleaned_data['text'], \
        post_time = form.cleaned_data['post_time'],\
        author = request.user)
    new_post.save()

    return render(request, 'discussion/post.json', \
        {'post': new_post}, content_type='application/json')


@login_required
@transaction.atomic
def post_reply(request):
    form = ReplyForm(request.POST)
    if not form.is_valid():
        print 'form not valid!'
        return render(request, 'discussion/reply.json', content_type='application/json')

    to_post = Post.objects.get(id=form.cleaned_data['post_id'])

    new_reply = Reply(text = form.cleaned_data['text'], \
        post_time = form.cleaned_data['post_time'],\
        reply_to = Post.objects.get(id = form.cleaned_data['post_id']),\
        author = request.user)
    new_reply.save()
    
    return render(request, 'discussion/reply.json', {'reply': new_reply}, content_type='application/json')


@login_required
def get_postreply(request, post_id, max_reply_id):
    replies = Reply.objects.filter(reply_to__id = post_id).filter(id__gt = max_reply_id)
    return render(request, 'discussion/replies.json', {'replies' : replies}, content_type='application/json')


@login_required
@transaction.atomic
def delete_post(request, post_id):
    postTemp = Post.objects.get(id = post_id)
    replies = Reply.objects.filter(reply_to__id = post_id)
    postTemp.delete()
    for reply in replies:
        reply.delete()
    return redirect(reverse('discussion_home'))


@login_required
@transaction.atomic
def delete_reply(request, reply_id):
    print 'in delete reply'
    replyTemp = Reply.objects.get(id = reply_id)
    post_id = replyTemp.reply_to.id
    replyTemp.delete()
    return render(request, 'discussion/reply.json', {}, content_type = 'application/json')
