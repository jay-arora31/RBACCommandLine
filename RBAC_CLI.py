from enum import Enum
from typing import Dict, Set, Optional

class AccessType(Enum):
    READ = "READ"
    WRITE = "WRITE"

class Resource:
    def __init__(self, name: str):
        self.name = name
        self.allowed_access: Set[AccessType] = set()

class Role:
    def __init__(self, name: str):
        self.name = name
        self.access_mapping: Dict[str, Set[AccessType]] = {}

class User:
    def __init__(self, name: str):
        self.name = name
        self.roles: Set[str] = set()

class RBACSystem:
    def __init__(self):
        self.access_types: Set[AccessType] = set()
        self.resources: Dict[str, Resource] = {}
        self.roles: Dict[str, Role] = {}
        self.users: Dict[str, User] = {}

    def add_access(self, access_type: str) -> None:
        try:
            self.access_types.add(AccessType(access_type))
            print(f"Added access type: {access_type}")
        except ValueError:
            print(f"Invalid access type: {access_type}")

    def add_resource(self, resource_name: str) -> None:
        if resource_name not in self.resources:
            self.resources[resource_name] = Resource(resource_name)
            print(f"Added resource: {resource_name}")
        else:
            print(f"Resource already exists: {resource_name}")

    def add_access_on_resource(self, access_type: str, resource_name: str) -> None:
        try:
            access = AccessType(access_type)
            if resource_name in self.resources and access in self.access_types:
                self.resources[resource_name].allowed_access.add(access)
                print(f"Added {access_type} access to resource: {resource_name}")
            else:
                print("Resource or access type not found")
        except ValueError:
            print(f"Invalid access type: {access_type}")

    def add_role(self, role_name: str) -> None:
        if role_name not in self.roles:
            self.roles[role_name] = Role(role_name)
            print(f"Added role: {role_name}")
        else:
            print(f"Role already exists: {role_name}")

    def add_access_on_resource_to_role(self, access_type: str, resource_name: str, role_name: str) -> None:
        try:
            access = AccessType(access_type)
            if (role_name in self.roles and 
                resource_name in self.resources and 
                access in self.access_types):
                
                if resource_name not in self.roles[role_name].access_mapping:
                    self.roles[role_name].access_mapping[resource_name] = set()
                self.roles[role_name].access_mapping[resource_name].add(access)
                print(f"Added {access_type} access on {resource_name} to role: {role_name}")
            else:
                print("Role, resource, or access type not found")
        except ValueError:
            print(f"Invalid access type: {access_type}")

    def add_user(self, user_name: str) -> None:
        if user_name not in self.users:
            self.users[user_name] = User(user_name)
            print(f"Added user: {user_name}")
        else:
            print(f"User already exists: {user_name}")

    def add_role_to_user(self, role_name: str, user_name: str) -> None:
        if role_name in self.roles and user_name in self.users:
            self.users[user_name].roles.add(role_name)
            print(f"Added role {role_name} to user: {user_name}")
        else:
            print("Role or user not found")

    def check_access(self, user_name: str, resource_name: str, access_type: str) -> bool:
        try:
            access = AccessType(access_type)
            
            if (user_name not in self.users or 
                resource_name not in self.resources or 
                access not in self.access_types):
                return False

            if access not in self.resources[resource_name].allowed_access:
                return False

            user = self.users[user_name]
            for role_name in user.roles:
                role = self.roles[role_name]
                if (resource_name in role.access_mapping and 
                    access in role.access_mapping[resource_name]):
                    return True

            return False
        except ValueError:
            return False

class RBACCommandLine:
    def __init__(self):
        self.rbac = RBACSystem()

    def execute_command(self, command: str) -> Optional[str]:
        parts = command.strip().split()
        
        if not parts:
            return None

        command_type = parts[0]

        try:
            if command_type == "addAccess" and len(parts) == 2:
                self.rbac.add_access(parts[1])
            
            elif command_type == "addResource" and len(parts) == 2:
                self.rbac.add_resource(parts[1])
            
            elif command_type == "addAccessOnResource" and len(parts) == 3:
                self.rbac.add_access_on_resource(parts[1], parts[2])
            
            elif command_type == "addRole" and len(parts) == 2:
                self.rbac.add_role(parts[1])
            
            elif command_type == "addAccessOnResourceToRole" and len(parts) == 4:
                self.rbac.add_access_on_resource_to_role(parts[1], parts[2], parts[3])
            
            elif command_type == "addUser" and len(parts) == 2:
                self.rbac.add_user(parts[1])
            
            elif command_type == "addRoleToUser" and len(parts) == 3:
                self.rbac.add_role_to_user(parts[1], parts[2])
            
            elif command_type == "checkAccess" and len(parts) == 4:
                return "Yes" if self.rbac.check_access(parts[1], parts[2], parts[3]) else "No"
            
            else:
                print("Invalid command or wrong number of arguments")
                
        except Exception as e:
            print(f"Error executing command: {str(e)}")
            
        return None
    
def main():
    cli = RBACCommandLine()
    print("RBAC CLI Application")
    print("Type 'exit' to quit")
    print("Available commands:")
    print("  addAccess <ACCESS_TYPE>")
    print("  addResource <RESOURCE_NAME>")
    print("  addAccessOnResource <ACCESS_TYPE> <RESOURCE_NAME>")
    print("  addRole <ROLE_NAME>")
    print("  addAccessOnResourceToRole <ACCESS_TYPE> <RESOURCE_NAME> <ROLE_NAME>")
    print("  addUser <USER_NAME>")
    print("  addRoleToUser <ROLE_NAME> <USER_NAME>")
    print("  checkAccess <USER_NAME> <RESOURCE_NAME> <ACCESS_TYPE>")
    
    while True:
        try:
            command = input("rbac> ").strip()
            if command.lower() == 'exit':
                break
            if not command:
                continue
                
            result = cli.execute_command(command)
            if result is not None:
                print(result)
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()