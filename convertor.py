import imageio
import os

video = os.path.abspath("diana.mp4")

def gifMaker(inputPath, targetFormat):
	outputPath = os.path.splitext(inputPath)[0] + targetFormat

	print(f"converting {inputPath} \n to {outputPath}")

	reader = imageio.get_reader(inputPath)
	fps = reader.get_meta_data()["fps"]

	writer = imageio.get_writer(outputPath, fps=fps)

	for frames in reader:
		writer.append_data(frames)
		print(f"Frame {frames}")

	print("Oh yeah!!!")
	writer.close()
	
if __name__ == '__main__':
	gifMaker()
