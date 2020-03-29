import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class MyGrid(Widget):
    name = ObjectProperty(None)
    lname = ObjectProperty(None)

    def btn(self):
        print(f"{self.name.text}, {self.lname.text}")

class DyApp(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    DyApp().run()

