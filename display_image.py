import pathlib
import time
from tkinter import Button, Canvas, Tk

from PIL import Image, ImageTk

class Window:
	def __init__(self, width, height) -> None:
		self._root = Tk()
		self._root.title = 'tagging'
		self.width = width
		self.height = height
		self.image = None
		self.image_index = 0
		self.images = list(pathlib.Path('/Users/vinceye/fiftyone/open-images-v6/validation/data').iterdir())
		self.canvas = Canvas(self._root, {'bg':'black','width':self.width, 'height':self.height})
		self.canvas.pack()
		self.running = False
		self._root.protocol('WM_DELETE_WINDOW', self.close)

		next_button = Button(self._root, text='Next Image', command=self.next_image)
		next_button.place(x=self.width-100, y=0)
		prev_button = Button(self._root, text='Previous Image', command=self.previous_image)
		prev_button.place(x=0, y=0)

	def _redraw(self):
		self._root.update_idletasks()
		self._root.update()

	def display_image(self, image_index=0):
		# img = self._get_image(image_id)
		self._animate()
		self.image_index = image_index
		self.image = ImageTk.PhotoImage(Image.open(self.images[image_index]))
		self.canvas.create_image(self.width // 2, self.height // 2, image=self.image)
		self.canvas.image = self.image
		
	def _get_image(self, image_id):
		pass

	def wait_for_close(self):
		self.running = True
		while self.running:
			self._redraw()

	def close(self):
		self.running = False

	def _animate(self):
		self._redraw()
		time.sleep(.05)

	def next_image(self):
		if self.image_index < len(self.images) - 1:
			next_index = self.image_index + 1
			self.display_image(next_index)

	def previous_image(self):
		if self.image_index > 0:
			next_index = self.image_index - 1
			self.display_image(next_index)

def main():
	win = Window(1000, 800)

	win.display_image(6)

	win.wait_for_close()
	
if __name__ == '__main__':
	main()
