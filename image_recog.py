from skimage.metrics import structural_similarity
import cv2
import os

def preprocess_user_image(user_path, new_width=500, new_height=300):
    user_image = cv2.imread(user_path)
    user_gray = cv2.cvtColor(user_image, cv2.COLOR_BGR2GRAY)
    user_resized = cv2.resize(user_gray, (new_width, new_height))
    return user_resized

def generate_image_paths(base_path, image_names):
    return [os.path.join(base_path, f"{name}.png") for name in image_names]

def compare_images(user_image, comparison_paths, new_width=500, new_height=300):
    total_score = 0
    scores_array = []

    for path in comparison_paths:
        comparison_image = cv2.imread(path)
        comparison_gray = cv2.cvtColor(comparison_image, cv2.COLOR_BGR2GRAY)
        comparison_resized = cv2.resize(comparison_gray, (new_width, new_height))

        # Compute SSIM between user image and comparison image
        score, _ = structural_similarity(user_image, comparison_resized, full=True)
        total_score += score

        # Append the similarity score to the array
        scores_array.append(score)

    # Calculate the average similarity score
    average_score = total_score / len(comparison_paths)
    return average_score

def compare_good_images(user_resized, good_names, base_path):
    good_image_paths = generate_image_paths(base_path, good_names)
    good_average_score = compare_images(user_resized, good_image_paths)
    return good_average_score

def compare_bad_images(user_resized, bad_names, base_path):
    bad_image_paths = generate_image_paths(base_path, bad_names)
    bad_average_score = compare_images(user_resized, bad_image_paths)
    return bad_average_score

def main():
    user_path = r'C:\Users\Siddharth\agribot\images\hc1.png'
    user_resized = preprocess_user_image(user_path)

    base_path = r'C:\Users\Siddharth\agribot\images'
    good_names = ['hc1', 'hc2', 'hc3', 'hc4', 'hc6', 'hc7', 'hc8', 'hc9', 'hc11', 'hP12', 'hP13', 'hP14', 'hp16', 'hp17']
    bad_names = ['dc1', 'dc2', 'dc3', 'dc4']

    good_average_score = compare_good_images(user_resized, good_names, base_path)
    bad_average_score = compare_bad_images(user_resized, bad_names, base_path)

    print(f"Average Similarity Score for Good Images: {good_average_score}")
    print(f"Average Similarity Score for Bad Images: {bad_average_score}")

    if good_average_score > bad_average_score:
        print("It is a Good Crop")
    else:
        print("It is a Bad Crop")

if __name__ == "__main__":
    main()
