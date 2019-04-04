from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from rest_framework import viewsets, status
from rest_framework.decorators import detail_route, action
from rest_framework.response import Response

from shortener.models import Shortcut
from shortener.serializers import ShortcutSerializer, ShortcutSerializerShort


def home(request):
    '''
        Home page, the only template used
    :param request:
    :return:
    '''
    return render(request, 'shortener/shortcut_form.html')


class ShortcutViewSet(viewsets.ModelViewSet):
    """
        Api endpoint that allows shortcut to be view or created
    """
    queryset = Shortcut.objects.all()
    serializer_class = ShortcutSerializer

    def get_serializer_class(self):
        # Change serializer if it's PUT method
        # Firstly we send POST request from Angular JS to create object
        # then we use PUT method to set `short` attribute
        serializer_class = self.serializer_class

        if self.request.method == 'PUT':
            serializer_class = ShortcutSerializerShort
        return serializer_class

    @action(detail=False, methods=['post'])
    def check_shorts(self, request, **kwargs):
        url = request.data['url']

        try:
            obj = Shortcut.objects.get(url=url)
            serializer = self.serializer_class(obj)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)


def pass_trough(request, id):
    '''
        Main function, redirects from shortcut to the original url

    :param request:
    :param id:
    :return:
    '''
    object = get_object_or_404(Shortcut, id=id)
    return redirect(object.url)
