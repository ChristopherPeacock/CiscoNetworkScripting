# Cisco Network Scripts Collection

Welcome to my **Cisco Network Scripts Collection**! This repository contains a collection of scripts designed to automate and simplify tasks related to Cisco networking devices. 

## Overview

The scripts in this repository are written in **Python** using the **Netmiko** library for SSH automation. These scripts can interact with Cisco devices via SSH, send commands, and capture output for further processing. They are designed to simplify repetitive networking tasks like interface monitoring, configuration backup, and troubleshooting.

### Instructions: 
1) Setup a account on https://developer.cisco.com/site/sandbox/
2) Select a always-on sand box, I have chosen IOS XR Programmabilty AlwaysOn
3) Your can access the device via SSH and in the Instructions there will be creditials
4) Launch the Virtual device

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
