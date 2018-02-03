'''

Copyright (C) 2017-2018 The Board of Trustees of the Leland Stanford Junior
University.
Copyright (C) 2017-2018 Vanessa Sochat.

This program is free software: you can redistribute it and/or modify it
under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or (at your
option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Affero General Public
License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

'''

from django.conf.urls import url
from shub.settings import (
    DOMAIN_NAME,
    REGISTRY_URI,
    REGISTRY_NAME
)

from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.response import Response
import os
    


##############################################################################
# Registry Metadata
##############################################################################


class Registry(object):
    def __init__(self, **kwargs):
       self.name = REGISTRY_NAME
       self.id = REGISTRY_URI
       self.url = DOMAIN_NAME


class RegistrySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=256)
    id = serializers.CharField(max_length=256)
    url = serializers.CharField(max_length=256)

    def list(self):
        return Registry()
    

class RegistryViewSet(viewsets.ViewSet):
    serializer_class = RegistrySerializer

    def get_object(self):
        return Registry()

    def get(self, request):
        registry = self.get_object()
        serializer = RegistrySerializer(registry)
        return Response(serializer.data)
    


#########################################################################
# urlpatterns
#########################################################################


urlpatterns = [

    url(r'^registry/identity/?$', RegistryViewSet.as_view({'get':'get'})),

]
