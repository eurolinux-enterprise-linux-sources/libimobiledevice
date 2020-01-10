Name:          libimobiledevice
Version:       1.2.0
Release:       1%{?dist}
Summary:       Library for connecting to mobile devices

Group:         System Environment/Libraries
License:       LGPLv2+
URL:           http://www.libimobiledevice.org/
Source0:       http://www.libimobiledevice.org/downloads/%{name}-%{version}.tar.bz2
Patch1:        0001-Fix-installation_proxy-when-using-GnuTLS-instead-of-.patch
Patch2:        CVE-2016-5104.patch
Patch3:        0001-Add-new-function-to-get-the-underlying-file-descript.patch
Patch4:        0001-Updated-gnutls-certificate-callback-to-new-API-backw.patch
Patch5:        0001-Fix-SSL-version-negotiation-for-newer-versions-of-Op.patch
Patch6:        0001-idevice-Update-GnuTLS-code-to-support-iOS-10.patch
Patch7:        0001-userpref-GnuTLS-Fix-pairing-record-generation-and-im.patch

BuildRequires: glib2-devel
BuildRequires: gnutls-devel
BuildRequires: libgcrypt-devel
BuildRequires: libplist-devel
BuildRequires: libplist-python
BuildRequires: libtasn1-devel
BuildRequires: libusbmuxd-devel
BuildRequires: libusbx-devel
BuildRequires: libxml2-devel

%description
libimobiledevice is a library for connecting to mobile devices including phones 
and music players

%package devel
Summary: Development package for libimobiledevice
Group: Development/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Files for development with libimobiledevice.

%package utils
Summary: Utilites for libimobiledevice
Group: Applications/System
Requires: %{name}%{?_isa} = %{version}-%{release}

%description utils
Utilites for use with libimobiledevice.

%package python
Summary: Python bindings for libimobiledevice
Group: Development/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}

%description python
Python bindings for libimobiledevice.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

# Fix dir permissions on html docs
chmod +x docs/html

%build
%configure --disable-static --disable-openssl --enable-dev-tools --without-cython
# Remove rpath as per https://fedoraproject.org/wiki/Packaging/Guidelines#Beware_of_Rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags} V=1

%install
make install DESTDIR=%{buildroot}

#Remove libtool archives.
find %{buildroot} -type f -name "*.la" -delete

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{!?_licensedir:%global license %%doc}
%license COPYING.LESSER
%doc AUTHORS README
%{_libdir}/libimobiledevice.so.6*

%files utils
%doc %{_datadir}/man/man1/idevice*
%{_bindir}/idevice*

%files devel
%doc docs/html/
%{_libdir}/pkgconfig/libimobiledevice-1.0.pc
%{_libdir}/libimobiledevice.so
%{_includedir}/libimobiledevice/

%files python
#%{python_sitearch}/imobiledevice*

%changelog
* Wed Mar 01 2017 Bastien Nocera <bnocera@redhat.com> - 1.2.0-1
+ libimobiledevice-1.2.0-1
- Rebase to 1.2.0
- Fix iOS trust issues
Resolves: #1387253

* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 1.1.5-6
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.1.5-5
- Mass rebuild 2013-12-27

* Tue Nov 05 2013 Bastien Nocera <bnocera@redhat.com> 1.1.5-4
- Re-enable RPM-wide CFLAGS (regression in 1.1.5-2)
Resolves: #884524

* Mon Nov 04 2013 Bastien Nocera <bnocera@redhat.com> 1.1.5-3
- Add missing libgcrypt BR
Resolves: #884524

