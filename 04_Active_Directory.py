# In Windows Active Directory, a group can consist of user(s) and group(s).
# User is represented by str representing their ids.

class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name



# Write a function that provides an efficient look up of whether the user is in a group.
# Return True if user is in the group, False otherwise.
def is_user_in_group(user, group): 
    if group == "" or group is None or user == "" or user is None:
        return False

    group_users = group.get_users()
    if user in group_users:
        return True
    else: 
        sub_groups = group.get_groups()
        for sub_group in sub_groups:
            is_user_in_group(user, sub_group)
    return False


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

# TEST

print("Expected to be True: ", is_user_in_group(sub_child_user, sub_child))
# True
print("Expected to be True: ", is_user_in_group('parent_user', parent))
# False
print("Expected to be False: ", is_user_in_group(sub_child_user, child))
# False
print("Expected to be False: ", is_user_in_group(sub_child_user, parent))
# False
print("Expected to be False: ", is_user_in_group(sub_child_user, None))
# False
print("Expected to be False: ", is_user_in_group('', parent))
# False
print("Expected to be False: ", is_user_in_group('', child))
# False