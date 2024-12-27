# Cisco Network Scripts Collection

Welcome to the **Cisco Network Scripts Collection**! This repository contains a collection of scripts designed to automate and simplify tasks related to Cisco networking devices. Whether you're working with routers, switches, or other Cisco hardware, you'll find useful scripts to help manage your network environment.

## Overview

The scripts in this repository are written in **Python** using the **Netmiko** library for SSH automation. These scripts can interact with Cisco devices via SSH, send commands, and capture output for further processing. They are designed to simplify repetitive networking tasks like interface monitoring, configuration backup, and troubleshooting.

### Some examples of what you'll find in this repo:
- Collecting interface information 


## Requirements

To run the scripts, you need to have Python and the necessary libraries installed:

### Python
- Python 3.x

### Libraries
- `netmiko`: A Python library for SSH to network devices.
- `python-dotenv`: To load environment variables from a `.env` file for sensitive information like device credentials.

You can install the required libraries using `pip`:

```bash
pip install netmiko python-dotenv
