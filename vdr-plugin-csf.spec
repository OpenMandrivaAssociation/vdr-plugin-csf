%define plugin	csf

Summary:	VDR plugin: CSF Channel Sort&Filter
Name:		vdr-plugin-%plugin
Version:	0.0.1
Release:	19
Group:		Video
License:	GPL
URL:		https://jmorra.tripod.com/
# binaries removed
Source:		%plugin-%version.tar.bz2
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
This plugin provides a menu entry from which the channels list can
be sorted and filtered using different algorithms.

%prep
%setup -q -n %plugin
%vdr_plugin_prep

%build
%vdr_plugin_build

%install
%vdr_plugin_install

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY




%changelog
* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.0.1-16mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 0.0.1-15mdv2009.1
+ Revision: 359304
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.0.1-14mdv2009.0
+ Revision: 197916
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.0.1-13mdv2009.0
+ Revision: 197648
- add vdr_plugin_prep
- bump buildrequires on vdr-devel

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.0.1-12mdv2008.1
+ Revision: 145056
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.0.1-11mdv2008.1
+ Revision: 103081
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.0.1-10mdv2008.0
+ Revision: 49986
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.0.1-9mdv2008.0
+ Revision: 42073
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.0.1-8mdv2008.0
+ Revision: 22735
- rebuild for new vdr


* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 0.0.1-7mdv2007.0
+ Revision: 90908
- rebuild for new vdr

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 0.0.1-6mdv2007.1
+ Revision: 73980
- rebuild for new vdr
- Import vdr-plugin-csf

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 0.0.1-5mdv2007.0
- rebuild for new vdr

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 0.0.1-4mdv2007.0
- stricter abi requires

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 0.0.1-3mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 0.0.1-2mdv2007.0
- rebuild for new vdr

* Wed Jun 21 2006 Anssi Hannula <anssi@mandriva.org> 0.0.1-1mdv2007.0
- initial Mandriva release

