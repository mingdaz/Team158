from django.shortcuts import render

from django.core.urlresolvers import reverse

from django.contrib.auth.decorators import login_required

from django.http import HttpResponse, Http404

from django.db import transaction


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
    return render(request, 'discussion/discussion_board.html', {'username' : request.user.username})


@login_required
def get_posts(request):
    all_posts = Post.objects.all().order_by('-post_time')
    post_replies = []
    for post in posts:
        replies = Reply.objects.filter(post__id = post.id).order_by('post_time')
        context_temp = {'post' : post, 'replies' : replies}
        post_reply.append(context_temp)
    context = {'post_replies' : post_replies}
    return render(request, 'discussion/posts.json', context, content_type = 'application/json')


@login_required
@transaction.atomic
def post_post(request):
    form = PostFormForm(request.POST)
    if not form.is_valid():
        print 'form not valid'
        return render(request, 'grumblr/post.json', {}, content_type='application/json')
    
    new_post = Post(text = form.cleaned_data['text'], \
        post_time = form.cleaned_data['post_time'],\
        author = request.user)
    new_post.save()

    return render(request, 'grumblr/post.json', \
        {'post': new_post}, content_type='application/json')


@login_required
@transaction.atomic
def post_reply(request):
    form = ReplyForm(request.POST)
    if not form.is_valid():
        print 'form not valid!'
        # return render(request, 'grumblr/reply.json', {}, content_type='application/json')
        return render(request, 'grumblr/stream.html', {'form': form})

    to_post = Post.objects.get(id=form.cleaned_data['post_id'])

    new_reply = Reply(text = form.cleaned_data['text'], \
        post_time = form.cleaned_data['post_time'],\
        post = Post.objects.get(id = form.cleaned_data['post_id']),\
        author = request.user)
    new_reply.save()
    
    return render(request, 'grumblr/reply.json', {'reply': new_reply}, content_type='application/json')