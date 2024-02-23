# Copyright 2024 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-urwid
Epoch: 100
Version: 2.6.13
Release: 1%{?dist}
BuildArch: noarch
Summary: A full-featured console (xterm et al.) user interface library
License: LGPL-2.1-or-later
URL: https://github.com/urwid/urwid/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-wheel

%description
Urwid is a console user interface library for Python on Linux, OSX,
Cygwin or other unix-like OS. It includes many features useful for text
console application developers.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-urwid
Summary: A full-featured console (xterm et al.) user interface library
Requires: python3
Provides: python3-urwid = %{epoch}:%{version}-%{release}
Provides: python3dist(urwid) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-urwid = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(urwid) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-urwid = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(urwid) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-urwid
Urwid is a console user interface library for Python on Linux, OSX,
Cygwin or other unix-like OS. It includes many features useful for text
console application developers.

%files -n python%{python3_version_nodots}-urwid
%license COPYING
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-urwid
Summary: A full-featured console (xterm et al.) user interface library
Requires: python3
Provides: python3-urwid = %{epoch}:%{version}-%{release}
Provides: python3dist(urwid) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-urwid = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(urwid) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-urwid = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(urwid) = %{epoch}:%{version}-%{release}

%description -n python3-urwid
Urwid is a console user interface library for Python on Linux, OSX,
Cygwin or other unix-like OS. It includes many features useful for text
console application developers.

%files -n python3-urwid
%license COPYING
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-urwid
Summary: A full-featured console (xterm et al.) user interface library
Requires: python3
Provides: python3-urwid = %{epoch}:%{version}-%{release}
Provides: python3dist(urwid) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-urwid = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(urwid) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-urwid = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(urwid) = %{epoch}:%{version}-%{release}

%description -n python3-urwid
Urwid is a console user interface library for Python on Linux, OSX,
Cygwin or other unix-like OS. It includes many features useful for text
console application developers.

%files -n python3-urwid
%license COPYING
%{python3_sitelib}/*
%endif

%changelog
