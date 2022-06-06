from kivy.lang import Builder
from kivymd.app import MDApp


class WeatherMain(MDApp):
    def build(self):
        return Builder.load_file('mainKV.kv')


if __name__ == '__main__':
    WeatherMain().run()
