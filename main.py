import sys
import requests
from urllib.robotparser import RobotFileParser
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import csv
from PyQt5 import QtWidgets, uic

# Function to get the HTML content of a given URL and return response status
def get_html_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        print(f"Successfully fetched {url}")
        return response.text, True
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None, False

# Function to check if a given URL is allowed to be crawled according to its robots.txt
def is_allowed_by_robots(url, user_agent='*'):
    try:
        parsed_url = urlparse(url)
        robots_url = f"{parsed_url.scheme}://{parsed_url.netloc}/robots.txt"
        
        rp = RobotFileParser()
        rp.set_url(robots_url)
        rp.read()
        
        return rp.can_fetch(user_agent, url)
    except Exception as e:
        print(f"Error reading robots.txt for {url}: {e}")
        return False

# Function to find Vimeo links within iframe tags in the given HTML content
def find_vimeo_links_from_iframe(html_content):
    if not html_content:
        return []
    
    vimeo_links = []
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find all iframe tags in the HTML content
    iframes = soup.find_all('iframe')
    
    # Loop through all iframe tags
    for iframe in iframes:
        src = iframe.get('src', '')
        # Check if the src attribute contains 'vimeo.com'
        if 'vimeo.com' in src:
            vimeo_links.append(src)
    
    return vimeo_links

# Function to find Vimeo links from a given URL
def find_links_from_url(url):
    content, responded = get_html_content(url)
    print(f"Content fetched: {responded}")  # Debugging line
    if not responded:
        return [], False  # If the site did not respond, return an empty list and False
    links = find_vimeo_links_from_iframe(content)
    return links, responded

# Function to write URLs and their corresponding Vimeo links to a CSV file
def write_links_to_csv(urls, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['URL', 'Vimeo Link', 'Permission', 'Responded']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # Iterate over each URL and find Vimeo links
        for url in urls:
            if url.strip() == '':
                continue
            permission = is_allowed_by_robots(url)
            links, responded = [], False
            if permission:
                links, responded = find_links_from_url(url)

            if links:
                for link in links:
                    writer.writerow({'URL': url, 'Vimeo Link': link, 'Permission': permission, 'Responded': responded})
            else:
                writer.writerow({'URL': url, 'Vimeo Link': 'No Vimeo links found', 'Permission': permission, 'Responded': responded})
    
    print(f"Results written to {output_file}")

# Class representing the main window of the application
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('main_window.ui', self)

        # List to keep track of all dynamic QLineEdit widgets
        self.input_fields = []

        # Connect the add button click event to the function
        self.addButton.clicked.connect(self.add_new_input)
        
        # Connect the save button click event to retrieve all inputs and print them
        self.saveButton.clicked.connect(self.save_inputs)

        # Get the layout from the container widget
        self.inputLayout = self.inputContainer.layout()

        # Adjust the layout margins and spacing for closer alignment
        self.inputLayout.setContentsMargins(0, 0, 0, 0)  # No margins
        self.inputLayout.setSpacing(5)  # Minimal spacing between widgets

    # Function to add a new input field to the layout
    def add_new_input(self):
        try:
            # Create a new QLineEdit (input text field) with placeholder text for URL
            new_input = QtWidgets.QLineEdit()
            new_input.setPlaceholderText("Enter URL here")
            
            # Add the new input text field to the layout
            self.inputLayout.addWidget(new_input)
            
            # Keep track of the input field
            self.input_fields.append(new_input)
        except Exception as e:
            print(f"Error adding new input field: {e}")

    # Function to save the inputs and write the links to a CSV file
    def save_inputs(self):
        try:
            # Get the text from the static QLineEdit
            static_input = self.lineEdit.text()
            
            # Get the text from each dynamic QLineEdit in the list
            dynamic_inputs = [input_field.text() for input_field in self.input_fields]
            
            # Print the static input and the list of dynamic inputs
            print("Static Input:", static_input)
            print("Dynamic Inputs:", dynamic_inputs)

            # Remove leading, trailing, and all embedded spaces from each URL
            dynamic_inputs = [url.strip().replace(" ", "") for url in dynamic_inputs]

            

            # Write the links to a CSV file
            write_links_to_csv(output_file=static_input, urls=dynamic_inputs)
        except Exception as e:
            print(f"Error saving inputs: {e}")

# Entry point of the application
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
