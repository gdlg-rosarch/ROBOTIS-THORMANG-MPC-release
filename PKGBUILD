# Script generated with Bloom
pkgdesc="ROS - This package describes robot manager to execute THORMANG3's motion modules."
url='http://wiki.ros.org/thormang3_manager'

pkgname='ros-kinetic-thormang3-manager'
pkgver='0.2.0_1'
pkgrel=1
arch=('any')
license=('Apache 2.0'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-robotis-controller'
'ros-kinetic-roscpp'
'ros-kinetic-thormang3-action-module'
'ros-kinetic-thormang3-base-module'
'ros-kinetic-thormang3-feet-ft-module'
'ros-kinetic-thormang3-gripper-module'
'ros-kinetic-thormang3-head-control-module'
'ros-kinetic-thormang3-manipulation-module'
'ros-kinetic-thormang3-walking-module'
)

depends=('ros-kinetic-robotis-controller'
'ros-kinetic-roscpp'
'ros-kinetic-thormang3-action-module'
'ros-kinetic-thormang3-base-module'
'ros-kinetic-thormang3-description'
'ros-kinetic-thormang3-feet-ft-module'
'ros-kinetic-thormang3-gripper-module'
'ros-kinetic-thormang3-head-control-module'
'ros-kinetic-thormang3-imu-3dm-gx4'
'ros-kinetic-thormang3-manipulation-module'
'ros-kinetic-thormang3-walking-module'
)

conflicts=()
replaces=()

_dir=thormang3_manager
source=()
md5sums=()

prepare() {
    cp -R $startdir/thormang3_manager $srcdir/thormang3_manager
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

