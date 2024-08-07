Certainly! Here is the revised `README.md` file with the additional information:

```markdown
# Vimeo Link Extractor

Vimeo Link Extractor is a Python application that scans a list of URLs to find Vimeo video links embedded within iframes. The application checks the robots.txt file of each website to ensure crawling permissions before fetching the HTML content. The results, including URLs, Vimeo links, permission status, and response status, are saved to a CSV file. The application also includes a GUI for ease of use.

## Features

- **Fetch Vimeo Links:** Extract Vimeo video links from iframes in the HTML content of given URLs.
- **Robots.txt Check:** Ensure that the URL is allowed to be crawled according to its robots.txt file.
- **CSV Output:** Save the results, including URLs, Vimeo links, permission status, and response status, to a CSV file.
- **GUI Interface:** User-friendly interface to input URLs and manage the extraction process.

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/your-username/vimeo-link-extractor.git
    cd vimeo-link-extractor
    ```

2. **Set up the virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Running the GUI

1. **Start the application:**

    ```sh
    python main.py
    ```

2. **Using the GUI:**

    - **Add Link:** Click on the "Add link" button to add new input fields for URLs.
    - **CSV File:** Enter the name of the CSV file where results will be saved.
    - **Scan and Save:** Click on the "Scan and save" button to process the URLs and save the results.

### Command Line Usage

You can also modify and run the script directly from the command line for batch processing without using the GUI.

### Executable

An executable version of the application is available as `main.exe`. You can run it directly without needing to set up a Python environment.

```sh
./dist/main.exe
```

## Directory Structure

```
Vimeo Link Extractor/
│
├── build/
├── dist/
├── venv/
├── beispiel.csv
├── Example.csv
├── main.exe
├── main.py
├── main.spec
├── main_window.py
├── main_window.ui
├── requirements.txt
├── test_page.html
├── urls.txt
└── vimeo_links.csv
```

### Important Files

- **`main.py`:** Entry point of the application, containing GUI logic using PyQt5.
- **`main_window.py`:** Contains the MainWindow class for the GUI.
- **`main_window.ui`:** The Qt Designer file for the GUI layout.
- **`requirements.txt`:** List of Python dependencies.
- **`main.exe`:** Executable version of the application for easy deployment.
- **`Example.csv`:** Example input CSV file.
- **`vimeo_links.csv`:** Example output CSV file after running the application.

## Example Output

Here is an example of the output CSV file structure:

```csv
URL,Vimeo Link,Permission,Responded
http://localhost:8000/test_page.html,https://player.vimeo.com/video/987240751?h=d84ce88b14,True,True
http://localhost:8000/test_page.html,https://player.vimeo.com/video/933709897?h=76d89ec160,True,True
http://example.com,No Vimeo links found,True,True
https://elfsight.com/vimeo-video-gallery-widget/examples/,No Vimeo links found,False,False
https://www.youtube.com/,No Vimeo links found,True,True
1234,No Vimeo links found,False,False
```

## Dependencies

- **Python 3.6+**
- **requests:** For making HTTP requests to fetch HTML content.
- **beautifulsoup4:** For parsing HTML and extracting iframe tags.
- **PyQt5:** For creating the GUI.

Install dependencies using:

```sh
pip install requests beautifulsoup4 PyQt5
```

## Contributing

1. **Fork the repository**
2. **Create your feature branch:**

    ```sh
    git checkout -b feature/your-feature
    ```

3. **Commit your changes:**

    ```sh
    git commit -m 'Add some feature'
    ```

4. **Push to the branch:**

    ```sh
    git push origin feature/your-feature
    ```

5. **Open a pull request**

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by the need to efficiently extract Vimeo links from multiple URLs with ease.
- Thanks to the developers of the libraries used in this project.

```

This revised `README.md` includes information about the directory structure and the availability of an executable version of the application. Let me know if you need any further modifications!
