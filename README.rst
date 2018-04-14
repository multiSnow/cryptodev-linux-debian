========================================================
debian dictionary to create cryptodev-linux dkms package
========================================================

Require:

- kernel headers
- dkms
- debhelper

Build:

- download source from http://nwl.cc/pub/cryptodev-linux/cryptodev-linux-1.9.tar.gz
- tar xf cryptodev-linux-1.9.tar.gz && cd cryptodev-linux-1.9
- git clone https://github.com/multiSnow/cryptodev-linux-debian.git debian
- dpkg-buildpackage -rfakeroot -us -uc -tc -b -j4
- install the cryptodev-linux-dkms package ( and cryptodev-linux-dev for build other program with cryptodev-linux )
