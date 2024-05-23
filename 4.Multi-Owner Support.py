class MultiOwnerAccessControl(AccessControl):
    def _init_(self):
        super()._init_()
        self.owner_permissions = {}  # Dictionary to store owner permissions
    
    def grant_owner_permission(self, owner, resource, permission):
        if owner not in self.owner_permissions:
            self.owner_permissions[owner] = {}
        self.owner_permissions[owner][resource] = permission
    
    def check_owner_permission(self, owner, resource, required_permission):
        if owner in self.owner_permissions and resource in self.owner_permissions[owner]:
            return self.owner_permissions[owner][resource] == required_permission
        return False

# Example usage
multi_owner_access_control = MultiOwnerAccessControl()
multi_owner_access_control.grant_owner_permission("owner1", "file1", "read")
print(multi_owner_access_control.check_owner_permission("owner1", "file1", "read"))  # True