from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        print('greet')
        user_name = self.root.ids.user_name_input.text.strip()
        if user_name != "":
            self.root.ids.greeting_label.text = f"Hello, {user_name}!"
        else:
            self.root.ids.greeting_label.text = "Please enter your name."


if __name__ == "__main__":
    BoxLayoutDemo().run()