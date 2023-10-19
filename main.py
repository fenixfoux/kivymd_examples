from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem
from kivymd.uix.card import MDCard


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'BlueGray'
        return Builder.load_file('gui_styles.kv')


class WindowManager(ScreenManager):
    """
        this is a screen manager class, used in .kv file to manage screens
        to add new Screen just write his name below, for example:
        WindowManager:
            MainScreen:
            Page1:
            Page2:
            ...
    """
    pass


class MainScreen(Screen):
    """
        this is the main screen which is showing when app starts
    """
    pass


class MD3Card(MDCard):
    """Implements a material design v3 card."""
    text = StringProperty()


class Page1(Screen):
    cards = ['card1', 'card2']

    def on_enter(self):
        self.ids.card_container.clear_widgets()
        for card_text in self.cards:
            # card = MD3Card(text=card_text)
            self.ids.card_container.add_widget(MD3Card(text=card_text))


class Page2(Screen):
    list = ['element1', 'element2', 'element3']

    def on_enter(self):
        self.ids.list_container.clear_widgets()
        for item in self.list:
            list_item = OneLineListItem(text=item)
            self.ids.list_container.add_widget(list_item)


class ExProgressBar(Screen):
    def press_it(self):
        # Grab the current progress bar value
        current = self.ids.my_progress_bar.value
        # If statement to start over after 100
        if current == 1:
            current = 0

        # Increment value by .25
        current += .25
        # Update the progress bar
        self.ids.my_progress_bar.value = current
        # Update the label
        self.ids.my_label.text = f'{int(current * 100)}% Progress'


if __name__ == '__main__':
    MainApp().run()
