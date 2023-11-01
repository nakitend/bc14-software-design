"""Singleton pattern ensures that there is only one instance of the class,
 and it provides a global point of access to that instance."""


# class IAMLogger:
#     # The single instance of the class
#     _instance = None

#     def __new__(cls):
#         # If there's no instance, create one
#         if cls._instance is None:
#             # Create a new instance of the class
#             cls._instance = super(IAMLogger, cls).__new__(cls)
#             # Initialize username and password to None
#             cls._instance._username = None
#             cls._instance._password = None
#         # Return the single instance
#         return cls._instance

#     def login(self, username, password):
#         # Set the username and password for the instance
#         self._username = username
#         self._password = password

#     def logout(self):
#         # Log out by setting username and password to None
#         self._username = None
#         self._password = None

#     def get_user_details(self):
#         if self._username is not None and self._password is not None:
#             # Return user details if available
#             return {"username": self._username, "password": self._password}
#         else:
#             # Return an empty dictionary if no user details are available
#             return {}


# # Usage
# user1 = IAMLogger()
# user1.login("senjack", "password")
# user1.logout()
# user2 = IAMLogger()
# user2.login("demetira", "demetira1")

# # Print the user details
# print(user1.get_user_details())  # This will print an empty dictionary
# print(user2.get_user_details())  # This will print user2's details
'''Singleton pattern ensures that there is only one instance of the class,
 and it provides a global point of access to that instance.'''

class IAMLogger:
    _instance = None
    _username = None
    _password = None

    def _init_(self, username, password):
        if IAMLogger._instance is None:
            IAMLogger._username = username
            IAMLogger._password = password
            IAMLogger._instance = self

    @staticmethod
    def login(username, password):
        if IAMLogger._instance is None:
            IAMLogger(username, password)
        return IAMLogger._instance

    @staticmethod
    def logout():
        IAMLogger._instance = None

    @staticmethod
    def get_instance():
        return IAMLogger._instance

    @staticmethod
    def get_user_details():
        if IAMLogger._instance:
            return {
                'username': IAMLogger._username,
                'password': IAMLogger._password
            }
        else:
            return {}

# Usage
user1 = IAMLogger.login('senjack', 'password')
IAMLogger.logout()
user2 = IAMLogger.login('demetira', 'demetira1')

print(IAMLogger.get_user_details())  
print(IAMLogger.get_user_details())