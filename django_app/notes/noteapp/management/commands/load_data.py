from itertools import count
from django.core.management.base import BaseCommand
import json
from noteapp.models import Tag, Author, Note
import datetime
from datetime import datetime




    
class Command(BaseCommand):
    def handle(self, *args, **options):

        
        with open('noteapp/management/commands/authors.json', 'rb') as f:
            data = json.load(f)
            
            for el in data:
                born_date_j = datetime.strptime(el.get('born_date'),"%B %d, %Y")
                born_date_j = born_date_j.date()
                author = Author(fullname=el.get('fullname'), born_date=born_date_j,
                                born_location=el.get('born_location'), description=el.get('description'))
                author.save()

        with open('noteapp/management/commands/quotes.json', 'rb') as q:
            data = json.load(q)

            for quote in data:
                tags = []
                
                for tag in quote['tags']:
                    t, *_ = Tag.objects.get_or_create(name=tag)
                    tags.append(t)
                print(quote,tags)
                exist_quote = bool(len(Note.objects.filter(description=quote['quote'])))
                print(exist_quote)
                try:
                    if not exist_quote:
                        a = Author.objects.get(fullname=quote['author'])
                        q = Note.objects.create(
                            description=quote['quote'],
                            author=a
                        )
                        print(a,q)
                        for tag in tags:
                            q.tags.add(tag)
                except:
                    print("err")
        
        # with open('noteapp/management/commands/quotes.json', 'rb') as q:
        #     data = json.load(q)

        #     tags_ = set()
        #     for el in data:  
        #         note = Note(description=el.get('quote'))
        #         note.save()
        #         for i in el.get('tags'):
        #             tag = Tag(name=i)
        #             tags_.add(i)
        #     for l in tags_: 
        #         tag = Tag(name=l)   
        #         tag.save()

        # with open('noteapp/management/commands/quotes.json', 'rb') as q:
        #     data = json.load(q)
        #     count_= 0
        #     for el in data:
        #         try:
        #             count_ += 1
        #             author = el.get("author")
        #             author_id = Author.objects.get(fullname=author)
        #             print( count_, author_id)
        #         except:
        #             print("err")
                #aut = author_id.get(id)
                    #print(quote_id, author_id)
            #     author_to_note = Note(author=el.get('quote'))
            # tags1 = Tag.objects.get(name="music")
            # tags2 = Author.objects.get(fullname="Jane Austen")
          #  Note.objects.get(pk=note_id, user=request.user).delete()
          #  Note.objects.filter(pk=note_id, user=request.user).update(done=True)
            #print(tags1,tags2)
