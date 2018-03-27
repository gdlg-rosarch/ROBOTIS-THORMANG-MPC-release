Name:           ros-kinetic-thormang3-mpc
Version:        0.2.0
Release:        0%{?dist}
Summary:        ROS thormang3_mpc package

Group:          Development/Libraries
License:        Apache 2.0
URL:            http://wiki.ros.org/thormang3_mpc
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-kinetic-ati-ft-sensor
Requires:       ros-kinetic-motion-module-tutorial
Requires:       ros-kinetic-sensor-module-tutorial
Requires:       ros-kinetic-thormang3-action-module
Requires:       ros-kinetic-thormang3-balance-control
Requires:       ros-kinetic-thormang3-base-module
Requires:       ros-kinetic-thormang3-feet-ft-module
Requires:       ros-kinetic-thormang3-gripper-module
Requires:       ros-kinetic-thormang3-head-control-module
Requires:       ros-kinetic-thormang3-kinematics-dynamics
Requires:       ros-kinetic-thormang3-manager
Requires:       ros-kinetic-thormang3-manipulation-module
Requires:       ros-kinetic-thormang3-walking-module
BuildRequires:  ros-kinetic-catkin

%description
ROS packages for the thormang3_mpc (meta package)

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Tue Mar 27 2018 Pyo <pyo@robotis.com> - 0.2.0-0
- Autogenerated by Bloom

* Wed May 24 2017 Pyo <pyo@robotis.com> - 0.1.3-0
- Autogenerated by Bloom

* Mon Apr 24 2017 Pyo <pyo@robotis.com> - 0.1.2-0
- Autogenerated by Bloom

* Fri Aug 19 2016 Pyo <pyo@robotis.com> - 0.1.1-0
- Autogenerated by Bloom

* Thu Aug 18 2016 Pyo <pyo@robotis.com> - 0.1.0-0
- Autogenerated by Bloom

