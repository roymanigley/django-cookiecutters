import math

from django.contrib.auth.decorators import login_required, permission_required
from django.db import models
from django.forms import ModelForm, DateInput, DateTimeInput, TimeInput, Textarea
from django.http import HttpRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import path

from {{ cookiecutter.project_slug }}.models import {{ cookiecutter.models.models_list|join(', ', attribute='name')}}



class AbstractFormView(ModelForm):
    class Meta:
        model = None
        fields = '__all__'
        fields_display = fields
        url = None
        view_template_list = 'crud/list.html'
        view_template_new = 'crud/new_edit.html'
        view_template_detail = 'crud/detail.html'
        view_template_edit = 'crud/new_edit.html'
        view_template_delete = 'crud/delete.html'
        auth = True
        permission = True

    @classmethod
    def urls(cls):
        url = cls.Meta.url
        return [
            path(f'{url}', login_required(cls.list_with_permission_check) if cls.Meta.auth else cls.list),
            path(f'{url}new/', login_required(cls.create_with_permission_check) if cls.Meta.auth else cls.create),
            path(f'{url}<int:id>/', login_required(cls.detail_with_permission_check) if cls.Meta.auth else cls.detail),
            path(f'{url}<int:id>/edit/', login_required(cls.edit_with_permission_check) if cls.Meta.auth else cls.edit),
            path(f'{url}<int:id>/delete/', login_required(cls.delete_with_permission_check) if cls.Meta.auth else cls.delete),
        ]

    @classmethod
    def list_with_permission_check(cls, request: HttpRequest):
        if cls.Meta.permission:
            return permission_required(f'{{ cookiecutter.project_slug }}.view_{cls.Meta.model.__name__.lower()}', raise_exception=True)(cls.list)(request)
        else:
            return cls.list(request)

    @classmethod
    def create_with_permission_check(cls, request: HttpRequest):
        if cls.Meta.permission:
            return permission_required(f'{{ cookiecutter.project_slug }}.add_{cls.Meta.model.__name__.lower()}', raise_exception=True)(cls.create)(request)
        else:
            return cls.create(request)

    @classmethod
    def detail_with_permission_check(cls, request: HttpRequest, id: int):
        if cls.Meta.permission:
            return permission_required(f'{{ cookiecutter.project_slug }}.view_{cls.Meta.model.__name__.lower()}', raise_exception=True)(cls.detail)(request, id)
        else:
            return cls.detail(request, id)

    @classmethod
    def edit_with_permission_check(cls, request: HttpRequest, id: int):
        if cls.Meta.permission:
            return permission_required(f'{{ cookiecutter.project_slug }}.change_{cls.Meta.model.__name__.lower()}', raise_exception=True)(cls.edit)(request, id)
        else:
            return cls.edit(request, id)

    @classmethod
    def delete_with_permission_check(cls, request: HttpRequest, id: int):
        if cls.Meta.permission:
            return permission_required(f'{{ cookiecutter.project_slug }}.delete_{cls.Meta.model.__name__.lower()}', raise_exception=True)(cls.delete)(request, id)
        else:
            return cls.delete(request, id)

    @classmethod
    def _get_next(cls, request):
        return request.GET['next'] if 'next' in request.GET and request.GET['next'] != '' else f'/{cls.Meta.url}'

    @classmethod
    def list(cls, request: HttpRequest):
        page = int(request.GET['page'] if 'page' in request.GET else 1)
        size = int(request.GET['size'] if 'size' in request.GET else 10)
        size_total = cls.Meta.model.objects.count()
        pages_total = range(math.ceil(size_total / size))
        index_start = (page - 1) * size
        index_end = index_start + size
        records = cls.Meta.model.objects.all()[index_start: index_end]

        return render(
            request,
            template_name=cls.Meta.view_template_list,
            context={
                'data': records,
                'fields': cls.Meta.fields_display,
                'page_current': page,
                'size': size,
                'pages_total': pages_total,
                'size_total': size_total
            }
        )

    @classmethod
    def detail(cls, request: HttpRequest, id: int):
        record = get_object_or_404(cls.Meta.model, id=id)

        return render(
            request, template_name=cls.Meta.view_template_detail,
            context={
                'data': record,
                'fields': cls.Meta.fields
            }
        )

    @classmethod
    def create(cls, request: HttpRequest):
        if request.method == 'POST':
            form = cls(request.POST, request.FILES)
            if form.is_valid():
                form.save()

                return redirect(cls._get_next(request))

            return render(
                request,
                template_name=cls.Meta.view_template_new,
                context={
                    'form': form,
                    'next': cls._get_next(request),
                    'data': request.POST,
                    'fields': cls.Meta.fields
                }
            )

        form = cls()

        return render(
            request,
            template_name=cls.Meta.view_template_new,
            context={
                'form': form,
                'next': cls._get_next(request),
                'data': {},
                'fields': cls.Meta.fields
            }
        )

    @classmethod
    def edit(cls, request: HttpRequest, id: int):
        record = get_object_or_404(cls.Meta.model, id=id)
        if request.method == 'POST':
            form = cls(request.POST, request.FILES, instance=record)
            if form.is_valid():
                form.save()

                return redirect(cls._get_next(request))

            return render(
                request,
                template_name=cls.Meta.view_template_edit,
                context={
                    'form': form,
                    'next': cls._get_next(request),
                    'data': record,
                    'fields': cls.Meta.fields
                }
            )

        form = cls(instance=record)

        return render(
            request,
            template_name=cls.Meta.view_template_edit,
            context={
                'form': form,
                'next': cls._get_next(request),
                'data': record,
                'fields': cls.Meta.fields
            }
        )

    @classmethod
    def delete(cls, request: HttpRequest, id: int):
        record = get_object_or_404(cls.Meta.model, id=id)
        if request.method == 'POST':
            record.delete()

            return redirect(cls._get_next(request))

        form = cls(instance=record)

        return render(
            request,
            template_name=cls.Meta.view_template_delete,
            context={
                'form': form,
                'next': cls._get_next(request),
                'data': record,
                'fields': cls.Meta.fields
            }
        )

    @staticmethod
    def create_view(
            *,
            model_class,
            model_fields_display=None,
            model_fields_edit=None,
            base_url=None,
            template_list='crud/list.html',
            template_new='crud/new_edit.html',
            template_detail='crud/detail.html',
            template_edit='crud/new_edit.html',
            template_delete='crud/delete.html',
    ) -> type['AbstractFormView']:

        field_names_display = model_fields_display if model_fields_display is not None else list(
            map(lambda f: f.name, filter(lambda f: not f.primary_key, model_class._meta.fields)))

        field_names = model_fields_edit if model_fields_edit is not None else list(
            map(lambda f: f.name, filter(lambda f: not f.primary_key, model_class._meta.fields)))

        base_url = base_url if base_url is not None else f'{model_class.__name__.lower()}/'

        type_widget_map = {}
        for f in model_class._meta.fields:
            if type(f) is models.DateField:
                type_widget_map[f.name] = DateInput(attrs={'type': 'date'})
            if type(f) is models.TimeField:
                type_widget_map[f.name] = TimeInput(attrs={'type': 'time'})
            if type(f) is models.DateTimeField:
                type_widget_map[f.name] = DateTimeInput(attrs={'type': 'datetime-local'})
            if type(f) is models.TextField:
                type_widget_map[f.name] = Textarea(attrs={'class': 'materialize-textarea', 'style': 'min-height: 7em;'})

        class ViewForm(AbstractFormView):

            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                for field in model_class._meta.fields:
                    if field.name in field_names:
                        if not field.blank:
                            self.fields[field.name].label += ' *'

            class Meta:
                model = model_class
                fields = field_names
                fields_display = field_names_display
                url = base_url
                widgets = type_widget_map
                view_template_list = template_list
                view_template_new = template_new
                view_template_detail = template_detail
                view_template_edit = template_edit
                view_template_delete = template_delete
                auth = True
                permission = True

        return ViewForm


def home(request: HttpRequest):
    return render(request, template_name='home.html')

{% for model in cookiecutter.models.models_list %}{{ model.name }}Form = AbstractFormView.create_view(model_class={{ model.name }})
{% endfor %}
