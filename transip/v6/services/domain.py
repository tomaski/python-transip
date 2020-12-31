# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 Roald Nefs <info@roaldnefs.com>
#
# This file is part of python-transip.

# python-transip is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# python-transip is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License
# along with python-transip.  If not, see <https://www.gnu.org/licenses/>.

from typing import Optional, Type

from transip.base import ApiService, ApiObject
from transip.mixins import GetMixin, DeleteMixin, ListMixin


class Domain(ApiObject):

    _id_attr: str = "name"

    def contacts(self):
        service = WhoisContactService(self.service.client, parent=self)
        return service.list()


class WhoisContact(ApiObject):

    _id_attr: Optional[str] = None


class DomainService(GetMixin, DeleteMixin, ListMixin, ApiService):

    _path: str = "/domains"
    _obj_cls: Optional[Type[ApiObject]] = Domain

    _resp_list_attr: str = "domains"
    _resp_get_attr: str = "domain"


class WhoisContactService(ListMixin, ApiService):

    _path: str = "/domains/{parent_id}/contacts"
    _obj_cls: Optional[Type[ApiObject]] = WhoisContact

    _resp_list_attr: str = "contacts"
