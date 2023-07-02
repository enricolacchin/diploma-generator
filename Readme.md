# Diploma Generator

This script generates personalized diplomas in PDF format for participants using a template diploma PDF and an Excel file containing participant names. Each participant's name is replaced in the diploma, and the current date is added. The generated diplomas are saved in the "Diplomas" folder.

## Features:

- Generates personalized diplomas for participants from an Excel file
- Replaces the name field in the template diploma with each participant's name
- Adds the current date to each diploma
- Supports customization of fonts and layout

## Prerequisites

- Python 3.x
- Pandas
- ReportLab
- PyPDF3

## Usage

1. Install the required Python packages by running the following command:

```shell
pip install pandas reportlab PyPDF3
```

2. Place the template diploma PDF named "diploma.pdf" in the same directory as the script.
3. Prepare the participant names in an Excel file named "user_list.xlsx". Ensure that the participant names are in a column named "name".
4. Run the script using the following command:

```shell 
pythone diploma_generator.py
```

5. The generated diplomas will be saved in the "Diplomas" folder.

## Customization

The Diploma Generator script can be customized to fit your specific requirements. Here are a few aspects you can customize:

- **Fonts**: The script utilizes custom fonts for the name and date fields in the generated diplomas. You can replace the font files in the "font" directory with your preferred fonts. Ensure that the font files are in TrueType (.ttf) format. After replacing the font files, update the font names in the script to match the new font files.

- **Diploma Template**: The script assumes the presence of a template diploma PDF named "diploma.pdf" in the same directory. If you have a different diploma template, replace the "diploma.pdf" file with your own template. Make sure that the name and date fields in the template are editable and can be replaced programmatically.

- **Diploma Layout and Coordinates**: It's important to understand the coordinate system used in the PDF template. The script assumes a coordinate system where the origin (0, 0) is located at the bottom-left corner of the page, with positive x-values increasing towards the right and positive y-values increasing towards the top. Adjust the x and y coordinates in the `drawString()` method of the canvas to position the text accurately within your PDF template. You may need to experiment and make adjustments based on your specific template's layout.

**Note**: When adjusting the coordinates, it's recommended to have a visual representation of the PDF template with visible gridlines or markers to help identify the appropriate positions for the text elements.

Feel free to experiment with the script and adjust it according to your specific diploma template and customization needs.

## License

This project is licensed under the [Creative Commons Attribution 4.0 International License](LICENSE).

Please refer to the license file for more information.

If you encounter any issues or have any questions, please open an issue in the GitHub repository.

## Notes 

Get started with the Diploma Generator today and streamline your diploma generation process!

Contributions and feedback are welcome. If you encounter any issues or have any suggestions, please open an issue on GitHub.