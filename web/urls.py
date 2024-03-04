from django.urls import path, re_path, include
from web.views import account, home, project, dashboard, wiki, file, setting, issues, statistics

urlpatterns = [
    path('', home.index, name='index'),

    # 用户注册及登录
    path('register/', account.register, name='register'),
    path('login/', account.login, name='login'),
    path('login/sms', account.login_sms, name='login_sms'),
    path('logout', account.logout, name='logout'),
    path('send/sms/', account.send_sms, name='send_sms'),
    path('img/code', account.img_code, name='img_code'),

    # 订单管理
    re_path(r'^price/$', home.price, name='price'),
    re_path(r'^payment/(?P<policy_id>\d+)/$', home.payment, name='payment'),
    re_path(r'^pay/$', home.pay, name='pay'),
    re_path(r'^pay/notify/$', home.pay_notify, name='pay_notify'),

    # 项目列表
    path('project/list', project.project_list, name='project_list'),
    re_path(r'^project/star/(?P<project_type>\w+)/(?P<project_id>\d+)$', project.project_star, name='project_star'),
    re_path(r'^project/unstar/(?P<project_type>\w+)/(?P<project_id>\d+)/$', project.project_unstar,
            name='project_unstar'),

    # 项目管理
    re_path(r'^manage/(?P<project_id>\d+)/', include([
        re_path(r'^wiki/$', wiki.wiki, name='wiki'),
        re_path(r'^wiki/add/$', wiki.wiki_add, name='wiki_add'),
        re_path(r'^wiki/catalog/$', wiki.wiki_catalog, name='wiki_catalog'),
        re_path(r'^wiki/delete/(?P<wiki_id>\d+)/$', wiki.wiki_delete, name='wiki_delete'),
        re_path(r'^wiki/edit/(?P<wiki_id>\d+)/$', wiki.wiki_edit, name='wiki_edit'),
        re_path(r'^wiki/upload/$', wiki.wiki_upload, name='wiki_upload'),

        re_path(r'^file/$', file.file, name='file'),
        re_path(r'^file/delete/$', file.file_delete, name='file_delete'),
        re_path(r'^cos/credential/$', file.cos_credential, name='cos_credential'),
        re_path(r'^file/post/$', file.file_post, name='file_post'),
        re_path(r'^file/download/(?P<file_id>\d+)/$', file.file_download, name='file_download'),

        re_path(r'^setting/$', setting.setting, name='setting'),
        re_path(r'^setting/delete/$', setting.delete, name='setting_delete'),

        re_path(r'^issues/$', issues.issues, name='issues'),
        re_path(r'^issues/detail/(?P<issues_id>\d+)/$', issues.issues_detail, name='issues_detail'),
        re_path(r'^issues/record/(?P<issues_id>\d+)/$', issues.issues_record, name='issues_record'),
        re_path(r'^issues/change/(?P<issues_id>\d+)/$', issues.issues_change, name='issues_change'),
        re_path(r'^issues/invite/url/$', issues.invite_url, name='invite_url'),

        re_path(r'^dashboard/$', dashboard.dashboard, name='dashboard'),
        re_path(r'^dashboard/issues/chart/$', dashboard.issues_chart, name='issues_chart'),
        #
        re_path(r'^statistics/$', statistics.statistics, name='statistics'),
        re_path(r'^statistics/priority/$', statistics.statistics_priority, name='statistics_priority'),
        re_path(r'^statistics/project/user/$', statistics.statistics_project_user, name='statistics_project_user'),
    ], )),
    re_path(r'^invite/join/(?P<code>\w+)/$', issues.invite_join, name='invite_join'),

]
