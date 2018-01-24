from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from .forms import *
# Create your views here.


def index(request):
    """ 学习笔记的主页 """
    return render(request, 'learning_logs/index.html')


def topics(request):
    """ 显示所有的主题 """
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    """ 显示单个主题及其所有的条目 """
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


def new_topic(request):
    """添加新主题"""
   # return render(request, 'learning_logs/new_topic.html')
    '''
    
        # 未提交数据：创建一个新表单
        # form = TopicForm()
        return render(request, 'learning_logs/new_topic.html')
    else:
        # POST提交的数据,对数据进行处理
        # form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)
   
    if request.method != 'POST':
        return HttpResponseRedirect('learning_logs/topic.html')
    topic = Topic()
    topic_name = request.POST['topic_name']
    if len(topic_name) > 0 :
        topic.text = topic_name
        topic.save()
        return HttpResponseRedirect('learning_logs/topic.html')
    else:
        return HttpResponse('主题不能为空')
         '''
    if request.method != 'POST':
        # 未提交数据：创建一个新表单
        form = TopicForm()
    else:
        # POST提交的数据,对数据进行处理
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


def new_entry(request,topic_id):
    """在特定的主题中添加新条目"""
    topic1 = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        # 未提交数据,创建一个空表单
        form = EntryForm()
    else:
        # POST提交的数据,对数据进行处理
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic1
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',
                                                    args=[topic_id]))
    context = {'topic': topic1, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


def base(request):
    context = {'index': '首页',
             }
    return render(request, 'learning_logs/base.html', context)
