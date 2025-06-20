# Network-Architecture-Archive
Python Scripts with Netmiko to automate STIG Deployments to IOS-XE Switches and Routers

## vtp_stig_check.py

This script connects to a Cisco IOS XE device using Netmiko and verifies the DISA STIG requirement that VTP is disabled (`vtp mode off`). If the configuration is missing, the script can automatically apply the predefined command or a custom command provided by the user.

Run the script and follow the prompts for connection details. When the device does not comply with the STIG setting, you will be asked whether to apply the predefined fix or specify your own remediation command.
