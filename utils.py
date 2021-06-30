from classes.StickerClass import StickerClass
from classes.UserClass import UserClass

classNames = {
	'Sticker': StickerClass,
	'User': UserClass
}


def get_obj(className: str, **kwargs):
	pass
	#return object of class with data from database


def new_obj(className: str, **kwargs):
	pass

	#instanstiate obj by for example :
	#	from orm_manager import ORM
	#	obj_data = orm_manager.create(classNames[className], **kwargs)
	#	obj = UserClass(**obj_data)
	#	return obj


def update_obj(className: str, **kwargs):
	pass
	#return updated object of class with data from database


def delete_obj(className: str, **kwargs):
	pass
	#delete data from database