* Tue Oct  8 2013 Matthias Clasen <mclasen@redhat.com> - 1.1.5-2
- Disable strict aliasing (related: #884524)

* Tue Mar 19 2013 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.5-1
- New 1.1.5 release

* Thu Feb 21 2013 Bastien Nocera <bnocera@redhat.com> 1.1.4-6
- Add patch to avoid multi-byte characters from being stripped
  from the device name

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Sep 05 2012 Bastien Nocera <bnocera@redhat.com> 1.1.4-4
- Don't make upowerd crash when run under systemd (#834359)

* Fri Aug 10 2012 Rex Dieter <rdieter@fedoraproject.org> - 1.1.4-3
- disable broken python/cython bindings (for now, currently FTBFS)
- track soname
- tighten  subpkg deps

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Apr 10 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 1.1.4-1
- New 1.1.4 release

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 08 2011 Bastien Nocera <bnocera@redhat.com> 1.1.1-4
- All the version of Fedora are > 13 now

* Thu Dec 01 2011 Bastien Nocera <bnocera@redhat.com> 1.1.1-3
- Add iOS 5 support patches from upstream

* Wed Sep 21 2011 Bastien Nocera <bnocera@redhat.com> 1.1.1-2
- Fix compilation against recent version of gnutls

* Fri Apr 29 2011 Peter Robinson <pbrobinson@gmail.com> 1.1.1-1
- New 1.1.1 release

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Dec 26 2010 Bastien Nocera <bnocera@redhat.com> 1.1.0-1
- Update to 1.1.0

* Sun Nov 28 2010 Peter Robinson <pbrobinson@gmail.com> 1.0.4-1
- New 1.0.4 release

* Mon Oct  4 2010 Peter Robinson <pbrobinson@gmail.com> 1.0.3-1
- New 1.0.3 release

* Sun Aug 01 2010 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 1.0.2-3
- Allow build against swig-2.0.0

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jun 20 2010 Peter Robinson <pbrobinson@gmail.com> 1.0.2-1
- New upstream stable 1.0.2 release

* Wed May 12 2010 Peter Robinson <pbrobinson@gmail.com> 1.0.1-1
- New upstream stable 1.0.1 release

* Sun Mar 21 2010 Peter Robinson <pbrobinson@gmail.com> 1.0.0-1
- New upstream stable 1.0.0 release

* Mon Feb 15 2010 Peter Robinson <pbrobinson@gmail.com> 0.9.7-3
- Add patch to fix DSO linking. Fixes bug 565084

* Wed Feb  3 2010 Peter Robinson <pbrobinson@gmail.com> 0.9.7-2
- Package review updates, add developer docs

* Wed Jan 27 2010 Peter Robinson <pbrobinson@gmail.com> 0.9.7-1
- New package for new library name. Update to 0.9.7

* Sun Jan 24 2010 Peter Robinson <pbrobinson@gmail.com> 0.9.6-1
- Update to 0.9.6 release

* Sat Jan  9 2010 Peter Robinson <pbrobinson@gmail.com> 0.9.5-3
- Updated to the new python sysarch spec file reqs

* Tue Dec 15 2009 Peter Robinson <pbrobinson@gmail.com> 0.9.5-2
- Update python bindings

* Sat Dec 12 2009 Peter Robinson <pbrobinson@gmail.com> 0.9.5-1
- Update to 0.9.5 release for new usbmuxd/libplist 1.0.0 final

* Sat Dec 12 2009 Peter Robinson <pbrobinson@gmail.com> 0.9.4-3
- Rebuild for libplist .so bump

* Wed Oct 28 2009 Peter Robinson <pbrobinson@gmail.com> 0.9.4-2
- Update from libusb to libusb1

* Wed Oct 28 2009 Peter Robinson <pbrobinson@gmail.com> 0.9.4-1
- Update to 0.9.4 release for new usbmuxd 1.0.0-rc1

* Mon Aug 10 2009 Peter Robinson <pbrobinson@gmail.com> 0.9.3-1
- Update to 0.9.3 release

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed May 13 2009 Peter Robinson <pbrobinson@gmail.com> 0.9.1-2
- Add new build reqs

* Tue May 12 2009 Peter Robinson <pbrobinson@gmail.com> 0.9.1-1
- Update to official 0.9.1 release

* Fri Apr 03 2009 - Bastien Nocera <bnocera@redhat.com> - 0.1.0-11.20090325git443edc8
- Update to latest master version

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-10.20090103git5cde554
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 3 2009 Peter Robinson <pbrobinson@gmail.com> 0.1.0-9.git5cde554
- Add back gnutls version patch

* Sat Jan 3 2009 Peter Robinson <pbrobinson@gmail.com> 0.1.0-8.git5cde554
- Upload bzipped source file

* Sat Jan 3 2009 Peter Robinson <pbrobinson@gmail.com> 0.1.0-7.git5cde554
- New git snapshot

* Mon Dec 8 2008 Peter Robinson <pbrobinson@gmail.com> 0.1.0-6.git8c3a01e
- Fix devel dependency 

* Mon Dec 8 2008 Peter Robinson <pbrobinson@gmail.com> 0.1.0-5.git8c3a01e
- Fix gnutls check for new rawhide version

* Mon Dec 8 2008 Peter Robinson <pbrobinson@gmail.com> 0.1.0-4.git8c3a01e
- Rebuild for pkgconfig

* Tue Dec 2 2008 Peter Robinson <pbrobinson@gmail.com> 0.1.0-3.git8c3a01e
- Fix git file generation

* Mon Dec 1 2008 Peter Robinson <pbrobinson@gmail.com> 0.1.0-2.git8c3a01e
- Updates for package review

* Sat Nov 29 2008 Peter Robinson <pbrobinson@gmail.com> 0.1.0-1
- Initial package
