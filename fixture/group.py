class GroupHelper:
    def __init__(self, app):
        self.app = app

    def get_group_list(self):
        self.open_group_editor()
        tree = self.group_editor.window(auto_id="uxAddressTreeView")
        root = tree.tree_root()
        group_list = [node.text() for node in root.children()]
        self.close_group_editor()
        return group_list

    def add_new_group(self, name):
        self.open_group_editor()
        self.group_editor.window(auto_id="uxNewAddressButton").click()
        input = self.group_editor.window(class_name="Edit")
        input.set_text(name)
        input.type_keys("\n")
        self.close_group_editor()

    def del_group(self, name):
        self.open_group_editor()

        tree = self.group_editor.window(auto_id="uxAddressTreeView")
        tree.get_item([0]).get_child(name).click()

        self.group_editor.window(auto_id="uxDeleteAddressButton").click()
        self.group_editor.window(auto_id="uxDeleteAddressButton").click()

        self.accept_delete_group()
        self.close_group_editor()

    def open_group_editor(self):
        self.app.main_window.window(auto_id="groupButton").click()
        self.group_editor = self.app.application.window(title="Group editor")
        self.group_editor.wait("visible")

    def accept_delete_group(self):
        self.accept_delete_window = self.app.application.window(title="Delete group")
        self.accept_delete_window.wait("visible")
        self.accept_delete_window.window(auto_id="uxOKAddressButton").click()

    def close_group_editor(self):
        self.group_editor.close
