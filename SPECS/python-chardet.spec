%global pypi_name chardet
Name:           python-%{pypi_name}
Version:        3.0.4
Release:        7%{?dist}
Summary:        Character encoding auto-detection in Python

Group:          Development/Languages
License:        LGPLv2
URL:            https://github.com/%{pypi_name}/%{pypi_name}
Source0:        https://files.pythonhosted.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel, python3-setuptools

%global _description\
Character encoding auto-detection in Python. As\
smart as your browser. Open source.

%description %_description

%package -n python3-%{pypi_name}
Summary:        Character encoding auto-detection in Python 3

%description -n python3-%{pypi_name}
Character encoding auto-detection in Python. As 
smart as your browser. Open source.

Python 3 version.

%prep
%setup -q -n %{pypi_name}-%{version}
sed -ie '1d' %{pypi_name}/cli/chardetect.py

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc README.rst
%{python3_sitelib}/*
%{_bindir}/chardetect


%changelog
* Wed Jul 11 2018 Petr Viktorin <pviktori@redhat.com> - 3.0.4-7
- Remove the Python 2 subpackage
  https://bugzilla.redhat.com/show_bug.cgi?id=1590397

* Mon Jun 25 2018 Petr Viktorin <pviktori@redhat.com> - 3.0.4-6
- Allow Python 2 for build
  see https://hurl.corp.redhat.com/rhel8-py2

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

