import PIL.Image
import drawings

class MemeGenerator:
    def __init__(self, image_path, caption):
        self.image_path = image_path
        self.caption = caption

    def generate(self):
        image = self.get_image_object()
        image = drawings.draw_border(image, border_size=10, border_color='black')
        return image

    def get_image_object(self):
        return PIL.Image.open(self.image_path)


image_object = MemeGenerator('./zwift.jpg', 'Something Something').generate()
image_object.save('result.jpg', quality=90)