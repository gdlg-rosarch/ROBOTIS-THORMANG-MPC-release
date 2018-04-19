# Script generated with Bloom
pkgdesc="ROS - This package is a motion module that can play the saved action. This module is based on position control."
url='http://wiki.ros.org/thormang3_action_module'

pkgname='ros-kinetic-thormang3-action-module'
pkgver='0.2.0_1'
pkgrel=1
arch=('any')
license=('Apache 2.0'
)

makedepends=('boost'
'ros-kinetic-catkin'
'ros-kinetic-robotis-controller-msgs'
'ros-kinetic-robotis-framework-common'
'ros-kinetic-roscpp'
'ros-kinetic-roslib'
'ros-kinetic-std-msgs'
'ros-kinetic-thormang3-action-module-msgs'
)

depends=('boost'
'ros-kinetic-robotis-controller-msgs'
'ros-kinetic-robotis-framework-common'
'ros-kinetic-roscpp'
'ros-kinetic-roslib'
'ros-kinetic-std-msgs'
'ros-kinetic-thormang3-action-module-msgs'
)

conflicts=()
replaces=()

_dir=thormang3_action_module
source=()
md5sums=()

prepare() {
    cp -R $startdir/thormang3_action_module $srcdir/thormang3_action_module
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

