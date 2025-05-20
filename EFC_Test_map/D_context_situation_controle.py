# Louis Janssens & GitHub Copilot - 19/05/2025

class ContextSituationControlModule:
    def __init__(self, name):
        self.name = name
        self.paths = []

    def add_path(self, path):
        self.paths.append(path)

    def process(self, context):
        split_path = self.splitter(context)
        for path in self.paths:
            print(f"Processing path: {path.name} with context: {context}")
        if context in ["happy", "joy", "positive"]:
            return "positive"
        elif context in ["sad", "anger", "negative"]:
            return "negative"
        else:
            return "neutral"

    def splitter(self, context):
        return context.split()

class Path:
    def __init__(self, name):
        self.name = name