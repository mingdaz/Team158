from django.shortcuts import render

from django.core.urlresolvers import reverse

from django.contrib.auth.decorators import login_required

from django.http import HttpResponse, Http404


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
    return render(request, 'discussion/discussion_board.html', {})