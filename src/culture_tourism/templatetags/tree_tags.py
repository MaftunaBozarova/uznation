from django import template
from culture_tourism.models import Menyu
register = template.Library()


def tree_show():
    return Menyu.get_root_nodes()

register.assignment_tag(tree_show)
