========================================================
debian dictionary to create cryptodev-linux dkms package
========================================================

Require:

- kernel headers
- dkms
- debhelper

Build:

- download source from https://github.com/cryptodev-linux/cryptodev-linux/archive/cryptodev-linux-1.10.tar.gz
- tar xf cryptodev-linux-1.10.tar.gz && mv cryptodev-linux-cryptodev-linux-1.10 cryptodev-linux-1.10 && cd cryptodev-linux-1.10
- git clone https://github.com/danielrheinbay/cryptodev-linux-debian.git debian
- dpkg-buildpackage -rfakeroot -us -uc -tc -b -j4
- install the cryptodev-linux-dkms package ( and cryptodev-linux-dev for build other program with cryptodev-linux )
