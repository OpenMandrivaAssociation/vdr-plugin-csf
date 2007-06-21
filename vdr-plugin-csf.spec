
%define plugin	csf
%define name	vdr-plugin-%plugin
%define version	0.0.1
%define rel	9

Summary:	VDR plugin: CSF Channel Sort&Filter
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://jmorra.tripod.com/
# binaries removed
Source:		%plugin-%version.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.4.1-6
Requires:	vdr-abi = %vdr_abi

%description
This plugin provides a menu entry from which the channels list can
be sorted and filtered using different algorithms.

%prep
%setup -q -n %plugin

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY


