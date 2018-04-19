# Script generated with Bloom
pkgdesc="ROS - This package is a sensor module for force torque sensors on feet."
url='http://wiki.ros.org/thormang3_feet_ft_module'

pkgname='ros-kinetic-thormang3-feet-ft-module'
pkgver='0.2.0_1'
pkgrel=1
arch=('any')
license=('Apache 2.0'
)

makedepends=('boost'
'eigen3'
'ros-kinetic-ati-ft-sensor'
'ros-kinetic-catkin'
'ros-kinetic-cmake-modules'
'ros-kinetic-robotis-controller-msgs'
'ros-kinetic-robotis-framework-common'
'ros-kinetic-robotis-math'
'ros-kinetic-roscpp'
'ros-kinetic-std-msgs'
'ros-kinetic-thormang3-feet-ft-module-msgs'
'ros-kinetic-thormang3-kinematics-dynamics'
'yaml-cpp'
)

depends=('boost'
'eigen3'
'ros-kinetic-ati-ft-sensor'
'ros-kinetic-cmake-modules'
'ros-kinetic-robotis-controller-msgs'
'ros-kinetic-robotis-framework-common'
'ros-kinetic-robotis-math'
'ros-kinetic-roscpp'
'ros-kinetic-std-msgs'
'ros-kinetic-thormang3-feet-ft-module-msgs'
'ros-kinetic-thormang3-kinematics-dynamics'
'yaml-cpp'
)

conflicts=()
replaces=()

_dir=thormang3_feet_ft_module
source=()
md5sums=()

prepare() {
    cp -R $startdir/thormang3_feet_ft_module $srcdir/thormang3_feet_ft_module
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

