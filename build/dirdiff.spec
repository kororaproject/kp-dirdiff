%define debug_package %{nil}

Name:           dirdiff
Version:        2.1
Release:        1%{?dist}
Summary:        Display, merge and patch differences between directories

Group:          Development/Tools
License:        GPLv2
URL:            https://www.samba.org/ftp/paulus/
Source0:        https://www.samba.org/ftp/paulus/%{name}-%{version}.tar.gz

#BuildRequires: tcl-devel
Requires:       tcl

%description
Dirdiff is a graphical tool for displaying the differences between
directory trees and for merging changes from one tree into another.
Dirdiff can handle up to 5 trees.  It displays a main window with a
list of the files which are different between the trees, with colored
squares to indicate the relative ages of the versions.  A menu allows
you to display the differences between any two of the versions in
another window.  Another menu allows you to copy the file from one
tree to another.


%prep
%setup -q


%build


%install
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
install -m 755 %{name} $RPM_BUILD_ROOT/%{_bindir}/%{name}


%files
%defattr(-,root,root,-)
%{_bindir}/%{name}

%changelog
* Thu Aug 27 2015 Chris Smart<csmart@kororaproject.org> - 2.1-1
- Initial package of dirdiff for Fedora.


