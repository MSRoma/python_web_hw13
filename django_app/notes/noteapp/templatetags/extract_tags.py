from django import template

register = template.Library()


def tags(note_tags):
    list_ = []
    for name in note_tags.all():
        list_.append(name) 
    
    return list_ 
   
   # return ', '.join([str(name) for name in note_tags.all()])


register.filter('tags', tags)
