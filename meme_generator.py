import PIL.Image
import drawings

class MemeGenerator:
    TEXT_COLOR = 'white'
    BACKGROUND_COLOR = 'black'

    def __init__(self, image_path, caption):
        self.image_path = image_path
        self.caption = caption

    def generate(self):
        image = self.get_image_object()
        text_image = drawings.get_text_as_image(
            self.caption,
            text_color = self.TEXT_COLOR,
            text_size=30,
            image_width=image.size[0],
            background_color=self.BACKGROUND_COLOR
        )
        image = drawings.bottom_expand_image_with_image(image, text_image, background_color=self.BACKGROUND_COLOR)
        image = drawings.draw_border(image, border_size=10, border_color=self.BACKGROUND_COLOR)
        return image

    def get_image_object(self):
        return PIL.Image.open(self.image_path)


image_object = MemeGenerator('./zwift.jpg', 'Something Something').generate()
image_object.save('result.jpg', quality=90)