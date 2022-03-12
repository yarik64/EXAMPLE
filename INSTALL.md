## Build instructions for ALT-Linux using CMake

### Clone source code

    git clone https://github.com/altlinux/example.git

### Create build environment

	mkdir build
	cd build && cmake .. && make -j `nproc`


## Build instruction for ALT-Linux using Gear

### Clone source code

    git clone https://github.com/altlinux/example.git

### Install development packages

    cat .gear/example.spec | grep BuildRequires | awk '{ print $2; }' | xargs apt-get install -y

### Build using Gear

    gear-rpm -ba
