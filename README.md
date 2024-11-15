
# LemmMade Etsy Alt Generator

This project contains a Python script that generates and adjusts alt text descriptions for Etsy images. It summarizes each description to fit within a specified character limit, while retaining the main content.

## Usage

### 1. Clone the Repository

1. Open your terminal (iTerm or similar).
2. Navigate to a folder where you want to save the project:
   ```bash
   cd ~/Desktop
   ```
3. Clone the repository:
   ```bash
   git clone git@github.com:justmolliecate/LemmMade-Etsy-Alt-Generator.git
   ```

### 2. Open the Project in Visual Studio Code

1. Navigate to the project folder:
   ```bash
   cd LemmMade-Etsy-Alt-Generator
   ```
2. Open the project in Visual Studio Code:
   ```bash
   code .
   ```

### 3. Install the Required Python Packages

In Visual Studio Code, open the integrated terminal (go to **View > Terminal**) and run:

```bash
pip3 install -r requirements.txt
```

This installs the necessary packages listed in `requirements.txt`.

### 4. Prepare Input and Output Folders

1. Create two folders within the project:
   - **input** – for the JSON files with original descriptions.
   - **output** – for the summarized descriptions.

   You can do this in Visual Studio Code:
   - Right-click in the **Explorer** panel and choose **New Folder**.
   - Name one folder **input** and the other **output**.

2. **Place JSON Files in the `input` Folder**:
   - Each JSON file should contain image descriptions in this format:
     ```json
     {
         "image1.jpg": "Long description of image 1...",
         "image2.jpg": "Another long description of image 2...",
         ...
     }
     ```

### 5. Run the Script

In the Visual Studio Code terminal, run the script to process the descriptions:

```bash
python3 summarize_descriptions.py
```

- The script reads each JSON file from the `input` folder, summarizes the descriptions to fit within 250 characters, and saves each summarized description as a `.txt` file in the `output` folder.

### 6. Check the Output

1. Open the `output` folder in the **Explorer** panel of Visual Studio Code.
2. You should see a `.txt` file for each JSON file processed, with each line formatted as `image_name: summarized_description`.

   Example output in `output/image_descriptions_summarized.txt`:
   ```
   image1.jpg: Shortened description for image 1.
   image2.jpg: Shortened description for image 2.
   ```

### Troubleshooting

- If `pip3` isn’t recognized, ensure Python 3 is properly installed.
- If you encounter any issues with package installations, try upgrading `pip`:
  ```bash
  pip3 install --upgrade pip
  ```

### Customizing the Character Limit

If you want to adjust the character limit, open `summarize_descriptions.py` in VS Code, find the `char_limit` parameter in the `process_json_files` function, and change it to your desired limit.

### License

This project is licensed under the MIT License.
