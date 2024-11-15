
# LemmMade Etsy Alt Generator

This project contains a Python script that generates and adjusts alt text descriptions for Etsy images. It summarizes each description to fit within a specified character limit, while retaining the main content.

## Usage

### 1. Clone the Repository

1. Open **iTerm**.
2. Navigate to a folder where you want to save the project:
   ```bash
   cd ~/Desktop
   ```
3. Clone the repository:
   ```bash
   git clone git@github.com:justmolliecate/LemmMade-Etsy-Alt-Generator.git
   ```

### 2. Install the Required Python Packages

Navigate to the project folder and install the necessary packages:

```bash
cd LemmMade-Etsy-Alt-Generator
pip3 install -r requirements.txt
```

### 3. Place JSON Files in the `input` Folder

Place your JSON files in the `input` folder. Each JSON file should contain image descriptions in this format:

```json
{
    "image1.jpg": "Long description of image 1...",
    "image2.jpg": "Another long description of image 2...",
    ...
}
```

### 4. Run the Script

In iTerm, navigate to the project folder if you’re not already there:

```bash
cd ~/Desktop/LemmMade-Etsy-Alt-Generator
```

Run the script:

```bash
python3 summarize_descriptions.py
```

- The script reads each JSON file from the `input` folder, summarizes the descriptions to fit within 250 characters, and saves each summarized description as a `.txt` file in the `output` folder.

### 5. Check the Output

1. Open the `output` folder.
2. Each `.txt` file corresponds to a JSON file processed, with each line formatted as `image_name: summarized_description`.

Example contents in `output/image_descriptions_summarized.txt`:

```
image1.jpg: Shortened description for image 1.
image2.jpg: Shortened description for image 2.
```

### Customizing the Character Limit

If you want to adjust the character limit, open `summarize_descriptions.py` in a text editor, find the `char_limit` parameter in the `process_json_files` function, and change it to your desired limit.

### License

This project is licensed under the MIT License.
