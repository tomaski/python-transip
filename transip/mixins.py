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

from typing import Optional, List, Type, Dict, Any

from transip import TransIP
from transip.base import ApiObject


class GetMixin:
    """Retrieve an single ApiObject.

    Derived class must define ``_resp_get_attr``.

    ``_resp_get_attr``: The response attribute which contains the object
    """
    client: TransIP
    _obj_cls: Optional[Type[ApiObject]]
    path: str

    _resp_get_attr: Optional[str] = None

    def get(self, id: str, **kwargs) -> Optional[Type[ApiObject]]:
        if self._obj_cls or self.path or self._resp_get_attr:
            obj: Type[ApiObject] = self._obj_cls(  # type: ignore
                self,
                self.client.get(f"{self.path}/{id}")[self._resp_get_attr]
            )
            return obj
        return None


class DeleteMixin:
    """Delete a single ApiObject."""

    client: TransIP
    path: str

    def delete(self, id: str, **kwargs) -> None:
        if self.path:
            self.client.delete(f"{self.path}/{id}")


class ListMixin:
    """Retrieve a list of ApiObjects.

    Derived class must define ``_resp_list_attr``.

    ``_resp_list_attr``: The response attribute which lists all objects
    """
    client: TransIP
    path: str
    _obj_cls: Optional[Type[ApiObject]]

    _resp_list_attr: Optional[str] = None

    def list(self, **kwargs) -> List[Type[ApiObject]]:
        objs: List[Type[ApiObject]] = []
        if self._obj_cls and self.path and self._resp_list_attr:
            for obj in self.client.get(self.path)[self._resp_list_attr]:
                objs.append(self._obj_cls(self, obj))  # type: ignore
        return objs


class CreateMixin:
    """
    Create a new ApiObject.
    """

    client: TransIP
    path: str

    def create(self, data: Optional[Dict[str, Any]]=None, **kwargs):
        if data is None:
            data = {}

        if self.path:
            self.client.post(self.path, json=data)
