import pdb
from models.member import Member
from models.fit_class import Fit_class

import repositories.member_repository as member_repository
import repositories.fit_class_repository as fit_class_repository

#Test save functions
member1 = Member("White", "Goodman", "01/01/1975", "Mr", "he/him", "Loves milk")
member_repository.save(member1)

fit_class1 = Fit_class("Dodgeball", "Sport", "Patches", "03/12/2021", "12:00", "Gym hall")
fit_class_repository.save(fit_class1)