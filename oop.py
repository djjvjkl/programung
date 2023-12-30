
# OBJECT MEMBER_ONE FOLLOW WHICH CLASS?

# class member:
#     def __init__(self):
#         print ("hello")
# member_one = member()
# print (member_one.__class__)
# =====================================


# INSTANCE ATTRIBUTES
# class member:
#     def __init__(self,name):
#         self.name=name
# member_one = member("ahmed")
# print(member_one.name)
# ======================================


# INSTANCE METHOD
# class member:
#    def __init__(self,name): 
#       self.name=name("ahmed")
#       def nname(self):
#           print  (self.name)



# CLASS ATTRIBUTES
# class member:
#     allowed_names = {"ali"}
#     def __init__ (self,name):
#         self.fname=name
#         def full_name(self):
#             if self.fname in member.allowed_names:
#                 raise ValueError("allowed")
#             else:
#                     print(fname)
# ========================================================= 


# CLASS METHOD
# class member:
#     def _init__(self, x, y):
#         self.x = x
#         self.y = y
        
#         @classmethod
#         def orgin(cls):
#             return cls(0,0)
        
# member1 = member(1,2)
# member2 = member.orgin()
# print (member1.x, member1.y)
# print (member2.x , member2.y)
# ==============================================


# STSATIC METHOD
# class member:
#     @staticmethod
#     def add(x , y):
#         return x + y
# print(member.add(1,2))
# ===========================================


# MAGIC METHOD
# class member:
#     def __init__(self, x, y):
#         self.x= x
#         self.y= y
#         def __add__(self,other):
#             return member(self.x+other.x, self.y+self.other)
# ================================================================
 


# INHERETANCE
# class member:
#     def __init__(self):
#         print("apple")
#     def eat (self):
#         print("banana")
# class member2(member):
#     def __init__(self):
#       member. __init__(self)
#       print("orange")
# member_one = member()
# member_two = member2()
# ==================================



# OVERRIDDING
# class member:
#     def __init__(self):
#         print("ahmed")
#     def eat(self):
#         print("ali")
# class member2(member):
#     def __init__(self):
#         print("ola")
#         def eat(self):
#             print("alaa")
# ========================================
        


# MULTIPLE INHERTANCE
# class member_one:
#     def __init__(self):
#         print("hi")
# class member_two:
#      def __init__(self):
#          print("hello")
# class member_three(member_one,member_two):
#      my_var = x
#      print(x.mro)         
# ==============================================



# MULTILEVEL INHERTANCE
# class member_one:
#     pass
# class member_two:
#     pass
# class member_three:
#     pass
# =============================================





# BOLYMERPHISM
# class member:
#     def do (self):
#         print("a")
# class member_two(member):
# member1=member_two()
#      print(member1.do)
# ============================================




# ENCUPSULATION---------> Public
# class member:
#     def __init__(self,name):
#         self.name=name
# one = member("ali")
# print(one.name) 
# one.name= ("ola")
# print(one.name)   
# ====================================





#ENCUPSULATION---------> Protected
# class member:
#       def __init__(self,name):
#         self._name=name
# one = member("ali")
# print(one._name) 
# ========================================= 


      

#ENCUPSULATION---------> Private
# class member:
#       def __init__(self,name):
#         self.__name=name
# one = member("ali")
# print(one.__name) 
# def say_hello(self):
#     return self.__name
#     one = member("ali")
#     print(one._member__name)
# ========================================    
    
    

    
# GETTER
# class member:
#       def __init__(self,name):
#         self.__name=name
#       def get_name(self):
#           return self.name
# one = member("ahmed")
# print(one.get__name)
# ===========================




# SETTER
# def set_name(self,newname):
#     def.__name = newname
# one.set__name("ali")
# print (one.set__name())
# =============================




















