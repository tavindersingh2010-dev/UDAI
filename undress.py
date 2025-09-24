import argparse

def undress_images(input_dir, output_dir):
    # Your code to process images and save results to output_dir
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Undress images.")
    parser.add_argument("--input", required=True, help="Path to the directory containing images to undress.")
    parser.add_argument("--output", required=True, help="Path to the directory where you want to save the results.")
    args = parser.parse_args()
    undress_images(args.input, args.output)
