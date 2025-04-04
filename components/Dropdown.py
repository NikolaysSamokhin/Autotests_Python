from components.Component import Component


class Dropdown(Component):
    @property
    def type_of(self):
        return "dropdown"