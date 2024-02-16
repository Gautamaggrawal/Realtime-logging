# Real-Time Logging with Django Channels

## Overview
This project implements a real-time logging solution using Django Channels, allowing users to view updates from a remote log file in their web browser without the need for page refreshes. The server-side program monitors the specified log file and streams updates to connected clients via WebSocket, while the web-based client displays these updates in real-time.

## Features
- **Real-Time Updates**: Clients receive log updates in real-time as they occur.
- **Efficient Retrieval**: Only the updates are transmitted, optimizing performance for large log files.
- **Multiple Clients**: The server can handle multiple clients simultaneously.
- **Last 10 Lines**: Clients see the last 10 lines of the log file when they initially load the page. 
- **No Page Refresh**: The web page does not need to be refreshed to see new log updates.

## Requirements
- Python 3.x
- Django
- Django Channels

## Installation
1. Clone the repository:
git clone https://github.com/your/repository.git

markdown
Copy code

2. Install dependencies:

pip install -r requirements.txt

markdown
Copy code

## Usage
1. Run the Django server:

python manage.py runserver

markdown
Copy code

2. Navigate to `http://localhost:8000/log` in your web browser to view the real-time log updates.

3. To monitor a specific log file, update the `log_path` variable in `consumers.py` with the path to your log file.

## File Structure
- **`consumers.py`**: Contains the WebSocket consumer class responsible for streaming log updates to clients.
- **`views.py`**: Defines the Django view for rendering the web-based client.
- **`templates/log.html`**: HTML template for the web-based client.
- **`routing.py`**: Configures routing for WebSocket connections.
- **`settings.py`**: Contains Django settings including Django Channels configuration.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.










