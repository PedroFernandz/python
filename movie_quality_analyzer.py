#!/usr/bin/env python3

# Import necessary libraries
import os
import argparse
import ffmpeg
import csv
import re

# Define supported video formats
VIDEO_FORMATS = ['.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv', '.webm', '.m4v']

# Check if a file has a video format
def is_video_format(filename):
    _, ext = os.path.splitext(filename)
    return ext.lower() in VIDEO_FORMATS

# Analyze the quality of movies in a directory and its subdirectories
def analyze_movie_quality(directory, verbose=False):
    # Initialize the quality dictionary and the movie list
    qualities = {'480p': 0, '720p': 0, '1080p': 0, '4K': 0, 'Unknown': 0}
    movies = []

    # Count the total number of files in the directory and subdirectories
    total_files = sum([len(files) for _, _, files in os.walk(directory)])
    processed_files = 0

    # Iterate through the directory and subdirectories
    for dirpath, _, filenames in os.walk(directory):
        for file in filenames:
            processed_files += 1

            # Print additional information if verbose mode is enabled
            if verbose:
                percentage = (processed_files / total_files) * 100
                print(f'Processing file {processed_files}/{total_files} ({percentage:.2f}%): {file}')

            # If the file is a video, analyze its quality
            if is_video_format(file):
                file_path = os.path.join(dirpath, file)
                quality = extract_quality_metadata(file_path)
                if not quality:
                    quality = 'Unknown'
                qualities[quality] += 1
                movies.append((file_path, quality))

    # Sort movies alphabetically by their full path
    movies.sort(key=lambda x: x[0])
    return qualities, movies

# Extract the quality of a video file using the ffmpeg library
def extract_quality_metadata(file_path):
    try:
        probe = ffmpeg.probe(file_path)
        video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
        if video_stream:
            height = video_stream['height']

            # Classify quality based on video height
            if 320 <= height < 720:
                return '480p'
            elif 720 <= height < 1080:
                return '720p'
            elif 1080 <= height < 2160:
                return '1080p'
            elif height >= 2160:
                return '4K'
    except ffmpeg.Error:
        pass

    return None

    # Main function of the script
def main():
        # Configure the argument parser
        parser = argparse.ArgumentParser(description='Analyze the quality of movies in a directory and its subdirectories.')
        parser.add_argument('directory', type=str, help='Path to the directory containing the movies.')
        parser.add_argument('-v', '--verbose', action='store_true', help='Display additional information during the process.')

        # Parse the command line arguments
        args = parser.parse_args()
        directory = args.directory
        verbose = args.verbose

        # Check if the directory exists
        if not os.path.isdir(directory):
            print(f'Error: The directory "{directory}" does not exist.')
            return

        # Analyze the quality of movies in the directory and its subdirectories
        qualities, movies = analyze_movie_quality(directory, verbose)

        # Define output file names
        output_txt_file = 'movie_qualities.txt'
        output_csv_file = 'movie_qualities.csv'

        # Save the list of movies and their quality in a text file
        with open(output_txt_file, 'w') as f:
            f.write('List of movies and their quality:\n')
            for movie, quality in movies:
                movie_without_path = movie.replace(directory, '')
                if movie_without_path.startswith('/'):
                    movie_without_path = movie_without_path[1:]
                f.write(f'{movie_without_path}: {quality}\n')
            f.write('\nSummary of movie qualities:\n')
            for quality, count in qualities.items():
                f.write(f'{quality}: {count}\n')

        # Save the list of movies and their quality in a CSV file
        with open(output_csv_file, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(['Movie', 'Quality'])
            for movie, quality in movies:
                movie_without_path = movie.replace(directory, '')
                if movie_without_path.startswith('/'):
                    movie_without_path = movie_without_path[1:]
                csv_writer.writerow([movie_without_path, quality])

        # Print a message informing that the results have been saved in the output files
        print(f'Results saved in files "{output_txt_file}" and "{output_csv_file}".')

    # Execute the main function if the script is run as the main program
if __name__ == '__main__':
        main()

