Name:           ros-jade-multires-image
Version:        0.1.0
Release:        0%{?dist}
Summary:        ROS multires_image package

Group:          Development/Libraries
License:        BSD
URL:            https://github.com/swri-robotics/mapviz
Source0:        %{name}-%{version}.tar.gz

Requires:       opencv-devel
Requires:       qt
Requires:       ros-jade-pluginlib
Requires:       ros-jade-roscpp
Requires:       ros-jade-swri-math-util
Requires:       ros-jade-swri-transform-util
Requires:       ros-jade-swri-yaml-util
Requires:       ros-jade-tf
BuildRequires:  opencv-devel
BuildRequires:  qt-devel
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-pluginlib
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-swri-math-util
BuildRequires:  ros-jade-swri-transform-util
BuildRequires:  ros-jade-swri-yaml-util
BuildRequires:  ros-jade-tf

%description
multires_image

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Tue Sep 29 2015 Marc Alban <malban@swri.org> - 0.1.0-0
- Autogenerated by Bloom

