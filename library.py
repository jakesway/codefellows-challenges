#(1) Use object-oriented Python to model a public library (w/ three classes: Library, Shelf, & Book). 
#The library should be aware of a number of shelves. Each shelf should know what books it contains. 
#Make the book object have "enshelf" and "unshelf" methods that control what shelf the book is sitting on. 
#The library should have a method to report all books it contains.

class book(object):  

	def __init__(self, title, author):
		(book, self).__init__()
		self.title = title
		self.author = author
		self.shelf_number = None

	def enshelf(self, shelf_number):
		self.shelf_number = shelf_number
		SPL.shelves[self.shelf_number].books[self] = self
	
	def unshelf(self):	
		del SPL.shelves[self.shelf_number].books[self]
		return self

	def get_title(self):
		return self.title

	def get_author(self):
		return self.author

class shelf(object):
	
	def __init__(self):
		(shelf, self).__init__()
		self.books = {}
		
	def get_books(self):
		temp_list = []

		for k in self.books.keys():
			temp_list.append(self.books[k].get_title())
		return temp_list

class library(object):

	def __init__(self, name):
		(library, self).__init__()
		self.name = name
		self.shelves = []

	def make_shelf(self):
		temp = shelf()
		self.shelves.append(temp)

	def remove_shelf(shelf_number):
		del shelves[shelf_number]

	def report_all_books(self):

		temp_list = []

		for x in range(0,len(self.shelves)):
			temp_list.append(self.shelves[x].get_books())

		print(temp_list)

#---------------------------------------------------------------------------------------
#----------------------SEATTLE PUBLIC LIBARARY -----------------------------------------
#---------------------------------------------------------------------------------------

SPL = library("Seattle Public Library")						

for x in range(0,3):
	SPL.make_shelf()

b1 = book("matterhorn","karl marlantes")
b2 = book("my life","bill clinton")
b3 = book("decision points","george bush")

b1.enshelf(0)
b2.enshelf(1)
b3.enshelf(2)

print(SPL.report_all_books())

b1.unshelf()
b2.unshelf()
b3.unshelf()
