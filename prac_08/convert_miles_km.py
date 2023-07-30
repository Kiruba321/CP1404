from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    output_text = StringProperty()

    def build(self):
        self.title = "Miles to Kilometers Converter"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert(self, value):
        try:
            miles = float(value) if value else 0.0
            kilometers = miles * MILES_TO_KM
            self.output_text = f"{kilometers:.2f} km"
        except ValueError:
            self.output_text = "0.0 km"

    def handle_increment(self, increment):
        try:
            miles = float(self.root.ids.input_miles.text) if self.root.ids.input_miles.text else 0.0
            miles += increment
            self.root.ids.input_miles.text = str(miles)
            self.handle_convert(self.root.ids.input_miles.text)
        except ValueError:
            self.output_text = "0.0 km"


if __name__ == "__main__":
    MilesConverterApp().run()