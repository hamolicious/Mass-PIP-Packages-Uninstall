import json
import os


def get_package_list() -> list[str]:
	os.system('pip list --no-color --disable-pip-version-check > temp')
	with open('temp', 'r') as f:
		data = f.read().split('\n')[2::]

	output = []
	for l in data:
		package = l.split(' ')[0].strip()
		if len(package) == 0 : continue

		output.append(
			package
		)

	return output

def cleanup() -> None:
	os.remove('temp')

def generate_uninstall_all_command(packages: list[str], whitelist: list[str]) -> str:
	packages = filter(
		lambda p : p not in whitelist,
		packages
	)

	return 'pip uninstall ' + ' '.join(packages)

def load_whitelist() -> list[str]:
	with open('whitelist.json', 'r') as f:
		return json.load(f)

def uninstall_all_packages(command: str) -> None:
	os.system(f'{command} -y --no-color')

pkg_list = get_package_list()
whitelist = load_whitelist()
command = generate_uninstall_all_command(pkg_list, whitelist)
cleanup()
uninstall_all_packages(command)


