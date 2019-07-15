import xadmin

from demo.models import *


class UserTestAdmin(object):
    list_display = ['id', 'name', 'age']
    search_fields = ['name', 'age']
    list_filter = ['id']


xadmin.site.register(UserTest, UserTestAdmin)