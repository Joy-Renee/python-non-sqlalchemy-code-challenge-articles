class Article:
    article_list = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self._title = title
        Article.article_list.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
      if hasattr(self, "title"):
            AttributeError("Title cannot be changed")
      else:
          if isinstance(new_title, str):
              if 5 <= len(new_title) <= 50:
                    self.title = new_title
              else:
                    ValueError("Titles must be between 5 and 50 characters")
          else:
                TypeError("Title must be of type str")

        
class Author:
    def __init__(self, name):

        self._name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if hasattr(self, "name"):
            AttributeError("Name cannot be changed")
        else:
            if isinstance(new_name, str):
                if len(new_name):
                    self.name = new_name
                else:
                    ValueError("Names must be longer than 0 characters")
            else:
                TypeError("Names must be of type str")


    def articles(self):
       return [article for article in Article.article_list if self == article.author]

    def magazines(self):
         return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
       pass

    def topic_areas(self):
        pass

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass



