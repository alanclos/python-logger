## Python Logging Example

### Purpose

To create a logger that writes logs to stdout and stderr based on message type.  

This is useful in containerized apps where logs are being captured by sidecar containers or some other implementation

### Usage

By default, the class will write CRITICAL ERROR WARNING to stderr and INFO DEBUG to stdout
