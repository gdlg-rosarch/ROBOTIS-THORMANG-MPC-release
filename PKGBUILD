# Script generated with Bloom
pkgdesc="ROS - ROS packages for the thormang3_mpc (meta package)"
url='http://wiki.ros.org/thormang3_mpc'

pkgname='ros-kinetic-thormang3-mpc'
pkgver='0.2.0_1'
pkgrel=1
arch=('any')
license=('Apache 2.0'
)

makedepends=('ros-kinetic-catkin'
)

depends=('ros-kinetic-ati-ft-sensor'
'ros-kinetic-motion-module-tutorial'
'ros-kinetic-sensor-module-tutorial'
'ros-kinetic-thormang3-action-module'
'ros-kinetic-thormang3-balance-control'
'ros-kinetic-thormang3-base-module'
'ros-kinetic-thormang3-feet-ft-module'
'ros-kinetic-thormang3-gripper-module'
'ros-kinetic-thormang3-head-control-module'
'ros-kinetic-thormang3-kinematics-dynamics'
'ros-kinetic-thormang3-manager'
'ros-kinetic-thormang3-manipulation-module'
'ros-kinetic-thormang3-walking-module'
)

conflicts=()
replaces=()

_dir=thormang3_mpc
source=()
md5sums=()

prepare() {
    cp -R $startdir/thormang3_mpc $srcdir/thormang3_mpc
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

