import os

package_name = 'piculator-static-gamma'
name = 'piculator-static-gamma'
desp = 'Static local assets for piculator gamma'
version = input('Please input version')
package_path = f'piculator-static-gamma_{version}'
files_path = f'{package_path}/usr/share/piculator/static/gamma/'
os.makedirs(files_path,exist_ok=True)
os.system(f'cp -r static/** {files_path}')
os.makedirs(f"{package_path}/DEBIAN",exist_ok=True)
control_content = f'''Package: {package_name}
Architecture: all
Name: {name}
Description: {desp}
Version: {version}
Section: base
Author: Piculator Development Team <piculator@protonmail.com>
Maintainer: Piculator Development Team <piculator@protonmail.com>
HomePage: https://github.com/piculator/{package_name}
'''
ctl_file=open(f'{package_path}/DEBIAN/control',mode='w+')
ctl_file.write(control_content)
ctl_file.close()
for r, d, f in os.walk(package_path):
    os.chmod(r, 0o755)
os.system(f'dpkg-deb -b {package_path}')