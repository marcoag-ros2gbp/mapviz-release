Name:           ros-indigo-tile-map
Version:        0.0.9
Release:        0%{?dist}
Summary:        ROS tile_map package

Group:          Development/Libraries
License:        BSD
URL:            https://github.com/swri-robotics/mapviz
Source0:        %{name}-%{version}.tar.gz

Requires:       jsoncpp
Requires:       qt
Requires:       qt-devel
Requires:       ros-indigo-mapviz
Requires:       ros-indigo-pluginlib
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-swri-math-util
Requires:       ros-indigo-swri-transform-util
Requires:       ros-indigo-swri-yaml-util
Requires:       ros-indigo-tf
BuildRequires:  jsoncpp-devel
BuildRequires:  qt-devel
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-mapviz
BuildRequires:  ros-indigo-pluginlib
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-swri-math-util
BuildRequires:  ros-indigo-swri-transform-util
BuildRequires:  ros-indigo-swri-yaml-util
BuildRequires:  ros-indigo-tf

%description
Tile map provides a slippy map style interface for visualizing OpenStreetMap and
GooleMap tiles. A mapviz visualization plug-in is also implemented

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Thu Apr 12 2018 Marc Alban <malban@swri.org> - 0.0.9-0
- Autogenerated by Bloom

* Fri Aug 11 2017 Marc Alban <malban@swri.org> - 0.0.8-0
- Autogenerated by Bloom

* Sun Oct 23 2016 Marc Alban <malban@swri.org> - 0.0.7-0
- Autogenerated by Bloom

* Sun Aug 14 2016 Marc Alban <malban@swri.org> - 0.0.6-0
- Autogenerated by Bloom

* Fri May 20 2016 Marc Alban <malban@swri.org> - 0.0.5-0
- Autogenerated by Bloom

* Wed Jan 06 2016 Marc Alban <malban@swri.org> - 0.0.4-0
- Autogenerated by Bloom

* Mon Sep 28 2015 Marc Alban <malban@swri.org> - 0.0.3-0
- Autogenerated by Bloom

* Sun Sep 27 2015 Marc Alban <malban@swri.org> - 0.0.2-0
- Autogenerated by Bloom

* Sat Sep 26 2015 Marc Alban <malban@swri.org> - 0.0.1-0
- Autogenerated by Bloom

