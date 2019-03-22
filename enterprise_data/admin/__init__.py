# -*- coding: utf-8 -*-
"""
Django admin integration for enterprise-data.
"""
from __future__ import absolute_import, unicode_literals

from edx_rbac.admin import UserRoleAssignmentAdmin, UserRoleAssignmentAdminForm

from django.contrib import admin

from enterprise_data.models import EnterpriseDataRoleAssignment


class EnterpriseDataRoleAssignmentAdminForm(UserRoleAssignmentAdminForm):
    """
    Djaong admin form for EnterpriseDataRoleAssignmentAdmin.
    """

    class Meta:
        """
        Meta class for EnterpriseDataRoleAssignmentAdminForm.
        """
        model = EnterpriseDataRoleAssignment
        fields = ('user', 'role')


@admin.register(EnterpriseDataRoleAssignment)
class EnterpriseDataRoleAssignmentAdmin(UserRoleAssignmentAdmin):
    """
    Django admin for EnterpriseDataRoleAssignment Model.
    """

    class Meta(object):
        """
        Meta class for EnterpriseDataRoleAssignmentAdmin.
        """
        model = EnterpriseDataRoleAssignment

    form = EnterpriseDataRoleAssignmentAdminForm
