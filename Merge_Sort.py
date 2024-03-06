import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

class MergeSortVisualizer:
    def __init__(self, array):
        self.array = array
        self.fig, self.ax = plt.subplots()
        self.ax.set_title("Merge Sort Visualization")
        self.bar_rects = self.ax.bar(range(len(self.array)), self.array, color='blue')
        self.animation = None

    def merge_sort(self, start, end):
        if end - start > 1:
            mid = (start + end) // 2
            yield from self.merge_sort(start, mid)
            yield from self.merge_sort(mid, end)
            yield from self.merge(start, mid, end)

    def merge(self, start, mid, end):
        merged_array = []
        left_index, right_index = start, mid

        while left_index < mid and right_index < end:
            if self.array[left_index] < self.array[right_index]:
                merged_array.append(self.array[left_index])
                left_index += 1
            else:
                merged_array.append(self.array[right_index])
                right_index += 1

        while left_index < mid:
            merged_array.append(self.array[left_index])
            left_index += 1

        while right_index < end:
            merged_array.append(self.array[right_index])
            right_index += 1

        for i, value in enumerate(merged_array):
            self.array[start + i] = value
            yield start + i, value

    def update_bars(self, rects, heights):
        for rect, height in zip(rects, heights):
            rect.set_height(height)

    def animate(self, *args):
        rects = self.bar_rects
        heights = [rect.get_height() for rect in rects]

        for index, value in self.animation:
            heights[index] = value

        self.update_bars(rects, heights)

    def visualize(self):
        self.animation = self.merge_sort(0, len(self.array))
        anim = animation.FuncAnimation(self.fig, self.animate, frames=len(self.array)**2,
                                       repeat=False, blit=False)
        plt.show()

if __name__ == "__main__":
    array = random.sample(range(1, 101), 15)
    merge_sort_visualizer = MergeSortVisualizer(array)
    merge_sort_visualizer.visualize()
