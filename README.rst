========================================================
debian dictionary to create cryptodev-linux dkms package
========================================================

Packages:

- cryptodev-linux-dkms: dkms of cryptodev-linux
- cryptodev-linux-dev: development files for other program

Require:

- dkms
- debhelper

Build:

.. code:: sh

 git clone https://github.com/multiSnow/cryptodev-linux-debian.git
 cd cryptodev-linux-debian
 git submodule update --init
 python3 news2changelog.py
 dpkg-buildpackage -rfakeroot -us -uc -tc -b
