
# Role-Based Access Control (RBAC) System


## Installation

```bash
git clone https://github.com/jay-arora31/RBACCommandLine
cd RBACCommandLine
```

## Usage

To start the RBAC CLI, run the following command:

```
python3 RBAC_CLI.py
```
## Available Commands


### Access Types
* `addAccess <ACCESS_TYPE>`
   * Adds a global access type (READ or WRITE)
   * Example: `addAccess READ`

### Resources
* `addResource <RESOURCE_NAME>`
   * Adds a new resource
   * Example: `addResource IMAGE`

### Resource Access
* `addAccessOnResource <ACCESS_TYPE> <RESOURCE_NAME>`
   * Adds access (READ/WRITE) to a resource
   * Example: `addAccessOnResource READ IMAGE`

### Roles
* `addRole <ROLE_NAME>`
   * Creates a new role
   * Example: `addRole ADMIN`

* `addAccessOnResourceToRole <ACCESS_TYPE> <RESOURCE_NAME> <ROLE_NAME>`
   * Assigns access to a role for a specific resource
   * Example: `addAccessOnResourceToRole READ IMAGE ADMIN`

### Users
* `addUser <USER_NAME>`
   * Creates a new user
   * Example: `addUser ADMINUSER`

* `addRoleToUser <ROLE_NAME> <USER_NAME>`
   * Assigns a role to a user
   * Example: `addRoleToUser ADMIN ADMINUSER`

### Access Verification
* `checkAccess <USER_NAME> <RESOURCE_NAME> <ACCESS_TYPE>`
   * Checks if a user has a specific type of access to a resource
   * Example: `checkAccess ADMINUSER IMAGE READ`
 

## Output
![image](https://github.com/user-attachments/assets/e0c2c6af-a0e6-418d-b12d-b9d3e85f962f)

