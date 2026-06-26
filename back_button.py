from hover_button import  HoverButtonYellow

class BackButton(HoverButtonYellow):
    def __init__(self , current_screen , **kwargs):
        super().__init__(**kwargs)

        self.text = "Back"
        self.current_screen = current_screen

        self.bind(on_press = self.go_back)

    def go_back(self , instance):
        self.current_screen.manager.transition.direction = "right"

        self.current_screen.manager.current = (
            self.current_screen.manager.previous()
        )