Name:           govc
Version:        0.27.4
Release:        1%{?dist}
Summary:        GOVC Vmware command line utility

Group:          Applications/System
License:        None
URL:            https://github.com/vmware/govmomi

# Use cautions with this setting.  This undefine will ALLOW rpmbuild to fetch
# the tarball automatically.
%undefine _disable_source_fetch

Source0:        https://github.com/vmware/govmomi/releases/download/v0.27.4/govc_Linux_x86_64.tar.gz

#BuildRequires: coreutils
#Requires:

%description
govc

%prep
%setup -q -c govc 

mkdir -p %{buildroot}/usr/local/bin/
cp govc %{buildroot}/usr/local/bin/

%files
%defattr(-,root,root)

%doc README.md
%doc CHANGELOG.md
%doc LICENSE.txt

/usr/local/bin/govc


%changelog
