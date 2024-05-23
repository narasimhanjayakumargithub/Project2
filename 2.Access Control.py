class AccessControl:
    def _init_(self):
        self.user_permissions = {}  # Dictionary to store user permissions
    
    def grant_permission(self, user, resource, permission):
        if user not in self.user_permissions:
            self.user_permissions[user] = {}
        self.user_permissions[user][resource] = permission
    
    def check_permission(self, user, resource, required_permission):
        if user in self.user_permissions and resource in self.user_permissions[user]:
            return self.user_permissions[user][resource] == required_permission
        return False

# Example usage
access_control = AccessControl()
access_control.grant_permission("user1", "file1", "read")
access_control.grant_permission("user2", "file1", "write")
print(access_control.check_permission("user1", "file1", "read"))  # True
print(access_control.check_permission("user2", "file1", "read"))  # False