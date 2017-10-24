class User:

    def __init__(self, id=0, name='', username='', email='', password=''):
        self.id = id
        self.name = name
        self.username = username
        self.email = email
        self.password = password


    # def __init__(self,username,password):
    #     self.username = username
    #     self.password = password
        

class RecipeListItem:

    def __init__(self,id,name,description,category,user):
        self.id = id
        self.name = name
        self.description = description
        self.category = category
        self.user = user
        


class Category:
    def __init__(self, id, name, description,user):
        self.id = id
        self.name = name
        self.description = description
        self.user = user
