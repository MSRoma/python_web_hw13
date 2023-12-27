from django import template

register = template.Library()


# def authors(note_authors):
#     return ', '.join([str(name) for name in note_authors.all()])

def authors(note_authors):
   
    # list_ = []
    # list_.append(note_authors.values_list( "id"))
    # list_.append(note_authors.values_list( "fullname"))
        
    
    # return list_ 
    return ', '.join([str(name) for name in note_authors.all()])


#register.filter('authors', authors)    note_authors.values_list( "id","fullname")
register.filter('authors', authors)


