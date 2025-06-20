import getpass
from netmiko import ConnectHandler


def check_vtp_mode_off(connection):
    """Check if 'vtp mode off' is present in the running configuration."""
    output = connection.send_command("show running-config | include ^vtp mode")
    return 'vtp mode off' in output


def apply_fix(connection, command):
    connection.send_config_set([command])
    # Save the configuration to persistent storage
    connection.save_config()


def main():
    device = {
        'device_type': 'cisco_xe',
        'host': input('Device IP: '),
        'username': input('Username: '),
        'password': getpass.getpass('Password: '),
        'secret': getpass.getpass('Enable secret (if any): '),
    }

    predefined_command = 'vtp mode off'

    with ConnectHandler(**device) as connection:
        if device['secret']:
            connection.enable()

        if check_vtp_mode_off(connection):
            print("STIG check passed: 'vtp mode off' is configured.")
            return

        print("STIG check failed: 'vtp mode off' not found.")
        choice = input(
            f"Apply predefined fix command ('{predefined_command}')? [y/N]: "
        ).strip().lower()

        if choice == 'y':
            apply_fix(connection, predefined_command)
            print(f"Applied predefined command: {predefined_command}")
        else:
            custom_cmd = input('Enter custom command to fix the issue: ').strip()
            if custom_cmd:
                apply_fix(connection, custom_cmd)
                print(f"Applied custom command: {custom_cmd}")
            else:
                print('No command entered. No changes made.')


if __name__ == '__main__':
    main()

