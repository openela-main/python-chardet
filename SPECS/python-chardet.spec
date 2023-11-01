Name:           python-chardet
Version:        4.0.0
Release:        5%{?dist}
Summary:        Character encoding auto-detection in Python
License:        LGPLv2
URL:            https://github.com/chardet/chardet
Source0:        %{pypi_source chardet}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

# Circular dependency on pytest
%bcond_without tests
%if %{with tests}
BuildRequires:  python3-pytest
%endif

%global _description\
Character encoding auto-detection in Python. As\
smart as your browser. Open source.

%description %_description


%package -n python3-chardet
Summary:        %{summary}

%description -n python3-chardet %_description


%prep
%autosetup -p1 -n chardet-%{version}

# Remove useless shebangs
# https://github.com/chardet/chardet/commit/1e94b33329
grep -lr "^#\!/usr/bin/env python" chardet/ | xargs sed -i "1d"


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files chardet


%if %{with tests}
%check
%pytest -v
%endif


%files -n python3-chardet -f %{pyproject_files}
%license LICENSE
%doc README.rst
%{_bindir}/chardetect


%changelog
* Mon Feb 21 2022 Tomas Orsava <torsava@redhat.com> - 4.0.0-5
- Add gating configuration and a simple smoke test
- Related: rhbz#1950291

* Tue Feb 08 2022 Tomas Orsava <torsava@redhat.com> - 4.0.0-4
- Add automatically generated Obsoletes tag with the python39- prefix
  for smoother upgrade from RHEL8
- Related: rhbz#1990421

* Tue Aug 10 2021 Mohan Boddu <mboddu@redhat.com> - 4.0.0-3
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 4.0.0-2
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Fri Feb 05 2021 Miro Hrončok <mhroncok@redhat.com> - 4.0.0-1
- Update to 4.0.0
- Fixes: rhbz#1906585
- Fixes: rhbz#1923076

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 22 2020 Miro Hrončok <mhroncok@redhat.com> - 3.0.4-17
- Rebuilt for Python 3.9

* Fri May 22 2020 Miro Hrončok <mhroncok@redhat.com> - 3.0.4-16
- Bootstrap for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 14 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0.4-14
- Subpackage python2-chardet has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0.4-13
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Thu Aug 15 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0.4-12
- Rebuilt for Python 3.8

* Wed Aug 14 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0.4-11
- Bootstrap for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 17 2018 Miro Hrončok <mhroncok@redhat.com> - 3.0.4-8
- Only have one /usr/bin/chardetect

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 13 2018 Miro Hrončok <mhroncok@redhat.com> - 3.0.4-6
- Rebuilt for Python 3.7

* Sun Feb 11 2018 Iryna Shcherbina <ishcherb@redhat.com> - 3.0.4-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.0.4-3
- Python 2 binary package renamed to python2-chardet
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 20 2017 Jeremy Cline <jeremy@jcline.org> - 3.0.4-1
- Update to 3.0.4 (#1441436)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 09 2016 Charalampos Stratakis <cstratak@redhat.com> - 2.3.0-2
- Rebuild for Python 3.6

* Wed Jul 27 2016 Miro Hrončok <mhroncok@redhat.com> - 2.3.0-1
- Update to 2.3.0 (#1150536)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 14 2015 Robert Kuska <rkuska@redhat.com> - 2.2.1-4
- Rebuilt for Python3.5 rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jul 31 2014 Tom Callaway <spot@fedoraproject.org> - 2.2.1-2
- fix license handling

* Wed Jul 02 2014 Miro Hrončok <mhroncok@redhat.com> - 2.2.1-1
- Updated to 2.2.1
- Introduced Python 3 subpackage (upstream has merged the codebase)
- Removed BuildRoot and python_sitelib definition
- Use python2 macros instead of just python

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed Jan 13 2010 Kushal Das <kushal@fedoraproject.org> 2.0.1-1
- New release

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Aug 04 2008 Kushal Das <kushal@fedoraproject.org> 1.0.1-1
- Initial release

