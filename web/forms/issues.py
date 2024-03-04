# 时间：2022/4/9 15:34
# -*- coding:utf-8 -*-
from django import forms
from utils.bootserapform import BootStrapForm
from web import models


class IssuesModelForm(BootStrapForm, forms.ModelForm):
    class Meta:
        model = models.Issues
        exclude = ['project', 'creator', 'create_datetime', 'latest_update_datetime']
        widgets = {
            "assign": forms.Select(attrs={'class': "selectpicker", "data-live-search": "true"}),
            "attention": forms.SelectMultiple(
                attrs={'class': "selectpicker", "data-live-search": "true", "data-actions-box": "true"}),
            "parent": forms.Select(attrs={'class': "selectpicker", "data-live-search": "true"}),
            "start_date": forms.DateTimeInput(attrs={'autocomplete': "off"}),
            "end_date": forms.DateTimeInput(attrs={'autocomplete': "off"})
        }

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 处理数据初始化

        # 1.获取当前项目的所有问题类型 [(1,'xx'),(2,"xx")]
        self.fields['issues_type'].choices = models.IssuesType.objects.filter(
            project=request.tracer.project).values_list('id', 'title')

        # 2.获取当前项目的所有模块
        model_list = [('', '没有选中任何模块')]
        model_object_list = models.Module.objects.filter(project=request.tracer.project).values_list('id', 'title')
        model_list.extend(model_object_list)

        # 3.指派和关注者
        # 数据库找到当前项目的参与者 和 创建者
        total_list = [(request.tracer.project.creator_id, request.tracer.project.creator.username), ]
        total_object_list = models.ProjectUser.objects.filter(project=request.tracer.project).values_list('user_id',
                                                                                                          'user__username')
        total_list.extend(total_object_list)

        self.fields['assign'].choices = [('', '没有选中任何成员')] + total_list
        self.fields['attention'].choices = total_list

        # 4. 当前项目已创建的问题
        parent_list = [('', '没有选中任何模块')]
        parent_object_list = models.Issues.objects.filter(project=request.tracer.project).values_list('id', 'subject')
        model_list.extend(parent_object_list)
        self.fields['parent'].choices = parent_list


class IssuesReplyModelForm(forms.ModelForm):
    class Meta:
        model = models.IssuesReply
        fields = ['content', 'reply']


class InviteModelForm(BootStrapForm, forms.ModelForm):
    class Meta:
        model = models.ProjectInvite
        fields = ['period', 'count']
