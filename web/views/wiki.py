from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from utils.cos import upload_file
from utils.encrypt import uid
from web import models
from web.forms.wiki import WikiModelForm
from django.views.decorators.clickjacking import xframe_options_exempt


def wiki(request, project_id):
    """ wiki的首页 """
    wiki_id = request.GET.get('wiki_id')
    if not wiki_id or not wiki_id.isdecimal:
        return render(request, 'web/wiki.html')
    wiki_object = models.Wiki.objects.filter(id=wiki_id, project_id=project_id).first()

    return render(request, 'web/wiki.html', {'wiki_object': wiki_object})


def wiki_add(request, project_id):
    """ wiki添加 """
    if request.method == 'GET':
        form = WikiModelForm(request)
        return render(request, 'web/wiki_add.html', {'form': form})
    form = WikiModelForm(request, data=request.POST)
    if form.is_valid():
        print(1)
        if form.instance.parent:
            form.instance.depth = form.instance.depth + 1
        else:
            form.instance.depth = 1
        form.instance.project = request.tracer.project
        form.save()
        url = reverse('wiki', kwargs={'project_id': project_id})
        return redirect(url)
    return render(request, 'web/wiki_add.html', {'form': form})


def wiki_catalog(request, project_id):
    """ wiki目录 """
    data = models.Wiki.objects.filter(project=request.tracer.project).values("id", 'title', 'parent_id').order_by(
        'depth', 'id')

    return JsonResponse({'status': True, 'data': list(data)})


def wiki_delete(request, project_id, wiki_id):
    """ 删除文章 """
    models.Wiki.objects.filter(project_id=project_id, id=wiki_id).delete()

    url = reverse('wiki', kwargs={'project_id': project_id})
    return redirect(url)


def wiki_edit(request, project_id, wiki_id):
    """ 编辑文章 """
    wiki_object = models.Wiki.objects.filter(project_id=project_id, id=wiki_id).first()
    if not wiki_object:
        url = reverse('wiki', kwargs={'project_id': project_id})
        return redirect(url)
    if request.method == 'GET':
        form = WikiModelForm(request, instance=wiki_object)
        return render(request, 'web/wiki_add.html', {'form': form})
    form = WikiModelForm(request, data=request.POST, instance=wiki_object)
    if form.is_valid():
        if form.instance.parent:
            form.instance.depth = form.instance.depth + 1
        else:
            form.instance.depth = 1
        form.instance.project = request.tracer.project
        form.save()
        url = reverse('wiki', kwargs={'project_id': project_id})
        preview_url = "{0}?wiki_id={1}".format(url, wiki_id)
        return redirect(preview_url)
    return render(request, 'web/wiki_add.html', {'form': form})


@xframe_options_exempt
@csrf_exempt
def wiki_upload(request, project_id):
    result = {
        'success': 0,
        'message': None,
        'url': None
    }

    image_object = request.FILES.get('editormd-image-file')
    if not image_object:
        result['message'] = "文件不存在"
        return JsonResponse(result)

    ext = image_object.name.rsplit('.')[-1]
    key = "{}.{}".format(uid(request.tracer.user.mobile_phone), ext)
    image_url = upload_file(
        request.tracer.project.bucket,
        request.tracer.project.region,
        image_object,
        key
    )
    result['success'] = 1
    result['url'] = image_url
    return JsonResponse(result)
