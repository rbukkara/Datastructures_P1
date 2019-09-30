class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = set()
        self.users = set()

    def add_group(self, group):
        self.groups.add(group)

    def add_user(self, user):
        self.users.add(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if group is None:
        return False

    if user in group.get_users():
        return True

    for subgroup in group.get_groups():
        user_in_subgroup = is_user_in_group(user, subgroup)
        if user_in_subgroup:
            return True

    return False


parent = Group("parent")
child = Group("child")

sub_child = Group("sub_child")
sub_child_user = "sub_child_user"

print(is_user_in_group(sub_child_user, sub_child))

sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

parent.add_user("parent_user")
parent.add_user("parent_user_1")

print(is_user_in_group(sub_child_user, sub_child))
print(is_user_in_group("parent_user", sub_child))
print(is_user_in_group(sub_child_user, parent))

print(is_user_in_group("parent_user", parent))
print("checking for parent_user_1 under parent")
print(is_user_in_group("parent_user_1", parent))
print(is_user_in_group("parent_user", sub_child))
print(is_user_in_group("parent_user", child))
print(is_user_in_group("parent_user", None))

child.add_user("child_user")
print("testing for child_user")
print(is_user_in_group("child_user", None))
print(is_user_in_group("child_user", child))
print(is_user_in_group("child_user", parent))
print(is_user_in_group("child_user", sub_child))
