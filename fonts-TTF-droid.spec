Summary:	Droid Fonts family
Name:		fonts-TTF-droid
Version:	0
Release:	5
License:	Apache License
Group:		Fonts
Source0:	https://raw.github.com/android/platform_frameworks_base/master/data/fonts/DroidSans.ttf
# Source0-md5:	9e94decf013d3e2c9adcc0b97cc5ce44
Source1:	https://raw.github.com/android/platform_frameworks_base/master/data/fonts/DroidSansMono.ttf
# Source1-md5:	78c0de8abf66567262ee5e4e653fc11c
Source2:	https://raw.github.com/android/platform_frameworks_base/master/data/fonts/DroidSerif-Bold.ttf
# Source2-md5:	9926100f7b25b9ca87dbd57adba1342e
Source3:	https://raw.github.com/android/platform_frameworks_base/master/data/fonts/DroidSerif-BoldItalic.ttf
# Source3-md5:	21038fbc8406c85a0ceb5d57fb48db22
Source4:	https://raw.github.com/android/platform_frameworks_base/master/data/fonts/DroidSerif-Italic.ttf
# Source4-md5:	f2a7b8b7458572a698ecdc04a0a3313a
Source5:	https://raw.github.com/android/platform_frameworks_base/master/data/fonts/DroidSerif-Regular.ttf
# Source5-md5:	4ce04d15fc21fd3eb35b3845af275e7b
Source6:	https://raw.github.com/android/platform_frameworks_base/master/data/fonts/NOTICE
# Source6-md5:	9645f39e9db895a4aa6e02cb57294595
Source7:	https://raw.github.com/android/platform_frameworks_base/master/data/fonts/README.txt
# Source7-md5:	83544262a86f1f1ec761e75897df92bc
URL:		http://www.droidfonts.com/
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/TTF
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		ttffontsdir	%{_fontsdir}/TTF

%description
The Droid family of fonts was designed by Ascender’s Steve Matteson
beginning in the fall of 2006. The goal was to provide optimal
quality and reading comfort on a mobile handset. The Droid fonts
were optimized for use in application menus, web browsers and for
other screen text.

%prep
%setup -qcT

cp %{SOURCE6} %{SOURCE7} .

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ttffontsdir}

cp -a %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} \
	%{SOURCE5} $RPM_BUILD_ROOT%{ttffontsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%doc NOTICE README.txt
%{ttffontsdir}/*.ttf

