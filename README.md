LemmMade Etsy Alt Generator

This project contains a Python script that generates and adjusts alt text descriptions for Etsy images. It summarizes each description to fit within a specified character limit, while retaining the main content.
Prerequisites

Before you start, ensure you have the following:

    iTerm (Mac's Terminal application) installed.
    Homebrew installed, which is used to install software packages on macOS.
    Visual Studio Code (VS Code) installed, a popular code editor.

Steps to Set Up

Follow these detailed steps to get everything set up, even if you've never used Python before.
1. Install Homebrew

If you don’t already have Homebrew installed, follow these steps:

    Open iTerm (or the regular Terminal app).

    Paste the following command to install Homebrew:

    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

    Follow the on-screen instructions to complete the installation.

    You might need to enter your Mac's password during installation.

2. Use Homebrew to Install Python

Now that Homebrew is installed, you can use it to install Python:

    In iTerm, run:

brew install python

Once installed, check if Python is installed correctly:

    python3 --version

    You should see an output like Python 3.x.x. This means Python 3 is installed.

3. Install Visual Studio Code

If you don’t already have Visual Studio Code:

    Download it from the official website.
    Install VS Code by dragging it to your Applications folder.

4. Clone This Repository Using iTerm

    Navigate to a folder where you want to store this project. For example, your Desktop:

cd ~/Desktop

Clone the Repository:

    If you have set up SSH with GitHub, use:

git clone git@github.com:justmolliecate/LemmMade-Etsy-Alt-Generator.git

Otherwise, use HTTPS:

    git clone https://github.com/justmolliecate/LemmMade-Etsy-Alt-Generator.git

Navigate to the Project Folder:

    cd LemmMade-Etsy-Alt-Generator

5. Open the Project in Visual Studio Code

    In iTerm, open the project in Visual Studio Code by running:

    code .

    This command opens the current folder (LemmMade-Etsy-Alt-Generator) in VS Code.

6. Install Required Python Packages

This project requires some specific Python packages. To install them, follow these steps:

    In VS Code, open the integrated terminal by going to View > Terminal.

    Run the following command to install the necessary packages:

pip3 install -r requirements.txt

    Note: If pip3 is not recognized, you may need to install pip separately by running:

        python3 -m ensurepip --upgrade

7. Prepare Your Input and Output Folders

    In the Explorer panel on the left side of VS Code, create two folders in your project:
        Right-click on the project folder and select New Folder.
        Name one folder input and the other output.

    Place Your JSON Files in the input Folder:
        Each JSON file should contain image descriptions. Here’s an example of what the content should look like:

        {
            "image1.jpg": "Long description of image 1...",
            "image2.jpg": "Another long description of image 2...",
            ...
        }

8. Run the Script to Process Descriptions

    In VS Code, with the terminal open, ensure you're in the project folder (LemmMade-Etsy-Alt-Generator).

    Run the following command to execute the script:

    python3 summarize_descriptions.py

    This will:
        Read JSON files from the input folder.
        Summarize each description to fit within 250 characters.
        Save each summarized description to a .txt file in the output folder.

9. Check the Output

    Open the output folder in VS Code’s Explorer panel.

    You should see a .txt file for each JSON file processed, containing the summarized descriptions.

    Example contents in output/image_descriptions_summarized.txt:

    image1.jpg: Shortened description for image 1.
    image2.jpg: Shortened description for image 2.

Troubleshooting

    If python3 isn’t recognized, ensure Python 3 was installed properly using Homebrew.
    If you encounter any issues with package installations, try running:

    pip3 install --upgrade pip

    to ensure pip is up to date.

Example Workflow Recap

    Put JSON files in the input folder.
    Run the script using python3 summarize_descriptions.py.
    View summarized descriptions in the output folder.

Additional Notes

    This script uses the Hugging Face Transformers library to summarize text, so the first run may take a while as it downloads model files.
    Feel free to adjust the char_limit parameter in summarize_descriptions.py to change the character limit.

License

This project is licensed under the MIT License.
