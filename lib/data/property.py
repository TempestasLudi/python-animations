class Property:
    def __init__(self, container, name):
        self.container = container
        self.name = name

    def set(self, value):
        container = self.container

        if type(container) == Property:
            container = container.get()

        if type(self.name) == int:
            container[self.name] = value
            return

        if type(self.name) == str:
            setattr(container, self.name, value)
            return

    def get(self):
        container = self.container

        if type(container) == Property:
            container = container.get()

        if type(self.name) == int:
            return container[self.name]

        if type(self.name) == str:
            return getattr(container, self.name)

    def clone(self, container):
        if type(self.container) == Property:
            container = self.container.clone(container)

        return Property(container, self.name)
