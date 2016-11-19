## ModelAdmin


list_display    		顯示表格

list_display_links 	表格連結

list_filter  			查找

list_editable 		更改內容

#### *list_display_links & list_editable 不能同時使用*


## CRUD [wiki_link](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete)
CREATE

RETRIEVE

UPDATE

DELETE

## Template

在**setting.py DIRS : [ ]** 中加入template dir

## shortcut render 

	import get_object_or_404 

## form

### create forms from model

    from django.forms import ModelForm
	from .models import <my_model>
	class <form_name>(ModelForm){
	class Meta:
    	model = <my_model>
	}

##Templates

	{%  extends "<base.html">  %}
	{%  block <name> %}  {% endblock %} 
	{% block.super %} //To inherit parent's template
## Static 

**In urls.py**
 
	from django.conf import settings
	from django.conf.urls.static import static

	
  	if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

**In setting.py**

	STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    #'/var/www/static/',
	]

	STATIC_ROOT = os.path.join(BASE_DIR,"static_cdn")

**mkdir static & static_cdn  in projectdir**

	>>python manage.py collectstatic
	
## 使用linebreaks來接收換行

	{{ value | linebreaks }}

##Making queries [ link](https://docs.djangoproject.com/en/1.10/topics/db/queries/ "link")

## Paginator 分頁也 [link](https://docs.djangoproject.com/en/1.10/topics/pagination/)




 


